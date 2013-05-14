from principal import Principal, Handler

class Litigation:
    """Define litigation class.

    Διαφορά. Ενδική αντιδικία δύο ή περισσότερων μερών.
    Δύο class attributes περιέχουν τα πιθανά είδη(types) και αντικείμενα(objects) διαφοράς.
    Κάθε instance της κλάσης ορίζει τον χειριστή(handler), τον εντολέα(principal) και την 
    δικάσιμο(hearing_day) της διαφοράς, καθώς και τον τύπο και το είδος της.
    """
    
    kinds = {0:'Αστική', 1:'Ποινική', 2:'Εμπορική', 3:'Εταιρική', 4:'Εργατική', 5:'Διοικητικη', 6:'Αυτοκίνητα'}
    objects = [] #still not defined. Farma help.
    
    def __init__(self, hearing_day, principal = None, handler = None):
        """Initialize a Litigation object.
        
        Δημιουργώντας ένα instance της Litigation class δηλώνουμε την δικάσιμο(hearing day).
        Optional είναι ο χειριστής(handler) και ο εντολέας(principal). Η default τιμή τους 
        είναι None.
        """
        
        self.hearing_day = hearing_day
        self.principal = principal
        self.handler = handler
        
        
    def define_type(self, kind):
        """ Define type of litigation.
        
        Αν εχω καταλάβει καλά δεν είναι κάτι απαραίτητο και 
        γι αυτό δεν ορίζεται στην __init__
        """

        self.kind = kinds[kind]

    def define_object(self, object):
        """ Define object of litigation.
    
        Βλέπε παραπάνω, μας λείπουν πληροφορίες.
        """
        pass

   
    

 class Procedure:
    """ Procedure class.

    Διαδικασία. Η πιο άμεσα χρήσιμη κλάση.
    Βάσει αυτής υπολογίζονται οι προθεσμίες(deadlines) που πρέπει να παρακολουθεί 
    ο χειριστής. Ορίζεται ο τύπος(type) διαδικασίας και η διαφορά(litigation) 
    απο την οποία προκύπτει.
    """
        
    def __init__(self, procedure):
        self.procedure = procedure
                  
    
class Application:
    """ Application class.
    
    Δικόγραφο, άγνωστο προς το παρόν το αν είναι απαραίτητο.
   
    """

    pass
