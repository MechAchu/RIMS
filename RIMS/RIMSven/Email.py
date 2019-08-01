import smtplib

#if(items in database are less than number):
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(user = 'beyerroboticswebsite@gmail.com', password = 'IronPatriots')
server.sendmail('beyerroboticswebsite@gmail.com', 'jacob_suveges@hotmail.com', 'We are low on items')
server.quit()
#Pagani.H@monet.k12.ca.us
#In robotics email need to set security setting
