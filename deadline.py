from datetime import date
import database

class Deadline:
    """Deadline

    Η κλάση deadline. θα πω περισσοτερα
    
    """
    # How many days before deadline you get a notification.
    first_notif  = 30
    second_notif = 15
    third_notif  = 10
    fourth_notif = 5
    last_notif   = 3
    margins      = [first_notif, second_notif, third_notif, fourth_notif, last_notif]

    # Notification message.
    notification = 'Απομένουν {} μέρες μέχρι την προθεσμία.'
    
    # Database name
    db_name = 'testing2.db'

    # Corresponding table in database.
    table = 'deadlines'

    def __init__(self, date_of, deadline_of = None, expired = False):
        """Initialzing a Deadline.
        
        Η date_of ειναι date object του datetime module.
        """
        
        self.date_of     = date_of
        self.deadline_of = deadline_of
        self.expired     = expired
        self.deadline_id = None

    def remaining_days(self):
        """How many days remain to end of deadline
        
        Επιστρέφει ένα timedelta object που αναφέρει την χρονική απόσταση
        (σε μέρες) απο την deadline.
        """
        
        today = date.today()
        diff  = self.date_of - today
        if diff.days > 0:
            return diff
        else:
            raise ValueError('Deadline has passed')

    def notify(self):
        """Check if it's time for notification, if so return approporiate string.
           
        Προχειροφτιαγμένη μέθοδος που ειδοποιεί χ μέρες πριν απο την προθεσμία.
        (οπου χ οι τιμες της λιστας margins). Αν δεν ειμαστε χ μερες πριν επιστρέφει
        None.
        """
        
        # goes through margins to check if remaining days equals any margin.
        for margin in self.margins:
            # if so, returns the appropriate message, using notification
            if self.remaning_days().days == margin:
                return self.notification.format(margin)
        # if no margin matches, return None
        return None
    
    def commit_to_db(self):
        """Commit the deadline to database.
        
        """
        values = (str(self.date_of), str(self.expired), self.deadline_of.procedure_id)
        if self.deadline_id:
            raise ValueError('This deadline has already been commited')
        else:
            dbm = database.DatabaseManager()
            cursor = dbm.insert(self.table, values)

            self.deadline_id = cursor.lastrowid
            #close connection to database
            del(dbm)
        

    
        
        
