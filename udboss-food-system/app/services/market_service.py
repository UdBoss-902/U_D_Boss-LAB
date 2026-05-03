from app.db.database import get_connection

def add_market_price(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO market_prices (market, crop, date, price)
        VALUES (?, ?, ?, ?)
    """, (data.market, data.crop, data.date, data.price))

    conn.commit()
    conn.close()

    return {"message": "Market price added successfully"}


def get_market_prices(crop: str = None):
    conn = get_connection()
    cursor = conn.cursor()

    if crop:
        cursor.execute("SELECT * FROM market_prices WHERE crop = ?", (crop,))
    else:
        cursor.execute("SELECT * FROM market_prices")

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]