import smtplib
from email.mime.text import MIMEText

def send_simple_email(sender_email, receiver_email, password, subject, body, smtp_server, smtp_port):
    """Sends a simple email """
    try:
        #create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        #connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server: 
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check your email/password or app-specific password settings.")
        print("For Gmail, you might need to enable 'Less secure app access' or generate an 'App Password'.")
    except smtplib.SMTPServerDisconnected:
        print("SMTP Server Disconnected: The server unexpectedly disconnected.")
    except smtplib.SMTPConnectError:
        print(f"SMTP Connect Error: Failed to connect to the server at {smtp_server}:{smtp_port}.")
    except Exception as e:
        print(f"An error occurred: {e}")


#--- Configuration ---
SENDER_EMAIL = "adstech@gmail.com"
RECEIVER_EMAIL = "darrylhiiz8@gmail.com"
SENDER_PASSWORD = "Adstech@2025!"

EMAIL_SUBJECT = "Test Email from Python Script"
EMAIL_BODY = "Hello,\n\nThis is a test email sent from a Python script.\n\nBest regards,\nPython Script"

SMTP_SERVER_HOST = "smtp.gmail.com"
SMTP_SERVER_PORT = 465

#--- Main Execution ---
if __name__ == "__main__":
    if SENDER_EMAIL == "your_email@gmail.com" or SENDER_PASSWORD == "you_email_password":
        print("Please update SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER_HOST, and SMTP_SERVER_PORT variables in the script.")
    else:
        send_simple_email(
            SENDER_EMAIL, 
            RECEIVER_EMAIL, 
            SENDER_PASSWORD, 
            EMAIL_SUBJECT, 
            EMAIL_BODY, 
            SMTP_SERVER_HOST, 
            SMTP_SERVER_PORT
            )

#--- End ---     