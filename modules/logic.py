import os
import logging
import re
import requests
import urllib.parse
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta

from modules.utils import extract_datetime_from_filename
from modules.constants import DATETIME_FORMAT_PYTHON, DATE_FORMAT_PYTHON

logger = logging.getLogger(__name__)

def download_logs_logic(host, port, user, password, sn_types, link_filter, start_str, end_str, status_filter, download_dir, progress_callback=None, scan_only=False, stop_check=None):
    os.makedirs(download_dir, exist_ok=True)
    
    start_dt = datetime.strptime(start_str, DATETIME_FORMAT_PYTHON)
    end_dt = datetime.strptime(end_str, DATETIME_FORMAT_PYTHON)

    base_url = f"http://{host}:{port}"
    session = requests.Session()
    session.auth = HTTPBasicAuth(user, password)
    
    results = []
    
    try:
        msg = f"Connecting to Everything HTTP {base_url}..."
        logger.info(msg)
        if progress_callback: progress_callback(msg)

        # 1. Build Query
        date_strs = []
        curr = start_dt
        while curr.date() <= end_dt.date():
            date_strs.append(curr.strftime(DATE_FORMAT_PYTHON))
            curr += timedelta(days=1)
            
        type_q = "<" + "|".join(sn_types) + ">" if sn_types else ""
        date_q = "<" + "|".join(date_strs) + ">" if date_strs else ""
        status_q = ""
        if status_filter == "PASS": status_q = "PASS"
        elif status_filter == "FAIL": status_q = "FAIL"
        
        search_query = f"{type_q} {status_q} {date_q}".strip()
        
        params = {
            'search': search_query,
            'json': 1,
            'path_column': 1
        }
        
        # 2. Get Search Results
        res = session.get(f"{base_url}/", params=params, timeout=15)
        res.raise_for_status()
        data = res.json()
        
        items = data.get('results', [])
        found_msg = f"Everything found {len(items)} matching files. Validating..."
        if progress_callback: progress_callback(found_msg)
        
        # 3. Process and Download
        for item in items:
            # Kiểm tra xem người dùng có nhấn STOP không
            if stop_check and stop_check():
                if progress_callback: progress_callback("!!! Process Cancelled by User !!!")
                break

            if item.get('type') != 'file':
                continue
                
            filename = item.get('name', '')
            remote_folder = item.get('path', '')
            upper_filename = filename.upper()
            
            # Kiểm tra bộ lọc đường dẫn (Link Filter)
            if link_filter:
                import fnmatch
                full_remote_path = os.path.join(remote_folder, filename).replace('\\', '/')
                norm_path = full_remote_path.lower()
                norm_filter = link_filter.replace('\\', '/').lower()
                
                if '*' in norm_filter or '?' in norm_filter:
                    fn_pattern = norm_filter
                    if not fn_pattern.startswith('*'):
                        fn_pattern = '*' + fn_pattern
                    if not fn_pattern.endswith('*'):
                        fn_pattern = fn_pattern + '*'
                    if not fnmatch.fnmatch(norm_path, fn_pattern):
                        continue
                else:
                    if norm_filter not in norm_path:
                        continue
            
            # Kiểm tra trạng thái nghiêm ngặt lại bằng Python
            if status_filter == "PASS" and "_PASS" not in upper_filename:
                continue
            if status_filter == "FAIL" and "_FAIL" not in upper_filename:
                continue
                
            # Kiểm tra khung giờ nghiêm ngặt lại bằng Python
            file_dt = extract_datetime_from_filename(filename)
            if not file_dt or not (start_dt <= file_dt <= end_dt):
                continue
                
            # Phân loại theo Machine ID (MMI hoặc SOZ)
            path_parts = remote_folder.replace('\\', '/').split('/')
            machine_id = "Unknown"
            for part in reversed(path_parts):
                if "-" in part and (part.startswith("MMI") or part.startswith("SOZ")):
                    machine_id = part
                    break
                    
            local_machine_dir = os.path.join(download_dir, machine_id)
            os.makedirs(local_machine_dir, exist_ok=True)
            local_path = os.path.join(local_machine_dir, filename)
            
            if scan_only:
                scan_msg = f"Found: {filename} ({machine_id})"
                logger.info(scan_msg)
                if progress_callback: progress_callback(scan_msg)
                results.append(filename)
                continue
                
            if os.path.exists(local_path):
                continue
                
            dl_msg = f"Downloading: {filename} ({machine_id})"
            logger.info(dl_msg)
            if progress_callback: progress_callback(dl_msg)
                
            # Download file trực tiếp qua Everything HTTP File Server
            # Đường dẫn Everything hỗ trợ là: http://host:port/C:/thu_muc/file.zip
            full_remote_path = f"{remote_folder}\\{filename}".replace('\\', '/')
            # Chỉ urlencode các ký tự đặc biệt, giữ lại : và /
            encoded_path = urllib.parse.quote(full_remote_path, safe=":/")
            download_url = f"{base_url}/{encoded_path}"
            
            try:
                dl_res = session.get(download_url, stream=True, timeout=60)
                dl_res.raise_for_status()
                with open(local_path, 'wb') as f:
                    for chunk in dl_res.iter_content(chunk_size=8192):
                        f.write(chunk)
                results.append(local_path)
            except Exception as e:
                err_msg = f"Error downloading {filename}: {e}"
                logger.error(err_msg)
                if progress_callback: progress_callback(err_msg)
                
    except Exception as e:
        logger.error(f"Everything HTTP Logic Error: {e}")
        raise e
        
    return results
