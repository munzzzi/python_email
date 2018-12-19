import smtplib #메일보낼때
import csv #CSV파일을열때
from email.message import EmailMessage #메일보낼때

import getpass #패스워드 보안
password = getpass.getpass('비밀번호머니?')


f = open('pygj.csv','r', encoding='utf-8')
read_csv = csv.reader(f)

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)  #보안SSL
s.login('fun3440@naver.com',password )

for line in read_csv:
    msg = EmailMessage()
    msg['Subject'] = line[0] + "님에게 보내는 메일입니다."
    msg['From'] = "fun3440@naver.com"
    msg['To'] = line[1]
    msg.set_content('강민지입니다:>' )
    s.send_message(msg)

