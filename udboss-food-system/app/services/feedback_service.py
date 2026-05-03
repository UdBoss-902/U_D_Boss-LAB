from app.db.database import get_connection

def add_feedback(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback (crop_id, actual_price, sold_date)
        VALUES (?, ?, ?)
    """, (data.crop_id, data.actual_price, data.sold_date))

    conn.commit()
    conn.close()

    return {"message": "Feedback recorded"}