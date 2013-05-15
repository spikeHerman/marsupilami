from datetime import date, timedelta
from deadline import Deadline

class Litigation:
    """Define litigation class.

    Διαφορά. Ενδική αντιδικία δύο ή περισσότερων μερών.
    Δύο class attributes περιέχουν τα πιθανά είδη(types) και αντικείμενα(objects) διαφοράς.
    Κάθε instance της κλάσης ορίζει τον χειριστή(handler), τον εντολέα(principal) και την 
    δικάσιμο(hearing_day) της διαφοράς, καθώς και τον τύπο και το είδος της.
    """
    
    kinds = {0:'Αστική', 1:'Ποινική', 2:'Εμπορική', 3:'Εταιρική', 4:'Εργατική', 5:'Διοικητικη', 6:'Αυτοκίνητα'}
    antikeimena = [] #still not defined. Farma help. i need a good translation too.
    
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

    def define_antikeimeno(self, object):
        """ Define antikeimeno of litigation.
    
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
    # προσωρινή(προφανως) προσομοίωση των τύπων διαδικασίας
    # ο τροπος υλοποιησης και η ονομασια πρεπει να διευκρινιστεί.
    # μαζι με άλλα 200 πράγματα
    types = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def __init__(self, kind, litigation, deadlines = []):
        """ Initialize a procedure object.
        
        Instance variables
        kind       -- ο τύπος διαδικασίας
        litigation -- η διαφορά απο την οποία προκύπτει η διαδικασία
        deadlines  -- λίστα με τις προθεσμίες που προκύπτουν απο την 
                      συγκεκριμένη διαδικασία. Default άδεια, γεμίζει
                      μέσω της define_deadlines μεθόδου.
        """
        
        self.kind = kind
        self.litigation = litigation
        self.deadlines = deadlines

    def define_deadlines(self):
        """Define deadlines for this procedure.
        
        Προσδιορίζει τις προθεσμίες της συγκεκριμένης διαδικασίας
        βάσει της δικασίμου της διαφοράς απο την οποία προκύπτει
        (ουτε εγω δε καταλαβα τπτ)
        Προς το παρόν γίνεται χειροκίνητα μιας και δεν έχουμε 
        συζητήσει πως θα γίνει η αυτοματοποίηση.
        Σαν υποθέση εργασίας ορίζουμε 2 τυχαία date objects.
        """
        
        self.deadlines.append(Deadline(date(2013, 6, 12), self))
        self.deadlines.append(Deadline(date(2013, 8, 15), self))

    def set_deadline(self, deadline):
        """Manually set a deadline for this procedure.

        Χειροκίνητος ορισμός μιας προθεσμίας. 
        Δέχεται ως argument ένα date object.
        """
        
        self.deadlines.append(deadline, self)
            
                  
    
class Application:
    """ Application class.
    
    Δικόγραφο, άγνωστο προς το παρόν το αν είναι απαραίτητο.
   
    """

    pass
