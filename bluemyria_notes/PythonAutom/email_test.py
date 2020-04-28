import smtplib, time
import imapclient

def sendmyemail():
    conn = smtplib.SMTP('smtp.gmail.com', 587)

    conn.ehlo()
    conn.starttls()
    conn.login('xxxxx@gmail.com','xxxxx')
    conn.sendmail('xxxxx@gmail.com','xxxxx@gmail.com', 'Subject: So Long from Python...\n\nHi Bluemyria this is sent from your Python program!')
    conn.quit()



def checkemail():
    conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    conn.login('xxxxx@gmail.com', 'mjnhbgvf!1')
    conn.select_folder('INBOX', readonly=True)
    mids = conn.search('SINCE 28-Apr-2020')
    print(conn.fetch([mids[-1]], ['BODY[]', 'FLAGS']))

#sendmyemail()
checkemail()