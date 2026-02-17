from app.db import get_db







def get_partite():
   
    db = get_db()
    giochi = db.execute(
        "SELECT * FROM partite"
    ).fetchall()
    return giochi