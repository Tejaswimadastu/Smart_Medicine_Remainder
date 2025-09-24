from apscheduler.schedulers.background import BackgroundScheduler
from services.reminder_service import ReminderService
from services.notification_service import NotificationService
from datetime import datetime

reminder_service = ReminderService()
notification_service = NotificationService()

def check_remainders():
    pending = reminder_service.get_pending_reminders()
    now = datetime.now().strftime("%H:%M:%S")

    for r in pending:
        # ✅ Trigger notification only once if time has passed and not already sent
        if r['reminder_time'] <= now and r['status'] != 'sent':
            message = f"💊 Time to take medicine for Prescription ID {r['prescription_id']}"
            
            # ✅ Send notification
            notification_service.send_notification(r['reminder_id'], message)
            print(f"✅ Notification sent for Reminder ID {r['reminder_id']}")

            # ✅ Mark this reminder as 'sent' so it won't repeat
            reminder_service.update_reminder_status(r['reminder_id'], "sent")

scheduler = BackgroundScheduler()
scheduler.add_job(check_remainders, 'interval', seconds=60)
scheduler.start()
