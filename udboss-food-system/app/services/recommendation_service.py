from app.db.database import get_connection

# --- Trend Detection ---
def get_price_trend(crop: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT price FROM market_prices
        WHERE crop = ?
        ORDER BY date DESC
        LIMIT 3
    """, (crop,))

    rows = cursor.fetchall()
    conn.close()

    prices = [row["price"] for row in rows]

    if len(prices) < 3:
        return "stable"

    if prices[0] > prices[1] > prices[2]:
        return "increasing"
    elif prices[0] < prices[1] < prices[2]:
        return "decreasing"
    else:
        return "stable"


# --- DECISION ENGINE (THIS IS WHAT YOU'RE ASKING ABOUT) ---
def generate_recommendation(crop_batch_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops WHERE id = ?", (crop_batch_id,))
    crop = cursor.fetchone()

    if not crop:
        conn.close()
        return {"error": "Crop not found"}

    trend = get_price_trend(crop["crop"])

    if trend == "increasing":
        action = "DELAY"
        message = "Prices are rising. Wait before harvesting."
    elif trend == "decreasing":
        action = "HARVEST_NOW"
        message = "Prices are dropping. Harvest immediately."
    else:
        action = "MONITOR"
        message = "Prices are stable. Keep monitoring."

    conn.close()

    return {
        "crop_id": crop_batch_id,
        "trend": trend,
        "action": action,
        "message": message
    }