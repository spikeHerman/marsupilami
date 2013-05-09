import datetime

class Principal:
    """Define Principal class.
    
    Arguments:
    name    -- Principal's name(default '')
    surname -- Principal's surname(default '')
    dob     -- Principal's date of birth(default '')
    afm     -- Principal's afm(default '')

    """

    def __init__(self, name='', surname='', dob='', afm=''):
        """Initialization method.

        Initializes all class arguments, defaulting them to ''
        if no value is passed.
        """
        
        self.name = name
        self.surname = surname
        self.dob = dob
        self.afm = afm
        self.litigations = []
        
    
    def commit(self):
        """Commit principal to database.
        
        """

        pass

    
    
