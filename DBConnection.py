class DBConnection:

    def __init__(self, db_name):
        import sqlite3
        self.con = sqlite3.connect(db_name)

    def create_table(self, tablename, *args):
        query = "create table if not exists ", tablename, str(args)
        self.con.execute(" ".join(query))

    def update_values(self, tablename, **kwargs):
        query = "insert into", tablename, str(tuple(kwargs.keys())), " values ", str(tuple(kwargs.values()))
        self.con.execute(" ".join(query))
        self.con.commit()

    def close_connection(self):
        self.con.close
