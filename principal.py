import database

class Operator:
    """Define Operator class.
    
    Abstraction for operator, any human involved in a litigation
    process.
    Instance Variables:
    name    -- Operator's name.
    surname -- Operator's surname.
    vat     -- Operator's VAT registration number.
    
    """
    def __init__(self, name, surname, vat):
        """Initialize instance.

        """
        self.name = name
        self.surname = surname
        self.vat = vat
        
class Handler(Operator):
    """Handler Class
    
    Inherits Operator class.
    Instance Variables:
    table: the table in database corresponding to handler.

    Class Methods:
    commit_to_db : commits the handler to database.

    """
    table = 'handlers'
    
    def __init__(self, name, surname, vat):
        """Initialize a handler instance.

        Inherit Operator's initialization method.
        Add handler_id equal to None. Will be set when handler is commited to database.
        
        """
        super().__init__(name, surname, vat)
        
        self.handler_id = None
    
    def commit_to_db(self):
        """ Commit handler to database.

        """
        values = (self.name, self.surname, self.vat)
        if self.handler_id:
            raise ValueError('This handler has already been commited')
        else:
            dbm = database.DatabaseManager()
            cursor = dbm.insert(self.table, values)

            self.handler_id = cursor.lastrowid
            # close connection to database
            del(dbm)
            
class Principal(Operator):
    """Define Principal class.
    
    Inherits Operator class.

    Instance Variables:
    table: the table in database corresponding to principal.

    Class Methods:
    commit_to_db : commits the principal to database.

    """

    table = 'principals'

    def __init__(self, name, surname, vat, handler):
        """Initialization method.
        
        """
        super().__init__(name, surname, vat)
        
        self.handled_by = handler
        self.principal_id = None
    
    # Probably not necessary.
    # def addLitigation(self, lit):
    #     """Add a new litigation.
        
    #     """
    #     self.litigations.append(lit)
            
        
    # def removeLitigation(self, lit):
    #     """Remove litigation.

    #     """
    #     self.litigation.remove(lit)
    
    def commit_to_db(self):
        """ Commit principal to database.

        """
        values = (self.name, self.surname, self.vat, self.handled_by.handler_id)
        
        if self.principal_id:
            # if instance has principal_id, it has already been commited.
            raise ValueError('This handler has already been commited') # need to find appropriate error
        else:
            dbm = database.DatabaseManager()
            cursor = dbm.insert(self.table, values)

            self.principal_id = cursor.lastrowid
            # close connection to database
            del(dbm)
        

        
    
