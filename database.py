import sqlite3 as lite

class DatabaseManager(object):
    """A database manager.

    τρομερη περιγραφη
    
    """
    
    def __init__(self, db):
        """Initializing the database manager.

        """
        # connector to the database
        self.conn = lite.connect(db)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        # getting the cursor
        self.cur = self.conn.cursor()

    def __del__(self):
        """Delete instance.

        """
        self.conn.close()

    def query(self, sql, sequence = None):
        """Query database with arg.

        """
        self.cur.execute(sql, sequence)
        self.conn.commit()
        return self.cur


