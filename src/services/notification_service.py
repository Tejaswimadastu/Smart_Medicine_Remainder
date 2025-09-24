from dao.notification_dao import NotificationDAO
from datetime import datetime

class NotificationService:
    def __init__(self):
        self.notification_dao = NotificationDAO()

    def send_notification(self, reminder_id, message):
        sent_time = datetime.now().isoformat()
        delivery_status = "Sent"
        return self.notification_dao.add_notification(reminder_id, sent_time, delivery_status, message)

    def list_notifications(self):
        return self.notification_dao.get_all_notifications()
