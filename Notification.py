class Notification:
    number_of_notifictions = 0
    def __init__(self,user_id,message,is_unread = True):
        self.user_id = user_id
        self.message = message
        self.is_unread = is_unread
        Notification.number_of_notifictions +=1

    def mark_as_read(self):
        self.is_unread = False
        Notification.number_of_notifictions -=1

    def __str__(self):
        return f"Hello {self.user_id}, you have new notification: {self.message}"
    
