from config import supabase

class CaregiverDAO:
    def add_caregiver(self, name, contact, email, relationship, assigned_patient_id):
        response = supabase.table("caregivers").insert({
            "name": name,
            "contact": contact,
            "email": email,
            "relationship": relationship,
            "assigned_patient_id": assigned_patient_id
        }).execute()
        return response.data

    def get_all_caregivers(self):
        response = supabase.table("caregivers").select("*").execute()
        return response.data
