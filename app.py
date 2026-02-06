import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Appointment Reminder Bot", layout="centered")

st.title("📅 Appointment Reminder Bot")
st.write("Smart scheduling assistant with reminder optimization.")

st.divider()

name = st.text_input("Client / Patient Name")
purpose = st.text_input("Purpose of Appointment")

date = st.date_input("Appointment Date")
time = st.time_input("Appointment Time")

channel = st.selectbox(
    "Preferred Reminder Channel",
    ["SMS", "Email", "Push Notification"]
)

reminder_timing = st.selectbox(
    "Reminder Timing",
    ["24 hours before", "12 hours before", "1 hour before"]
)

st.divider()

def no_show_risk(timing):
    if timing == "1 hour before":
        return "Low"
    elif timing == "12 hours before":
        return "Medium"
    else:
        return "High"

if st.button("Generate Smart Reminder"):
    if not name or not purpose:
        st.warning("Please fill all required fields.")
    else:
        risk = no_show_risk(reminder_timing)

        reminder_message = f"""
Hello {name},

This is a reminder for your upcoming appointment.

 Date: {date}
 Time: {time}
 Purpose: {purpose}

 Reminder Channel: {channel}
 Reminder Timing: {reminder_timing}

No-show Risk Prediction: {risk}

Please confirm, reschedule, or cancel if needed.
Thank you!
"""

        st.success("Reminder Generated Successfully")
        st.text(reminder_message)

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button(" Confirm Appointment"):
                st.success("Appointment confirmed successfully.")

        with col2:
            if st.button(" Reschedule"):
                st.info("Rescheduling request recorded.")

        with col3:
            if st.button(" Cancel"):
                st.error("Appointment cancelled.")