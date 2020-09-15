import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def save_profile(form_profile):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_profile.filename)
    profile_fn = random_hex + f_ext
    profile_path = os.path.join(
        current_app.root_path, 'static/profile_img', profile_fn)
    output_size = (125, 125)
    i = Image.open(form_profile)
    i.thumbnail(output_size)
    i.save(profile_path)
    return profile_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)    