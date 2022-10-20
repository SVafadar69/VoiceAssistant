from mysay import print_say
from mysr import voice_to_text
import ssl
import smtplib
from email.message import EmailMessage

email_list = {"steven": "svafadar19@gmail.com", "steven": "svafadar17@gmail.com"}

def email_setup():

    email_message, email_subject, email_recipient, destination_email = send_email()

    email = "svafadar19@gmail.com"
    password = "Svafadar20?"
    body = email_message
    em = EmailMessage()
    em['From'] = email
    em['To'] = email_list[email_recipient]
    em['Subject'] = email_subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, destination_email, em.as_string())  # send email


def send_email():

    print_say("What do you want to say?")
    inp = voice_to_text().lower()

    while True:
        if "email" in inp:
            print_say("What do you want to send?")
            email_message = voice_to_text().lower()
            print_say(f"You said {email_message}")

            print_say("What is the subject of the email?")
            email_subject = voice_to_text().lower()
            print_say(f"You said {email_subject}")

            print_say("Who do you want to send it to?")
            email_recipient = voice_to_text().lower()
            print_say(f"You said {email_recipient}")

            print_say("Is there anyone else you want to send this email to")
            additional_people = voice_to_text().lower()

            if "yes" in additional_people:
                print_say("What is their name? What is their email?")
                additional_people = voice_to_text().lower()

            print_say("Is there anything else you want to say")
            confirmation = voice_to_text().lower()

            if confirmation == "no":
                break

            email, password, destination_email = email_setup()

send_email()
# import smtplib
#
# # Build a dictionary of names and emails
# emails = {'mark': 'mark.liu@uky.edu',
#           'sarah': 'Sarah email address here',
#           'chris': 'Chris email address here'}
# # Different email providers have different domain name and port number
# mysmt = smtplib.SMTP('smtp.gmail.com', 587)
# mysmt.ehlo()
# mysmt.starttls()
# # Use your own login info; you may need an app password
# mysmt.login('{your email here}', '{your password here}')
# # Ask for the name of of the recipeint
# name = input('Who do you want to send the email to?\n')
# email = emails[name]
# print(f"You just said {name}.")
# # Ask for the subject line
# subline = input('What is the subject line?\n')
# print(f"You just said {subline}.")
# # Ask for the email content
# content = input('What is the email content?\n')
# print(f"You just said {content}.")
# # Send the actual email
# mysmt.sendmail('ukmarkliu@gmail.com', email,
#                f'Subject: {subline}.\nHello, {content}.')
# {}
# print('Ok, email sent')
# mysmt.quit()
