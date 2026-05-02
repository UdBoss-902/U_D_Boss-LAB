from app.db.database import get_connection

def create_farmer(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO farmers (name, location, phone)
        VALUES (?, ?, ?)
    """, (data.name, data.location, data.phone))

    conn.commit()

    farmer_id = cursor.lastrowid
    conn.close()

    return {
        "id": farmer_id,
        "name": data.name,
        "location": data.location,
        "phone": data.phone
    }


def get_farmers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM farmers")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]