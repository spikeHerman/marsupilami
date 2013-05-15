
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
    margins = [first_notif, second_notif, third_notif, fourth_notif, last_notif]

    # Notification message.
    notification = 'Απομένουν {} μέρες μέχρι την προθεσμία.'
            

    def __init__(self, date, belongs_to = None, expired = False):
        """Initialzing a Deadline.
        
        Σχολια σε λιγο.
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

    def notify(self):
        """Check if it's time for notification, if so return approporiate string.

        """
        
        # goes through margins to check if remaining days equals any margin.
        for margin in self.margins:
            # if so, returns the appropriate message, using notification
            if self.remaning_days().days == margin:
                return self.notification.format(margin)
        # if no margin matches, return None
        return None

        
        

    
        
        
