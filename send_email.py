"""
https://www.twilio.com/blog/how-to-send-recurring-emails-in-python-with-sendgrid

"""

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

api = os.environ.get('SENDGRID_API')    
print("api : ", api)

def send_email(from_email, to_email, subject, html_content):
    message = Mail(
        from_email=from_email,
        to_emails= to_email,
        subject=subject,
        html_content=html_content)
    
    

    sg = SendGridAPIClient(api)

    response = sg.send(message)


    print(response.status_code, response.body, response.headers)


if __name__=='__main__':

    send_email('egswhwang@gmail.com', 'egswhwang@gmail.com', 'test', 'test')