import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv
import bcrypt
import datetime

# ----------------------------
# Load environment variables
# ----------------------------
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="MediPal Dashboard", layout="wide")

# ----------------------------
# Load CSS
# ----------------------------
def local_css(file_name):
    css_path = os.path.join(os.path.dirname(__file__), file_name)
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {css_path}")

local_css("static/css/style.css")

# ----------------------------
# Session State
# ----------------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None

# ----------------------------
# Helper Functions
# ----------------------------
def signup_user(name, email, password):
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    supabase.table("users").insert({
        "name": name,
        "email": email,
        "password": hashed_pw
    }).execute()
    st.success("✅ Account created successfully! Please login.")

def login_user(email, password):
    user = supabase.table("users").select("*").eq("email", email).execute().data
    if user:
        hashed_pw = user[0]['password']
        if bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8')):
            st.session_state.logged_in = True
            st.session_state.user = user[0]
            st.success(f"Welcome {user[0]['name']}!")
        else:
            st.error("❌ Incorrect password")
    else:
        st.error("❌ User not found")

# ----------------------------
# Notification Bell
# ----------------------------
def show_notifications_icon():
    st.markdown("""
        <style>
        .notification-bell {
            position: fixed;
            top: 20px;
            right: 30px;
            font-size: 28px;
            cursor: pointer;
            z-index: 1000;
        }
        .notification-count {
            position: absolute;
            top: -8px;
            right: -8px;
            background: red;
            color: white;
            border-radius: 50%;
            padding: 2px 6px;
            font-size: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    notifications = supabase.table("notifications").select("*").execute().data
    pending_count = len([n for n in notifications if n['delivery_status'] == "Pending"]) if notifications else 0

    st.markdown(f"""
        <div class="notification-bell" onclick="window.location.href='#notifications'">
            🔔
            <span class="notification-count">{pending_count}</span>
        </div>
    """, unsafe_allow_html=True)

# ----------------------------
# Login / Signup UI
# ----------------------------
if not st.session_state.logged_in:
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.image(os.path.join(os.path.dirname(__file__), "static", "images", "logo.png"), width=120)
    st.markdown("<h2>🔐 Welcome to MediPal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#555;'>Login or create an account to manage your medical reminders.</p>", unsafe_allow_html=True)

    choice = st.radio("Select Option", ["Login", "Sign Up"], horizontal=True)
    
    if choice == "Sign Up":
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email")
        password = st.text_input("🔑 Password", type="password")
        if st.button("Create Account"):
            signup_user(name, email, password)
    
    if choice == "Login":
        email = st.text_input("📧 Email", key="login_email")
        password = st.text_input("🔑 Password", type="password", key="login_password")
        if st.button("Login"):
            login_user(email, password)

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Dashboard
# ----------------------------
if st.session_state.logged_in:
    show_notifications_icon()  # Top-right bell

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["👤 Patients", "🧑‍⚕️ Caregivers", "💊 Medicines", "📋 Prescriptions", "⏰ Reminders"]
    )

    # Patients Tab
    with tab1:
        st.subheader("Patients")
        patients = supabase.table("patients").select("*").execute().data
        st.dataframe(patients if patients else [])
        with st.form("add_patient_form"):
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            contact = st.text_input("Contact")
            email = st.text_input("Email")
            address = st.text_area("Address")
            submitted = st.form_submit_button("Add Patient")
            if submitted:
                supabase.table("patients").insert({
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "contact": contact,
                    "email": email,
                    "address": address
                }).execute()
                st.success(f"Patient {name} added!")

    # Caregivers Tab
    with tab2:
        st.subheader("Caregivers")
        caregivers = supabase.table("caregivers").select("*").execute().data
        st.dataframe(caregivers if caregivers else [])
        with st.form("add_caregiver_form"):
            name = st.text_input("Name", key="cg_name")
            contact = st.text_input("Contact", key="cg_contact")
            email = st.text_input("Email", key="cg_email")
            relationship = st.text_input("Relationship", key="cg_relation")
            assigned_patient_id = st.number_input("Assigned Patient ID", min_value=0, key="cg_patient")
            submitted = st.form_submit_button("Add Caregiver")
            if submitted:
                supabase.table("caregivers").insert({
                    "name": name,
                    "contact": contact,
                    "email": email,
                    "relationship": relationship,
                    "assigned_patient_id": assigned_patient_id
                }).execute()
                st.success(f"Caregiver {name} added!")

    # Medicines Tab
    with tab3:
        st.subheader("Medicines")
        medicines = supabase.table("medicines").select("*").execute().data
        st.dataframe(medicines if medicines else [])
        with st.form("add_medicine_form"):
            name = st.text_input("Medicine Name", key="med_name")
            dosage = st.text_input("Dosage", key="med_dosage")
            frequency = st.text_input("Frequency", key="med_freq")
            description = st.text_area("Description", key="med_desc")
            submitted = st.form_submit_button("Add Medicine")
            if submitted:
                supabase.table("medicines").insert({
                    "name": name,
                    "dosage": dosage,
                    "frequency": frequency,
                    "description": description
                }).execute()
                st.success(f"Medicine {name} added!")

    # Prescriptions Tab
    with tab4:
        st.subheader("Prescriptions")
        prescriptions = supabase.table("prescriptions").select("*").execute().data
        st.dataframe(prescriptions if prescriptions else [])
        with st.form("add_prescription_form"):
            patient_id = st.number_input("Patient ID", min_value=0, key="pres_patient")
            medicine_id = st.number_input("Medicine ID", min_value=0, key="pres_med")
            start_date = st.date_input("Start Date", key="pres_start")
            end_date = st.date_input("End Date", key="pres_end")
            instructions = st.text_area("Instructions", key="pres_instr")
            submitted = st.form_submit_button("Add Prescription")
            if submitted:
                supabase.table("prescriptions").insert({
                    "patient_id": patient_id,
                    "medicine_id": medicine_id,
                    "start_date": start_date.isoformat(),
                    "end_date": end_date.isoformat(),
                    "instructions": instructions
                }).execute()
                st.success(f"Prescription added for Patient ID {patient_id}!")

    # Reminders Tab
    with tab5:
        st.subheader("Reminders")
        reminders = supabase.table("reminders").select("*").execute().data
        st.dataframe(reminders if reminders else [])
        with st.form("add_reminder_form"):
            prescription_id = st.number_input("Prescription ID", min_value=0, key="rem_pres")
            reminder_time = st.time_input("Reminder Time", key="rem_time")
            submitted = st.form_submit_button("Add Reminder")
            if submitted:
                supabase.table("reminders").insert({
                    "prescription_id": prescription_id,
                    "reminder_time": reminder_time.strftime("%H:%M:%S"),
                    "status": "Pending"
                }).execute()
                st.success(f"Reminder added for Prescription ID {prescription_id}!")

        # Display notifications in expander
        with st.expander("🔔 Notifications", expanded=False):
            notifications = supabase.table("notifications").select("*").execute().data
            if notifications:
                for n in notifications[::-1]:
                    status = n['delivery_status']
                    st.write(f"📌 {n['message']} - {status} at {n['sent_time']}")
            else:
                st.write("No notifications yet.")

    # Logout
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.experimental_rerun()
