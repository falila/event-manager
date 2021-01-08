from threading import Thread
from flask_mail import Message

def send_async_email(app, msg):
    from app import app , mail
    from resources.errors import InternalServerError
    with app.app_context():
        try:
            mail.send(msg)
        except ConnectionRefusedError:
            raise InternalServerError



def send_mail(subject, sender, recipients, text_body, html_body):
    from app import app, mail
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()