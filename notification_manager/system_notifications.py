from notification_manager.notification import Notification


class SystemNotification():
    def __init__(self):
        self.notifications = []
    
    def send_notification(self,user_id ,message):
        
        notification = Notification(user_id,message)
        self.notifications.append(notification)

    def view_notification(self , user_id, message):
        
        for n in self.notifications:
            if n.user_id == user_id and n.message == message:
                return n

    def list_all_notifictions(self, user_id):
        return[n for n in self.notifications if n.user_id == user_id]
    

    def mark_notifiction_as_read(self, user_id, message):
         notification = self.view_notification(user_id,message)
         notification.mark_as_read()
         return notification
    
    def show_number_of_unread_notifications(self):
        return Notification.Notification.number_of_notifictions
    




        
