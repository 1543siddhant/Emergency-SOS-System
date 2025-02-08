import streamlit as st
import smtplib

# Streamlit UI
st.title("🚨 Emergency Email Sender")

# Default sender credentials
SENDER_EMAIL = "tensortitans2612@gmail.com"
SENDER_PASSWORD = "hjcy lblh gwhv jmzk"

# Default receiver emails
DEFAULT_RECEIVERS = [
    "siddhantpatil1543@gmail.com",
    "siddhantpatil1540@gmail.com"
]

# Default email subject & message
DEFAULT_SUBJECT = "I am in an Emergency. I need urgent help"
DEFAULT_MESSAGE = "I need urgent help. I am in an emergency situation !!!!!"

# Receiver emails input (allows editing)
receiver_emails = st.text_area("📥 Receiver Emails (comma-separated)", ", ".join(DEFAULT_RECEIVERS))

# Subject (not editable, since it's fixed)
st.text_input("📌 Subject", DEFAULT_SUBJECT, disabled=True)

# Message (editable)
message = st.text_area("📝 Message", DEFAULT_MESSAGE)

# Send email button
if st.button("🚀 Send Emergency Email"):
    if receiver_emails and message:
        email_list = [email.strip() for email in receiver_emails.split(",")]  # Convert input to list
        text = f"Subject: {DEFAULT_SUBJECT}\n\n{message}"  # Email format
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, email_list, text)
            server.quit()
            
            st.success(f"✅ Emergency Email sent successfully to: {', '.join(email_list)}")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
    else:
        st.warning("⚠️ Please ensure all fields are filled before sending.")

