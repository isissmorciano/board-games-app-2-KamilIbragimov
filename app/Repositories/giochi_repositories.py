from app.db import get_db


def get_giochi():
   
    db = get_db()
    giochi = db.execute(
        "SELECT * FROM giochi"
    ).fetchall()
    return giochi