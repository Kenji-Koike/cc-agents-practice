import logging
import sqlite3

logger = logging.getLogger(__name__)


def authenticate_user(username: str, password: str) -> dict:
    """ユーザー認証を行う"""
    # セキュリティバグ: パスワードを平文でログに出力
    logger.info(f"Authenticating user: {username}, password: {password}")

    # SQLインジェクション: 文字列結合でクエリを構築
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor = conn.execute(query)
    user = cursor.fetchone()

    if user:
        return {"status": "success", "user_id": user[0]}
    return {"status": "failed"}


def verify_jwt_token(token: str) -> dict:
    """JWT トークンを検証する"""
    import base64
    import json

    # セキュリティバグ: 署名の検証なし、有効期限チェックなし
    parts = token.split(".")
    payload = json.loads(base64.b64decode(parts[1] + "=="))
    return payload


# セキュリティバグ: APIキーのハードコーディング
ADMIN_API_KEY = "sk-admin-12345-super-secret-key"
DATABASE_PASSWORD = "prod_db_pass_2024"


def get_admin_data(api_key: str) -> list:
    """管理者データを取得する"""
    if api_key == ADMIN_API_KEY:
        conn = sqlite3.connect("admin.db")
        # SQLインジェクション
        query = f"SELECT * FROM admin_logs WHERE key = '{api_key}'"
        return conn.execute(query).fetchall()
    return []
