from dao.patient_dao import PatientDAO
class PatientService:
    def __init__(self):
        self.patient_dao=PatientDAO()
    def register_patient(self, name, age, gender, contact, email, address):
        return self.patient_dao.add_patient(name, age, gender, contact, email, address)

    def list_patients(self):
        return self.patient_dao.get_all_patients()