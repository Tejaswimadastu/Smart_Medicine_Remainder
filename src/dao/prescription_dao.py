from config import supabase
class PrescriptionDAO:
     def add_prescription(self, patient_id, medicine_id, start_date, end_date, instructions):
          response=supabase.table("prescriptions").insert({
               "patient_id":patient_id,
               "medicine_id": medicine_id,
               "start_date":start_date,
               "end_date":end_date,
               "instructions":instructions

          }).execute()
          return response.data
     def get_all_prescriptions(self):
          response=supabase.table("prescriptions").select("*").execute()
          return response.data