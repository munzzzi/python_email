import smtplib #메일보낼때

from email.message import EmailMessage 

import getpass #패스워드 보안
password = getpass.getpass('비밀번호머니?')



#read_csv = csv.reader(f)



msg = EmailMessage()
msg['Subject'] = " 메일입니다."
msg['From'] = "fun3440@naver.com"
msg['To'] = "fun3440@gmail.com"
#msg.set_content('강민지입니다:>' )
msg.add_alternative('''
<h1>안녕하세요.</h1>
<p>저는 강민지 입니다.</p>
''',subtype="html")

smtp_url = "smtp.naver.com"
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)  #보안SSL

s.login('fun3440@naver.com',password )
s.send_message(msg)
