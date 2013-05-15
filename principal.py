
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
        self.name = name
        self.surname = surname
        self.vat = vat

class Principal(Operator):
    """Define Principal class.
    
    Inherits Operator class.

    Instance Variables:
    litigations -- List of current litigations owned by Principal

    Class Methods:
    addLitigation(litigation) -- adds litigation to litigations instance variable
    removeLitigation(litigation) -- adds litigation to litigations instance variable
    """

    def __init__(self, name, surname, vat):
        """Initialization method.
        
        """
        super().__init__(name, surname, vat)
        self.litigations = []
    

    def addLitigation(self, lit):
        """Add a new litigation.
        
        """
        self.litigations.append(lit)
            
        
    def removeLitigation(self, lit):
        """Remove litigation.

        """
        self.litigation.remove(lit)

class Handler(Operator):
    """Handler Class
    
    Inherits Operator class
    """

    pass
