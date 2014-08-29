from flask import Flask
from flask.ext.mail import Mail, Message
from app import app

app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'surajkap@gmail.com',
    MAIL_PASSWORD = 'wilshere10',
    )

mail = Mail(app)