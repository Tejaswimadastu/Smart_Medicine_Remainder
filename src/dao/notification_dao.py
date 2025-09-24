from config import supabase
class NotificationDAO:
    def add_notification(self, reminder_id, sent_time, delivery_status, message):
        response = supabase.table("notifications").insert({
            "reminder_id": reminder_id,
            "sent_time": sent_time,
            "delivery_status": delivery_status,
            "message": message
        }).execute()
        return response.data

    def get_all_notifications(self):
        response = supabase.table("notifications").select("*").execute()
        return response.data
