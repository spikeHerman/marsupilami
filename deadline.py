from datetime import date, timedelta

class Deadline:
    """deadline

    Η κλάση deadline
    """
    
    # How many days before deadline you get a notification.
    first_notif  = 30
    second_notif = 15
    third_notif  = 10
    fourth_notif = 5
    last_notif   = 3
    days = [first_notif, second_notif, third_notif, fourth_notif, last_notif]

    # Notification message.
    notification = 'Απομένουν {} μέρες μέχρι την προθεσμία.'
            

    def __init__(self, date, belongs_to = None, expired = False):
        """Initialzing a Deadline.
        
        Σε λιγο.
        """
        
        self.date = date
        self.belongs_to = belongs_to
        self.expired = expired

    def remaining_days(self):
        """How many days remain to end of deadline
        
        Επιστρέφει ένα timedelta object που αναφέρει την χρονική απόσταση
        (σε μέρες) απο την deadline.
        """
        today = date.today()
        diff  = self.date - today
        if diff.days > 0:
            return diff
        else:
            raise ValueError('Deadline has passed')

    

    
        
        
