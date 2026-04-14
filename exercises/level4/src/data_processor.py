import sqlite3


def process_large_file(filepath: str) -> list:
    """大きなファイルを処理する"""
    # パフォーマンスバグ: ファイル全体を一度にメモリに読み込む
    with open(filepath) as f:
        all_lines = f.readlines()

    results = []
    for line in all_lines:
        if line.strip():
            results.append(line.strip().upper())
    return results


def get_users_with_orders(conn: sqlite3.Connection) -> list:
    """注文を持つユーザーの一覧を取得する"""
    users = conn.execute("SELECT * FROM users").fetchall()

    result = []
    for user in users:
        # N+1 クエリ: ユーザーごとに個別クエリを発行
        orders = conn.execute(
            "SELECT * FROM orders WHERE user_id = ?", (user[0],)
        ).fetchall()
        result.append({"user": user, "orders": orders})
    return result


def find_user_by_email(users: list, email: str) -> dict:
    """メールアドレスでユーザーを検索する"""
    # パフォーマンスバグ: リストの線形探索（O(n)）
    # 大量データの場合はインデックス付きの辞書を使うべき
    for user in users:
        if user.get("email") == email:
            return user
    return {}


def generate_report(conn: sqlite3.Connection) -> str:
    """月次レポートを生成する"""
    # パフォーマンスバグ: 全データをメモリに読み込んでPython側で集計
    # SQLで集計すべき
    all_orders = conn.execute("SELECT * FROM orders").fetchall()
    all_users = conn.execute("SELECT * FROM users").fetchall()
    all_products = conn.execute("SELECT * FROM products").fetchall()

    total_revenue = sum(order[3] for order in all_orders)
    user_count = len(all_users)
    product_count = len(all_products)

    return f"Revenue: {total_revenue}, Users: {user_count}, Products: {product_count}"
