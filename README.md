# Smart_Medicine_Remainder
MediPal 💊 – Smart Medicine Reminder
Project Overview

MediPal is a Python-based CLI application designed to help patients and caregivers manage medication schedules efficiently. It allows storing patient information, caregivers, medicines, prescriptions, and reminders, while sending timely notifications for each scheduled dose.

Motivation

Many patients, especially those taking multiple medicines, struggle to remember doses at the correct time. MediPal automates reminders and ensures timely intake of medications, reducing errors and improving healthcare management.

Key Features

Add and view Patients and Caregivers

Store Medicines with dosage, expiry date, and intake times

Create Prescriptions linking patients and medicines

Schedule Reminders automatically based on intake times

Automatic Notifications for pending reminders

CLI-based interface for easy operation

Technology Stack

Python 3.11+

Supabase as backend database

APScheduler for scheduled notifications

Python-dotenv for environment variable management

Installation & Setup

Clone the repository:

git clone (https://github.com/Tejaswimadastu/Smart_Medicine_Remainder.git)
cd MediPal


Create virtual environment (recommended):

python -m venv venv
source venv/Scripts/activate  # Windows


Install dependencies:

pip install -r requirements.txt


Create a .env file with Supabase credentials:

SUPABASE_URL="https://euvockiojukfyzirwkyg.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV1dm9ja2lvanVrZnl6aXJ3a3lnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg2MDczODYsImV4cCI6MjA3NDE4MzM4Nn0.XabyYaiCCvnH5Iv8Kffhw6mn1JnMO3ZhJ5c5CrtxO_4"


Ensure Supabase tables exist:

patients, caregivers, medicines, prescriptions, reminders, notifications

Use lowercase table names to avoid API errors.

Project Structure
MediPal/
│
├── .env
├── requirements.txt
├── README.md
└── src/
    ├── cli/
    │   ├── main.py
    │   └── scheduler.py
    ├── dao/
    │   ├── patient_dao.py
    │   ├── caregiver_dao.py
    │   └── ...
    └── services/
        ├── patient_service.py
        ├── caregiver_service.py
        └── ...

Usage

Run the application from src/ folder:

cd src
python -m cli.main


Menu Options:

1. Add Patient
2. View Patients
3. Add Caregiver
4. View Caregivers
5. Add Medicine
6. View Medicine
7. Add Prescription
8. View Prescription
9. Add Reminder
10. View Reminders
11. View Notifications
12. Exit


Workflow Example:

Add Patient → Add Caregiver → Add Medicine → Add Prescription → Add Reminders

Scheduler runs automatically and sends notifications for pending reminders.

Database Design

Patients: patient_id, name, age, gender, contact, email, address

Caregivers: caregiver_id, name, contact, email, relationship, assigned_patient_id

Medicines: medicine_id, name, dosage, expiry_date, intake_times, description

Prescriptions: prescription_id, patient_id, medicine_id, start_date, end_date, instructions

Reminders: reminder_id, prescription_id, reminder_time, status

Notifications: notification_id, reminder_id, sent_time, delivery_status

Future Enhancements

GUI or Web App interface

Multi-patient and multi-store support

Real-time dashboards for medication tracking

Integration with SMS/email notifications

Contributing

Fork the repository

Create a feature branch (git checkout -b feature_name)

Commit changes (git commit -m "Add feature")

Push to branch (git push origin feature_name)

Create a Pull Request

License

This project is licensed under the MIT License.