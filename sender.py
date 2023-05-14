
#___________________________________IMPORTS_________________________
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, emailBody, to):
    # Set up the email parameters
    msg = MIMEMultipart()
    msg['From'] = "emailtesteremailtester123@gmail.com"
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(emailBody, 'plain'))

    # Log in to the Gmail SMTP server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login("emailtesteremailtester123@gmail.com", "wykxeptrluwazmvr")

    # Send the email
    text = msg.as_string()
    smtp_server.sendmail("emailtesteremailtester123@gmail.com", to, text)

    # Close the SMTP server
    smtp_server.quit()


#subject = "Green Wolrd"
#body = "This is a test email sent using Python."
#to = "beatriz.landi.coelho@gmail.com"
#send_email(subject, body, to)