import sqlite3

def init_db():
    con = sqlite3.connect("bot.db.sql")
    cur = con.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            username text,
            text NOT NULL
        )
        '''
    )
    con.commit()
    return con, cur