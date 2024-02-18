# https://docs.python.org/3/library/email.examples.html

#Due to Email Authentication, Using SMTP_SSL instead of SMTP with port 465
#without using email module

""" import smtplib
from datetime import date

sender = '********@yahoo.com' 
to  = 'ricenek964@laymro.com'
subj='You won a Million Dollars!'
current_date = date.today()
message_text='I am a Python Emailing Master!'

msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( sender, to, subj, current_date, message_text ) #String formatting
  
username = str('********@yahoo.com')  # your username
password = str('********')  #yahoo sign-in pass app token
  
try :
    server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    server.login(username,password)
    server.sendmail(sender, to,msg)
    server.quit()    
    print ('ok the email has been sent ')
except :
    print ('can\'t send the Email')
 """



###########################################################################
#Another way

import smtplib
from email.message import EmailMessage

# The Email Syntax
email = EmailMessage()
email['from'] = '**********@yahoo.com' #sender email
email['to'] = 'ricenek964@laymro.com' #Dummy Email
email['subject'] = 'You won a Million Dollars!'

email.set_content('I am a Python Master!')

#Log in to the client and send it

with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as smtp:
    smtp.ehlo() #hello the starting msg
    #smtp.starttls() #encryption mechanism, connecting to email
    smtp.login('********@yahoo.com','********')
    smtp.send_message(email)
    print('Email Sent Successfully!')
###########################################################################

