from dao.caregiver_dao import CaregiverDAO
class CaregiverService:
    def __init__(self):
        self.caregiver_dao = CaregiverDAO()

    def register_caregiver(self, name, contact, email, relationship, assigned_patient_id):
        return self.caregiver_dao.add_caregiver(name, contact, email, relationship, assigned_patient_id)

    def list_caregivers(self):
        return self.caregiver_dao.get_all_caregivers()
