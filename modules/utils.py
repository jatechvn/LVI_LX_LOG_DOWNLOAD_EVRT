import re
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def extract_datetime_from_filename(filename):
    """
    Trích xuất ngày giờ từ tên tệp tin bằng Regular Expression.
    Định dạng được hỗ trợ có chứa dạng: YYYY-MM-DD HH:MM:SS hoặc tương đương.
    """
    match = re.search(r'(20[2-9]\d)[-_]?(\d{2})[-_]?(\d{2}).*?(\d{2})[-_:]?(\d{2})[-_:]?(\d{2})', filename)
    if match:
        try:
            y, mo, d, h, mi, s = map(int, match.groups())
            return datetime(y, mo, d, h, mi, s)
        except ValueError:
            pass
    return None
