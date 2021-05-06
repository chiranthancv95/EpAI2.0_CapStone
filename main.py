
'''
This is the main script that runs the app.
As mentioned in the readme, there are two modes available to the user.
If selected '1', then it enables bulk mailing.
If selected '2' or any other number, then it enables single mailing option to the user.
'''


import os

import argparse

from utils_package.certificate_creator import print_certificate
from utils_package.decorators import timeit,func_name
from utils_package.iterator_class import FileIter
#from utils_package.send_mail import mailer
from utils_package.send_mail_smtp import mailer_smtp
from utils_package.parser_args import filename, path, sleep_timer,name, score, total, email, single_mode,passwords



if single_mode == '1':
	try: 
		items = FileIter(filename)
		csv_info= "".join(next(items))

		csv_info_list = csv_info.split('\n')

			
		csv_info_iterator = iter(csv_info_list)

		print(next(csv_info_iterator))
		cert_map_object = map(print_certificate,csv_info_iterator)
		print(list(cert_map_object))
	except IndexError as error:
		#runs the sending email part since the IndexError is a known error which occurs during the map call 
		print(error)
	try:
		# Sending the mails now
		mail_items = FileIter(filename)
		mail_info= "".join(next(mail_items))

		mail_info_list = mail_info.split('\n')


		mail_info_iterator = iter(mail_info_list)

		print(next(mail_info_iterator))

		mail_map_object = map(mailer_smtp,mail_info_iterator)
		print(list(mail_map_object))
	except IndexError as error:
		print(error)

else:
	index = '1'
	info_obj = str(index)+','+ str(name) + ','+ str(score) +' ,'+ str(email)+','+str(total)
	#info_obj = [str(index,name,score,email)]
	#index,name,score,mail=a[0],a[1],a[2],a[3]
	
	#info_obj.append(index,name,score,email)
	print_certificate(info_obj)
	mailer_smtp(info_obj)

print("Finished sending all mails with certificates to the qualified candidates")

