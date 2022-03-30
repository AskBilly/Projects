
import smtplib
import os
from email.message import EmailMessage



# Step 1  ~  Getting email and password from environment variable
EMAIL_ADDRESS = os.environ.get('MY_GMAIL')
EMAIL_PASSWORD = os.environ.get('MY_GMAIL_PASS')



#Step 2  ~  Initializing Email Instance
msg = EmailMessage()
msg['Subject'] = 'Email Tester with Attachment'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'reciever@gmail.com'
msg.set_content('We found this file for your query')



# Step 3  ~  Finding a file
query = input('Filename: ')
path = 'desire search path'

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.split('.')[0].lower() == query.lower():
            file_path = os.path.join(dirpath, filename)
            file_ext = os.path.splitext(file_path)[1]

            if file_ext == '.pdf':
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = filename
                
                # Step 4  ~  Adding file as an attachment to the Email instane
                msg.add_attachment(file_data, maintype='application',
                            subtype='octet-stream', filename=file_name)

            elif file_ext == '.txt':
                with open(file_path, 'r') as f:
                    file_data = f.read()
                    file_name = filename
                    
                msg.add_attachment(file_data, filename=file_name)



# Step 5  ~  Sending Email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
