from dao.medicine_dao import MedicineDAO

class MedicineService:
    def __init__(self):
        self.medicine_dao = MedicineDAO()

    def add_medicine(self, name, dosage, frequency, description):
        return self.medicine_dao.add_medicine(name, dosage, frequency, description)

    def list_medicines(self):
        return self.medicine_dao.get_all_medicines()
