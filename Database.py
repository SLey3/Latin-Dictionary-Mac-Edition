import sqlite3
class Database:
   def __init__(self, db):
       self.conn = sqlite3.connect(db)
       self.cur = self.conn.cursor()
       self.cur.execute('CREATE TABLE IF NOT EXISTS definitions (id INTEGER PRIMARY KEY, lbl_entry text, definition function, userInput commands')
       self.conn.commit()
       
    def fetch(self):
        self.cur.execute("SELECT * FROM lbl_entry")
        rows = self.cur.fetchall()
        return rows

        