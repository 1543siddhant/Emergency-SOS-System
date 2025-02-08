import streamlit as st
import smtplib
import os
from email.message import EmailMessage

# Streamlit UI
st.title("🚨 Emergency Email System with Image Attachment")

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

# File uploader for image attachment
uploaded_file = st.file_uploader("📷 Upload an image (optional)", type=["png", "jpg", "jpeg"])

# Send email button
if st.button("🚀 Send Emergency Email"):
    if receiver_emails and message:
        email_list = [email.strip() for email in receiver_emails.split(",")]  # Convert input to list
        
        # Create the email
        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(email_list)
        msg["Subject"] = DEFAULT_SUBJECT
        msg.set_content(message)

        # Attach the uploaded image (if any)
        if uploaded_file is not None:
            file_data = uploaded_file.read()
            file_name = uploaded_file.name
            msg.add_attachment(file_data, maintype="image", subtype=file_name.split(".")[-1], filename=file_name)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            server.quit()
            
            st.success(f"✅ Emergency Email sent successfully to: {', '.join(email_list)}")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
    else:
        st.warning("⚠️ Please ensure all fields are filled before sending.")
