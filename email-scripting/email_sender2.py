#Sending Customized Emails using html body
#using string template we can substitute variables using ' $ ' symbol.
#pathlib is similar to os module, allows us to access the html file

import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage

#Html file-path object
html = Template(Path('index.html').read_text())

# The Email Syntax
email = EmailMessage()
email['from'] = '********@yahoo.com'
email['to'] = 'ricenek964@laymro.com' #Dummy Email
email['subject'] = 'You won a Million Dollars!'

#Substituting Variables in Html File with String Template
email.set_content(html.substitute({'name' : 'Sam'}), 'html')

#Log in to the client and send it

with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as smtp:
    smtp.ehlo() #hello the starting msg
    #smtp.starttls() #encryption mechanism, connecting to email
    smtp.login('********@yahoo.com','********')#email and pass token
    smtp.send_message(email)
    print('Email Sent Successfully!')
