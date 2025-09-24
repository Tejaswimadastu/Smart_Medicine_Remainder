from config import supabase 

class ReminderDAO:
    def add_reminder(self, prescription_id, reminder_time, status="Pending"):
        response = supabase.table("reminders").insert({
            "prescription_id": prescription_id,
            "reminder_time": reminder_time,
            "status": status
        }).execute()
        return response.data

    def get_all_reminders(self):
        response = supabase.table("reminders").select("*").execute()
        return response.data

    def get_pending_reminders(self):
        response = supabase.table("reminders").select("*").eq("status", "Pending").execute()
        return response.data

    def update_status(self, reminder_id, status):
        response = supabase.table("reminders").update({"status": status}).eq("reminder_id", reminder_id).execute()
        return response.data
