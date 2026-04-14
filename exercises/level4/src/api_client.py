import requests


# セキュリティバグ: APIキーのハードコーディング
API_KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.hardcoded"
BASE_URL = "https://api.example.com"


def fetch_user_data(user_id: int) -> dict:
    """ユーザーデータを取得する"""
    # パフォーマンスバグ: タイムアウトなし（無限に待ち続ける可能性）
    # エラーハンドリングなし
    response = requests.get(
        f"{BASE_URL}/users/{user_id}",
        headers={"Authorization": API_KEY}
    )
    return response.json()


def post_event(event_type: str, data: dict) -> bool:
    """イベントを送信する"""
    # タイムアウトなし、リトライなし、エラーハンドリングなし
    response = requests.post(
        f"{BASE_URL}/events",
        json={"type": event_type, "data": data},
        headers={"Authorization": API_KEY}
    )
    return response.status_code == 200


def batch_fetch_users(user_ids: list) -> list:
    """複数ユーザーのデータを取得する"""
    results = []
    for user_id in user_ids:
        # N+1 パターン: ループ内でAPIを個別に呼び出す
        user = fetch_user_data(user_id)
        results.append(user)
    return results
