'''
This script generates the certificates of the candidates in a specific format and stores them.
'''



import cv2
import img2pdf
from PIL import Image
from datetime import datetime

import os
from utils_package.parser_args import filename, path, certificate_file, sleep_timer,name, score, total, email, single_mode, course_name, passwords
from utils_package.decorators import *


@timeit
@func_name
def print_certificate(info_obj):
	'''
	This function helps in gathering information from the csv file and aprropriately generating the certificates of the candidates.
	Then stores it as .jpg file extension and later converted to .pdf file which can then be exported with the mail.
	'''
	a=info_obj.split(',')
	index,name,score,mail=a[0],a[1],a[2],a[3]
	# converting name to standard capitalized format
	name_on_certificate = name.title()
	name="".join(name_on_certificate.split())
	img=cv2.imread(certificate_file)


	# font
	font = cv2.FONT_HERSHEY_SIMPLEX

	# fontScale
	fontScale = 1

	color = (0, 0, 0)

	# Line thickness of 2 px
	thickness = 2

	#datetime(year, month, day)
	date_object = datetime(2021, 4, 24)
	#print(date_string)
	
	date_str = date_object.strftime("%d")+"th " +date_object.strftime("%B")+" "+date_object.strftime("%Y")
	
	#positions
	course_position = (370,299)
	image = cv2.putText(img, course_name, course_position, font, 
					   fontScale, color, thickness, cv2.LINE_AA)
	name_position = (400,440)
	image = cv2.putText(img, name_on_certificate, name_position, font, 
					   fontScale, color, thickness, cv2.LINE_AA)
	date_position = (200,525)
	image = cv2.putText(img, date_str, date_position, font, 
					   0.7, color, 2, cv2.LINE_AA)
	signature_position = (630,525)
	image = cv2.putText(img, 'Rohan Shravan', signature_position, font, 
					   0.7, color, thickness, cv2.LINE_AA)
	
		
	# Create the directory only if it does not exist already
	try: 
		os.mkdir(path) 
	except OSError as error: 
		print(error) 
	print(os.path.join(path, name+'_certificate.jpg'))
	cv2.imwrite(os.path.join(path, name+'_certificate.jpg'), img)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	im_pil = Image.fromarray(img)
	pdf_bytes = img2pdf.convert(os.path.join(path, name+'_certificate.jpg'))
	
	file1 = open(os.path.join(path, name+'_certificate.pdf'), "wb")
	# writing pdf files with chunks
	file1.write(pdf_bytes)

	# closing pdf file
	file1.close()
	
	
	print("Printing: ", index,name,score,mail)
	return date_str