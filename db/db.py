import sqlite3

DBNAME = __file__.replace('db.py', './db.db')


class Database:
    db = None

    def __init__(self):
        self._conn = sqlite3.connect(DBNAME)
        self._cursor = self._conn.cursor()

    @staticmethod
    def get_database():
        if not Database.db:
            Database.db = Database()
        return Database.db

    def execute(self, sql, params=None, unescape=None):
        sql = sql.format(unescape) if unescape else sql
        try:
            if params:
                return self._cursor.execute(sql, params)
            else:
                return self._cursor.execute(sql)
        finally:
            self._conn.commit()

