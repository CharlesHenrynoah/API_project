import re


def sanitize(unsafe_str):
    allowed_range = set(range(32, 127))
    safe_str = ''
    for char in unsafe_str:
        cp = ord(char)
        if cp in allowed_range:
            safe_str += char
        elif cp == 9:
            safe_str += ' ' * 4
    return re.sub(r'\s+', ' ', safe_str)