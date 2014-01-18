import smtplib
from email.mime.text import MIMEText

def send_email(message,subject,from_email,to_email,smtp_server,smtp_port):
	msg = MIMEText(message)
	msg['Subject']=subject
	msg['From']=from_email
	msg['To']=to_email
	s=smtplib.SMTP(smtp_server,smtp_port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	try :
		s.login(smtp_settings.user,smtp_settings.password)
		s.sendmail(msg['From'], msg['To'], msg.as_string())
	finally :
		s.quit()	
	

