import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호머니?')

email_list = ['fun3440@gmail.com','fun4001@nate.com']

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "제목이지롱"
    msg['From'] = "fun3440@naver.com"
    msg['To'] = email
    msg.set_content('내용이지롱')

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)  #보안SSL

s.login('fun3440',password )
s.send_message(msg)