from app.db import get_db


def get_giochi():
    db = get_db()
    cursor = db.execute("SELECT * FROM giochi")
    giochi = cursor.fetchall()
    
    if not giochi:
        return []
    
    # Converte sqlite3.Row objects a dict
    return [dict(gioco) for gioco in giochi]