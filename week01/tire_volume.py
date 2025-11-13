from datetime import date, datetime

try:
    import config
except Exception:
    class _Cfg:
        pass
    config = _Cfg()

# send email with file attached
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket

def prompt_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

tire_width = prompt_int("Enter the tire width in mm (e.g., 205): ")

aspect_ratio = prompt_int("Enter the aspect ratio (e.g., 60): ")

wheel_diameter = prompt_int("Enter the wheel diameter in inches (e.g., 15): ")

volume = (3.14159 * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + (2540 * wheel_diameter))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")

with open("volumes.txt", "a") as file:
    file.write(f"{date.today()},{tire_width},{aspect_ratio},{wheel_diameter},{volume:.2f}\n")

print(f"Data saved to volumes.txt on {datetime.now():%Y-%m-%d %H:%M:%S}.")

email = input("Please enter your email address to receive the file directly: ").strip()
if not email:
    print("No email provided; skipping email send.")
else:
    smtp_host = getattr(config, 'smtp_server', None) or 'smtp.office365.com'
    smtp_port = getattr(config, 'smtp_port', None) or 587

    username = getattr(config, 'username', None)
    password = getattr(config, 'password', None)

    if not username or not password:
        print("Email credentials not found in config; skipping email send.")
    else:
        try:
            socket.gethostbyname(smtp_host)
        except socket.gaierror:
            print(f"SMTP host '{smtp_host}' could not be resolved; skipping email send.")
        else:
            try:
                msg = MIMEMultipart()
                msg['From'] = username
                msg['To'] = email
                msg['Subject'] = 'Tire Volume Data'

                body = 'Find the attached tire volume data here.'
                msg.attach(MIMEText(body, 'plain'))

                with open("volumes.txt", "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename=volumes.txt')
                    msg.attach(part)

                with smtplib.SMTP(smtp_host, smtp_port, timeout=10) as server:
                    server.starttls()
                    server.login(username, password)
                    server.send_message(msg)

                print(f"Email sent to {email}.")

            except Exception as e:
                print(f"Error sending email: {e}")