import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="MediPal Dashboard", layout="wide")

st.title("💊 MediPal Dashboard")
st.write("Monitor patients, caregivers, medicines, prescriptions, reminders, and notifications.")

# Tabs for different tables
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["👤 Patients", "🧑‍⚕️ Caregivers", "💊 Medicines", "📋 Prescriptions", "⏰ Reminders", "🔔 Notifications"]
)

with tab1:
    st.subheader("Patients")
    patients = supabase.table("patients").select("*").execute().data
    if patients:
        st.dataframe(patients)
    else:
        st.info("No patients found.")

with tab2:
    st.subheader("Caregivers")
    caregivers = supabase.table("caregivers").select("*").execute().data
    if caregivers:
        st.dataframe(caregivers)
    else:
        st.info("No caregivers found.")

with tab3:
    st.subheader("Medicines")
    medicines = supabase.table("medicines").select("*").execute().data
    if medicines:
        st.dataframe(medicines)
    else:
        st.info("No medicines found.")

with tab4:
    st.subheader("Prescriptions")
    prescriptions = supabase.table("prescriptions").select("*").execute().data
    if prescriptions:
        st.dataframe(prescriptions)
    else:
        st.info("No prescriptions found.")

with tab5:
    st.subheader("Reminders")
    reminders = supabase.table("reminders").select("*").execute().data
    if reminders:
        st.dataframe(reminders)
    else:
        st.info("No reminders found.")

with tab6:
    st.subheader("Notifications")
    notifications = supabase.table("notifications").select("*").execute().data
    if notifications:
        st.dataframe(notifications)
    else:
        st.info("No notifications found.")
