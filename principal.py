import database

class Operator:
    """Define Operator class.
    
    Abstraction for operator, any human involved in a litigation
    process.
    Instance Variables:
    name    -- Operator's name.
    surname -- Operator's surname.
    vat   -- Operator's VAT registration number.
    
    """
    def __init__(self, name, surname, vat):
        """Initialize instance.

        """
        self.name = name
        self.surname = surname
        self.vat = vat
        
class Handler(Operator):
    """Handler Class
    
    Inherits Operator class
    """
    corresponding_table = 'handlers'
    
    def __init__(self, name, surname, vat):
        """Initialize a handler instance.

        Inherit Operator's initialization method.
        Add handler_id equal to None. Will be set when handler is commited to database.
        
        """
        super().__init__(name, surname, vat)
        self.handler_id = None
    
    def commit_to_db(self, db_name):
        """Commit to database.
        
        """
        pre_script = """
        INSERT INTO {}(name, surname, vat)
        VALUES(?, ?, ?)
        """
        
        sql      = pre_script.format(self.corresponding_table)
        sequence = (self.name, self.surname, self.vat)
        
        if self.handler_id:
            # need to find the appropriate error
            raise ValueError('This handler has already been commited')
        else:
            # query database, commit the changes
            dbm = database.DatabaseManager(db_name)
            cursor = dbm.query(sql, sequence)
            # assign handler id to handler object.
            self.handler_id = cursor.lastrowid
            
            # close the connection to the database.
            del(dbm)
            
        
            
class Principal(Operator):
    """Define Principal class.
    
    Inherits Operator class.

    Instance Variables:
    litigations -- List of current litigations owned by Principal

    Class Methods:
    addLitigation(litigation) -- adds litigation to litigations instance variable
    removeLitigation(litigation) -- adds litigation to litigations instance variable

    """

    correspoding_table = 'principals'

    def __init__(self, name, surname, vat, handler):
        """Initialization method.
        
        """
        super().__init__(name, surname, vat)
        self.handler = handler
    
    
    # def addLitigation(self, lit):
    #     """Add a new litigation.
        
    #     """
    #     self.litigations.append(lit)
            
        
    # def removeLitigation(self, lit):
    #     """Remove litigation.

    #     """
    #     self.litigation.remove(lit)
    
    def commit_to_db(self, db_name):
        """Commit to database.
        
        """
        pre_script = """
        INSERT INTO {}(name, surname, vat, principal_handler)
        VALUES(?, ?, ?, ?)
        """
        
        sql      = pre_script.format(self.corresponding_table)
        sequence = (self.name, self.surname, self.vat, self.handler.handler_id)
        
        if self.principal_id:
            # need to find the appropriate error
            raise ValueError('This principal has already been commited')
        else:
            # query database and commit the changes
            dbm = database.DatabaseManager(db_name)
            cursor = dbm.query(sql, sequence)
            # assign handler id to handler object.
            self.principal_id = cursor.lastrowid

             # close the connection to the database.
            del(dbm)
            

        
    
