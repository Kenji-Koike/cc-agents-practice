import re


def format_date(date_str: str) -> str:
    """YYYY-MM-DD を MM/DD/YYYY に変換する"""
    # バグ: 入力形式のバリデーションなし
    parts = date_str.split("-")
    return f"{parts[1]}/{parts[2]}/{parts[0]}"


def is_valid_email(email: str) -> bool:
    """簡単な正規表現でメールアドレスを検証する"""
    # 問題: 不完全な正規表現（例: a@b は通過する）
    pattern = r".+@.+"
    return bool(re.match(pattern, email))


def truncate_string(s: str, max_len: int) -> str:
    """文字列を指定した長さに切り詰める"""
    # 問題: 日本語などのマルチバイト文字を考慮していない
    if len(s) <= max_len:
        return s
    return s[:max_len] + "..."
