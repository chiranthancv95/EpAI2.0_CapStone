
import os

import img2pdf
from PIL import Image
import base64
from utils_package.parser_args import filename, path, certificate_file, sleep_timer,name, score, total, email, single_mode, course_name, sender_email, password
from utils_package.decorators import *

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email_validator import validate_email, EmailNotValidError
import time


def check_valid_email(email):
	try:
		# Validate.
		valid = validate_email(email)
		print("valid email")
		# Update with the normalized form.
		email = valid.email
		return True
	except EmailNotValidError as e:
		# email is not valid, exception message is human-readable
		print(str(e))
		return False



@timeit
@func_name
@is_connected
@logged
#@authenticatedOrNot
def mailer_smtp(info):
	#Waiting to send mail
	print(f"Waiting for {sleep_timer} seconds to send next mail")
	time.sleep(int(sleep_timer))
	a=info.split(',')
	index,name,score,mailid=a[0],a[1],a[2],a[3]

	total=str(100)

	try:
		total = a[4]
	except Exception as e:
		pass

	name = name.title()
	name="".join(name.split())

	fromaddr = sender_email
	toaddr = mailid
	   
	# instance of MIMEMultipart
	msg = MIMEMultipart()
	  
	# storing the senders email address  
	msg['From'] = fromaddr
	  
	# storing the receivers email address 
	msg['To'] = toaddr
	  
	# storing the subject 
	msg['Subject'] = "Certificate of Course Completion_new7"
	  
	# string to store the body of the mail
	#body = "Body_of_the_mail"
	body=(f'Dear {name},\nCongratulations! You have cleared the EPAI 2.0 Course with {score} marks out of {total} marks!\n We are excited to share the attached Award of Excellence for your performance!\n Regards')
	content_str = body

	# attach the body with the msg instance
	msg.attach(MIMEText(body, 'plain'))
	  
	# open the file to be sent 
	filename = name+'_certificate.pdf'
	attachment = open(os.path.join(path, name+'_certificate.pdf'), 'rb')
	  
	# instance of MIMEBase and named as p
	p = MIMEBase('application', 'octet-stream')
	  
	# To change the payload into encoded form
	p.set_payload((attachment).read())
	  
	# encode into base64
	encoders.encode_base64(p)
	   
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	  
	# attach the instance 'p' to instance 'msg'
	msg.attach(p)
	  
	# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)
	  
	# start TLS for security
	s.starttls()
	  
	# Authentication
	s.login(fromaddr, password)
	  
	# Converts the Multipart msg into a string
	text = msg.as_string()
	
	if check_valid_email(toaddr) == True:
		# sending the mail
		s.sendmail(fromaddr, toaddr, text)
	  
	# terminating the session
	s.quit()
	return content_str