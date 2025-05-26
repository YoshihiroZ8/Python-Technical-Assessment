import smtplib
from email.mime.text import MIMEText

def sed_simple_email(send_email, receiver_email, password, subject, body, smtp_server, smtp_port):
    """Sends a simple email """
    try:
        #create the email message
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = send_email
        msg['To'] = receiver_email

        #connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server: 
            server.login(send_email, password)
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
