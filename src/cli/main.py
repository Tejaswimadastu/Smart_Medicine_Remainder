from services.patient_service import PatientService
from services.caregiver_service import CaregiverService
from services.medicine_service import MedicineService
from services.prescription_service import PrescriptionService
from services.reminder_service import ReminderService
from services.notification_service import NotificationService
from . import scheduler 
def main():
    patient_service=PatientService()
    caregiver_service=CaregiverService()
    medicine_service=MedicineService()
    prescription_service=PrescriptionService()
    reminder_service=ReminderService()
    notification_service=NotificationService()
    while True:
        print("\n--- Smart Medicine Remainder ---")
        print("1.Add Patient")
        print("2.view Patients")
        print("3.Add Caregiver")
        print("4.View Caregivers")
        print("5. Add Medicine")
        print("6.View Medicine")
        print("7.Add Prescription")
        print("8.View Prescription")
        print("9.Add Reminder")
        print("10.View Reminders")
        print("11. View Notifications")
        print("12.Exit")
        ch=input("Enter choice: ")
        if ch=="1":
            name=input("Name: ")
            age=int(input("Age: "))
            gender=input("Gender: ")
            contact = input("Contact: ")
            email = input("Email: ")
            address = input("Address: ")
            patient = patient_service.register_patient(name, age, gender, contact, email, address)
            print("Patient added:", patient)
        elif ch=="2":
            patients = patient_service.list_patients()
            for p in patients:
                print(p)
        elif ch=="3":
            name = input("Name: ")
            contact = input("Contact: ")
            email = input("Email: ")
            relationship = input("Relationship: ")
            assigned_patient_id = int(input("Assigned Patient ID: "))
            caregiver = caregiver_service.register_caregiver(name, contact, email, relationship, assigned_patient_id)
            print("Caregiver added:", caregiver)
        elif ch == "4":
            caregivers = caregiver_service.list_caregivers()
            for c in caregivers:
                print(c)
        elif ch== "5":
            name = input("Medicine Name: ")
            dosage = input("Dosage: ")
            frequency = input("Frequency: ")
            description = input("Description: ")
            medicine = medicine_service.add_medicine(name, dosage, frequency, description)
            print("Medicine added:", medicine)

        elif ch== "6":
            medicines = medicine_service.list_medicines()
            for m in medicines:
                print(m)

        elif ch== "7":
            patient_id = int(input("Patient ID: "))
            medicine_id = int(input("Medicine ID: "))
            start_date = input("Start Date (YYYY-MM-DD): ")
            end_date = input("End Date (YYYY-MM-DD): ")
            instructions = input("Instructions: ")
            prescription = prescription_service.add_prescription(patient_id, medicine_id, start_date, end_date, instructions)
            print("Prescription added:", prescription)

        elif ch== "8":
            prescriptions = prescription_service.list_prescriptions()
            for p in prescriptions:
                print(p)

        elif ch== "9":
            prescription_id = int(input("Prescription ID: "))
            reminder_time = input("Reminder Time (HH:MM:SS): ")
            reminder = reminder_service.add_reminder(prescription_id, reminder_time)
            print("Reminder added:", reminder)

        elif ch== "10":
            reminders = reminder_service.list_reminders()
            for r in reminders:
                print(r)

        elif ch== "11":
            notifications = notification_service.list_notifications()
            for n in notifications:
                print(n)

        elif ch== "12":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()