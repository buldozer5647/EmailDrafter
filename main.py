from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import base64

class EmailDrafter:
    """
    A class for creating gmail drafts 
    using authorized sender
    """
    def __init__(self, receiver_email: str, subject: str, email_content: str):
        # initialize the class with the necessary variables
        self.subject = subject
        self.receiver_email = receiver_email
        self.email_content = email_content
        
        # your email (sender)
        self.sender_email = "your_gmail@gmail.com"

        # add credentionals variable based on token.json (which was created by quickstart.py)
        creds = Credentials.from_authorized_user_file("token.json")
        self.service = build("gmail", "v1", credentials=creds)

    def create_message(self):
        # function for creating MIMEText message (the body for the email)
        message = MIMEText(self.email_content)
        message['to'] = self.receiver_email
        message['from'] = self.sender_email
        message['subject'] = self.subject

        raw_message = base64.urlsafe_b64encode(message.as_string().encode("utf-8"))

        return {
            'raw': raw_message.decode("utf-8")
        }

    def create_draft(self):
        # function for creating a draft using Gmail API
        try:
            message_body = self.create_message()

            message = {'message': message_body}
            draft = self.service.users().drafts().create(userId="me", body=message).execute()
            print("Successfully crated a draft!")
            return draft
        except Exception as e:
            print('Error!\n', e)
            return None
        
if __name__ == "__main__":
    # example usage
    e = EmailDrafter("receiver_mail@gmail.com", "Hello", "world")
    e.create_draft()
