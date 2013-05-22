import sqlite3 as lite

class DatabaseManager(object):
    """A database manager.

    τρομερη περιγραφη
    
    """
    
    # A directory of insert sql statements for each table.
    insert_statements = {
        'handlers'   :"INSERT INTO handlers(name, surname ,vat) VALUES(?, ?, ?)",
        'principals' :"INSERT INTO principals(name, surname, vat, handled_by) VALUES(?, ?, ?, ?)",
        'litigations':"INSERT INTO litigations(type, hearing_day, owned_by) VALUES(?, ?, ?)",
        'procedures' :"INSERT INTO procedures(type, procedure_of) VALUES(?, ?)",
        'deadlines'  :"INSERT INTO deadlines(date, expired, deadline_of) VALIUES (?, ?, ?)"
    }
        

    def __init__(self, db = 'testing2.db'):
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

        
    def insert(self, table, values):
        """Insert values into database

        """
        self.cur.execute(self.insert_statements[table], values)
        self.conn.commit()
        return self.cur

        
    
