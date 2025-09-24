from config import supabase
class PatientDAO:
    def add_patient(self, name, age, gender, contact, email, address):
        response=supabase.table("patients").insert({
            "name":name,
            "age":age,
            "gender":gender,
            "contact":contact,
            "email":email,
            "address":address
        }).execute()
        return response.data
    def get_all_patients(self):
        response = supabase.table("patients").select("*").execute()
        return response.data
