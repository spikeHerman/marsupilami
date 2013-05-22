import database
#import date
#from deadline import Deadline

class Litigation:
    """Define litigation class.

    Διαφορά. Ενδική αντιδικία δύο ή περισσότερων μερών.
    Δύο class attributes περιέχουν τα πιθανά είδη(types) και αντικείμενα(objects) διαφοράς.
    Κάθε instance της κλάσης ορίζει τον χειριστή(handler), τον εντολέα(principal) και την 
    δικάσιμο(hearing_day) της διαφοράς, καθώς και τον τύπο και το είδος της.
    """
    
    kinds = {0:'Αστική', 1:'Ποινική', 2:'Εμπορική', 3:'Εταιρική', 4:'Εργατική', 5:'Διοικητικη', 6:'Αυτοκίνητα'}
    antikeimena = [] #still not defined. Farma help. i need a good translation too.
    table = 'litigations'

    def __init__(self, hearing_day, principal):
        """Initialize a Litigation object.
        
        """
        
        self.hearing_day = hearing_day
        self.owned_by = principal
        self.litigation_id = None
        
    # def define_type(self, kind):
    #     """ Define type of litigation.
        
    #     Αν εχω καταλάβει καλά δεν είναι κάτι απαραίτητο και 
    #     γι αυτό δεν ορίζεται στην __init__
    #     """

    #     self.kind = self.kinds[kind]

    # def define_antikeimeno(self, object):
    #     """ Define antikeimeno of litigation.
    
    #     Βλέπε παραπάνω, μας λείπουν πληροφορίες.
    #     """
    #     pass

    def commit_to_db(self):
        """ Commit litigation to database.

        """
        
        values = (self.hearing_day, self.owned_by.principal_id)
        if self.litigation_id:
            raise ValueError('This litigation has already been commited')
        else:
            dbm = database.DatabaseManager()
            cursor =  dbm.insert(self.table, values)
        
            self.litigation_id = cursor.lastrowid
            #close connection to database
            del(dbm)


class Procedure:
    """ Procedure class.

    Διαδικασία. Η πιο άμεσα χρήσιμη κλάση.
    Βάσει αυτής υπολογίζονται οι προθεσμίες(deadlines) που πρέπει να παρακολουθεί 
    ο χειριστής. Ορίζεται ο τύπος(kind) διαδικασίας και η διαφορά(litigation) 
    απο την οποία προκύπτει.
    """
    # προσωρινή(προφανως) προσομοίωση των τύπων διαδικασίας
    # ο τροπος υλοποιησης και η ονομασια πρεπει να διευκρινιστεί.
    # μαζι με άλλα 200 πράγματα
    kinds = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    table = 'procedures'

    def __init__(self, kind, litigation):
        """ Initialize a procedure object.
        
        """
        
        self.kind = kind
        self.procedure_of = litigation
        self.procedure_id = None

    # def define_deadlines(self):
    #     """Define deadlines for this procedure.
        
    #     Προσδιορίζει τις προθεσμίες της συγκεκριμένης διαδικασίας
    #     βάσει της δικασίμου της διαφοράς απο την οποία προκύπτει
    #     (ουτε εγω δε καταλαβα τπτ)
    #     Προς το παρόν γίνεται χειροκίνητα μιας και δεν έχουμε 
    #     συζητήσει πως θα γίνει η αυτοματοποίηση.
    #     Σαν υποθέση εργασίας ορίζουμε 2 τυχαία date objects.
    #     """
        
    #     self.deadlines.append(Deadline(date(2013, 6, 12), self))
    #     self.deadlines.append(Deadline(date(2013, 8, 15), self))

    # def set_deadline(self, deadline):
    #     """Manually set a deadline for this procedure.

    #     Χειροκίνητος ορισμός μιας προθεσμίας. 
    #     Δέχεται ως argument ένα date object.
    #     """
        
    #     self.deadlines.append(deadline, self)
    
    def commit_to_db(self):
        """ Commit to database.

        """
        
        values = (self.kind, self.procedure_of.litigation_id)
        if self.procedure_id:
            raise ValueError('This procedure has already been commited')
        else:
            dbm = database.DatabaseManager()
            cursor =  dbm.insert(self.table, values)
        
            self.procedure_id = cursor.lastrowid
            #close connection to database
            del(dbm)

    
class Application:
    """ Application class.
    
    Δικόγραφο, άγνωστο προς το παρόν το αν είναι απαραίτητο.
   
    """

    pass
