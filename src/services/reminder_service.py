from dao.reminder_dao import ReminderDAO

class ReminderService:
    def __init__(self):
        self.reminder_dao = ReminderDAO()

    def add_reminder(self, prescription_id, reminder_time, status="Pending"):
        return self.reminder_dao.add_reminder(prescription_id, reminder_time, status)

    def list_reminders(self):
        return self.reminder_dao.get_all_reminders()

    def get_pending_reminders(self):
        return self.reminder_dao.get_pending_reminders()

    # Added to match scheduler.py usage
    def update_reminder_status(self, reminder_id, status):
        return self.reminder_dao.update_status(reminder_id, status)
