from dao.prescription_dao import PrescriptionDAO

class PrescriptionService:
    def __init__(self):
        self.prescription_dao = PrescriptionDAO()

    def add_prescription(self, patient_id, medicine_id, start_date, end_date, instructions):
        return self.prescription_dao.add_prescription(patient_id, medicine_id, start_date, end_date, instructions)

    def list_prescriptions(self):
        return self.prescription_dao.get_all_prescriptions()
