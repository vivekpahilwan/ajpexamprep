import smtplib

# Set up the sender's email address and password
sender_email = 'your_email@example.com'
sender_password = 'your_email_password'

# Set up the recipient's email address
recipient_email = 'recipient_email@example.com'

# Set up the message content
subject = 'Test Email'
body = 'This is a test email sent from Python.'

# Set up the email headers
headers = f'To: {recipient_email}\nFrom: {sender_email}\nSubject: {subject}\n'

# Combine the headers and body into a single message
message = headers + '\n' + body

# Connect to the SMTP server and log in to the sender's email account
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# Send the email
server.sendmail(sender_email, recipient_email, message)

# Disconnect from the SMTP server
server.quit()

print('Email sent successfully!')
