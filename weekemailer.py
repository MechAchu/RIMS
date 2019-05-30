import smtplib
from email.mime.text import MIMEText

with open(textfile, 'r') as fp:
    msg = MIMEText(fp.read())

msg['Subject'] = 'Weekly Report' % textfile
msg['From'] = 'rims.maildaemon@gmail.com'
msg['To'] = 'ironpatriots4135@gmail.com'

s = smtplib.SMTP('localhost')
s.sendmail('rims.maildaemon@gmail.com', ['ironpatriots4135@gmail.com'], msg.as_string())
s.quit()
