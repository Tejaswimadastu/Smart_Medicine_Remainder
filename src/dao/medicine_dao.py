from config import supabase
class MedicineDAO:
    def add_medicine(self, name, dosage, frequency, description):
        response=supabase.table("medicines").insert({
            "name":name,
            "dosage":dosage,
            "frequency":frequency,
            "description":description
        }).execute()
        return response.data
    def get_all_medicines(self):
        response = supabase.table("medicines").select("*").execute()
        return response.data
    