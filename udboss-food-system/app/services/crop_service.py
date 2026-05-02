from app.db.database import get_connection

def create_crop(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO crops (farmer_id, crop, expected_harvest_date, quantity, status)
        VALUES (?, ?, ?, ?, ?)
    """, (data.farmer_id, data.crop, data.expected_harvest_date, data.quantity, "growing"))

    conn.commit()

    crop_id = cursor.lastrowid
    conn.close()

    return {
        "id": crop_id,
        "farmer_id": data.farmer_id,
        "crop": data.crop,
        "expected_harvest_date": data.expected_harvest_date,
        "quantity": data.quantity,
        "status": "growing"
    }


def get_crops():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM crops")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]