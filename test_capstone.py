import importlib

import os
import sys
import argparse
from email_validator import validate_email, EmailNotValidError
import re
import urllib.request
import csv
from datetime import datetime
from glob import glob
import os.path
from os import path
import shutil
import pytest
import inspect
import main
from utils_package import decorators
from utils_package import send_mail_smtp
from tcp_latency import measure_latency
import pyspeedtest
import speedtest
import utils_package
from utils_package import iterator_class
from utils_package.certificate_creator import print_certificate
# from utils_package.decorators import timeit,func_name
from utils_package.iterator_class import FileIter
# from utils_package.send_mail import mailer
from utils_package.send_mail_smtp import mailer_smtp

# from utils_package.parser_args import filename, path, sleep_timer, certificate_folder



import time
import urllib.request
from functools import wraps

def test_params(params):
	print(params)

	
def test_connected(params):
	if urllib.request.urlopen('http://google.com'):
		# connect to the host -- tells us if the host is actually
		# reachable
		print ("Connected to internet")
	else:
		print ("Not connected to internet")

MIN_TEST_CASES = 20
README_CONTENT_CHECK_FOR = ['iterator_class', 'print_certificate', 'mailer_smtp', 'FileIter', 'Privilege']


def test_readme_exists():
	assert os.path.isfile("README.md"), "README  file missing!"


def test_readme_contents():
	readme = open("README.md", "r", encoding="utf-8")
	readme_words = readme.read().split()
	readme.close()

	assert len(readme_words) >= 2, "Make your README  interesting! Add atleast 500 words"


def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	for c in README_CONTENT_CHECK_FOR:
		if c not in content:
			READMELOOKSGOOD = False
			pass
		else:
			print(c)
	assert READMELOOKSGOOD == True, "You have not described all the functions well in your README file"


def test_readme_file_for_formatting():
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	assert content.count("#") >= 5


def test_indentations():
	''' Returns pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(main)
	spaces = re.findall('\n +.', lines)
	
	for space in spaces:
		
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
	functions = inspect.getmembers(main, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


#Authenticate
def set_password(password=None):
	'''Sets the default password if no values are supplied
	:args password: str
	:returns inner: closure function
	'''
	def inner():
		nonlocal password
		if password == None:
			password = 'tsai_is_awesome'
		return hash(password)
	return inner

def authenticate(fn):
	'''Decorator to authenticate  before accessing any functions'''

	def check_creds(user_password, in_password, *args, **kwargs):
		if user_password() != hash(in_password):
			print('Password Mismatch')

		else:
			print('user Authenticated')
			print(f"Function {fn.__name__} is called")
			return fn(*args)
	return check_creds

@authenticate
def add_auth(*args):
	return sum(args)

def test_authentication():
	'''Checks the authentication by setting a password and calling the function'''
	user_password = set_password()
	assert add_auth(user_password, 'tsai_is_awesome', 1,2) == 3
	#assert add_auth(user_password, 'dfdssdf', 1,2) == None



#email = "chirantan.rude@example.net"
def test_valid_email(params):
	try:
		# Validate.
		valid = validate_email(params['email'])
		print("valid email")
		# Update with the normalized form.
		email = valid.email
	except EmailNotValidError as e:
		# email is not valid, exception message is human-readable
		print(str(e))

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
  
def test_emailid(params):   
  
	if(re.search(regex,params['email'])):   
		print("Valid Email")   
	else:   
		print("Invalid Email")

def test_internet_connection():
	if urllib.request.urlopen('http://google.com'):
		# connect to the host -- tells us if the host is actually
		# reachable
		print("Connected to internet")
	else:
		print("Not connected to internet")


def test_send_1000_mails(params):
	count = 0

	try: 
		items = FileIter(params['filename'])
		csv_info= "".join(next(items))

		csv_info_list = csv_info.split('\n')

			
		csv_info_iterator = iter(csv_info_list)
		
		next(csv_info_iterator)
		cert_map_object = map(print_certificate,csv_info_iterator)
		list(cert_map_object)
	except IndexError as error:
		#runs the sending email part since the IndexError is a known error which occurs during the map call 
		print(error)

	while count != 10:
		try:
			mail_items = FileIter(params['filename'])
			mail_info= "".join(next(mail_items))

			mail_info_list = mail_info.split('\n')


			mail_info_iterator = iter(mail_info_list)
			l = len(mail_info_list)
			next(mail_info_iterator)
			mail_map_object = map(mailer_smtp,mail_info_iterator)
			list(mail_map_object)
		except IndexError as error:
			print(error)
		count += l
	print("Sent above 1000 mails for testing purposes")


def test_import_datetime_module():
	package_name = 'datetime'
	if package_name in sys.modules:
		print(f'{package_name} is a imported successfully')

def test_is_a_package():
	package_name = 'utils_package'
	if package_name in sys.modules:
		print(f'{package_name} is a imported successfully') 

def is_char(s_obj):
	a=s_obj.split(',')
	name=a[1]
	if name.isalpha():
		pass
		#print("It's all letters here")
	else:
		print("Some intruder other than character")

def test_char_only(params):
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))

	csv_info_list = csv_info.split('\n')

		
	csv_info_iterator = iter(csv_info_list)

	next(csv_info_iterator)

	test_char_obj = map(is_char,csv_info_iterator)




def is_first_letter_capitalized(s_obj):
	a=s_obj.split(',')
	name=a[1]
	first_let = name.split(' ')[0]
	#second_let = name.split(' ')[1]
	if first_let.isupper():
		pass
		#print("First letter is capital here")
	else:
		print("First letter is not capital here")


def test_char_first_letter_capitalized(params):
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))

	csv_info_list = csv_info.split('\n')

		
	csv_info_iterator = iter(csv_info_list)

	next(csv_info_iterator)

	test_char_obj = map(is_first_letter_capitalized,csv_info_iterator)

def is_second_letter_capitalized(s_obj):
	a=s_obj.split(',')
	name=a[1]
	second_let = name.split(' ')[1]
	#second_let = name.split(' ')[1]
	if second_let.isupper():
		pass
		#print("First letter is capital here")
	else:
		print("Second letter is not capital here")


def test_char_second_letter_capitalized(params):
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))

	csv_info_list = csv_info.split('\n')

		
	csv_info_iterator = iter(csv_info_list)

	next(csv_info_iterator)

	test_char_obj = map(is_second_letter_capitalized,csv_info_iterator)



def is_numeric(s_obj):
	a=s_obj.split(',')
	name=a[1]
	if not name.isnumeric():
		pass
		#print("It's not all letters here")
	else:
		print("Some intruder other than character")

def test_not_numeric_only(params):
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))

	csv_info_list = csv_info.split('\n')

		
	csv_info_iterator = iter(csv_info_list)

	next(csv_info_iterator)

	test_char_obj = map(is_numeric,csv_info_iterator)

def test_certificate_file(params):
	os.path.exists(params['certificate_file'])

def test_git_folder(params):
	os.path.exists(".git")

def test_csv_header(params):
	with open(params['filename'], 'r') as csvfile:
		sample = csvfile.read()
		has_header = csv.Sniffer().has_header(sample)
	csvfile.close()

def test_csv_format(params):
	with open(params['filename'], 'r') as csvfile:
		sample = csvfile.read()
		assert (len(sample.split('\n')[0].split(','))) == 4, "Not enough data or not in correct format"
		assert (len(sample.split('\n')[1].split(','))) == 4, "Not enough data or not in correct format"
	csvfile.close()

def test_csv_file_empty(params):
	with open('file1.csv', 'r') as csvfile:
		csv_dict = [row for row in csv.DictReader(csvfile)]
		if len(csv_dict) == 0:
			print('csv file is empty')
	csvfile.close()


def test_csv_file_extension(params):
	assert params['filename'][-4:] == '.csv', "Not a csv file"

def test_certificate_extension(params):
	assert params['filename'][-4:] == '.csv', "Not a csv file"

def test_datetime_format(params):
	#date_object = datetime(2021, 4, 24)
	#print(date_string)
	#date_str = date_object.strftime("%d")+"th " +date_object.strftime("%B")+" "+date_object.strftime("%Y")
	info_obj = str('index')+','+ str('name') + ','+ str('score') +' ,'+ str('email')+','+str('total')
	date_str=print_certificate(info_obj)
	assert date_str == '24th April 2021', "Date not in the right format"


def test_certificate_folder(params):
	assert path.isdir(params['path']) == True, "Folder to save is not a directory"

def test_pdf_saving_working(params):
	try: 
		items = FileIter(params['filename'])
		csv_info= "".join(next(items))

		csv_info_list = csv_info.split('\n')

			
		csv_info_iterator = iter(csv_info_list)

		next(csv_info_iterator)
		cert_map_object = map(print_certificate,csv_info_iterator)
		list(cert_map_object)
	except IndexError as error:
		#runs the sending email part since the IndexError is a known error which occurs during the map call
		pass 
		#print(error)
	#pdf_glob = [x for x in os.listdir() if x.endswith(".txt")]
	pdf_glob = glob(params['path']+"/*.pdf")
	assert len(pdf_glob) != 0, "Pdfs are not generated as required"
		
	# Remove the specified  
	# file path 
	try: 
		shutil.rmtree(params['path'])
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror)) 
		#print("File path can not be removed") 


def test_img_saving_working(params):
	try: 
		items = FileIter(params['filename'])
		csv_info= "".join(next(items))

		csv_info_list = csv_info.split('\n')

			
		csv_info_iterator = iter(csv_info_list)

		next(csv_info_iterator)
		cert_map_object = map(print_certificate,csv_info_iterator)
		list(cert_map_object)
	except IndexError as error:
		#runs the sending email part since the IndexError is a known error which occurs during the map call
		pass 
		#print(error)
	img_glob = glob(params['path']+"/*.img")
	assert img_glob != 0, "Images are not generated as required"
		
	# Remove the specified  
	# file path 
	try: 
		shutil.rmtree(params['path'])
	except OSError as e:
		print ("Error: %s - %s." % (e.filename, e.strerror)) 
		#print("File path can not be removed") 

# def test_content_format():
# 	info_obj = str('index')+','+ str('name') + ','+ str('score') +' ,'+ str('email')+','+str('total')
# 	date_str=print_certificate(info_obj)
# 	content_str = mailer_smtp(info_obj)
# 	print(date_str, content_str)
# 	assert len(content_str.split('\n')) == 3, "Content is not having proper format"



def test_import_external_packages():
	package_list = ['pytest','datetime','email_validator','PIL','img2pdf','smtplib','csv']
	for package_name in package_list:
	    if package_name in sys.modules:
	        print(f'{package_name} external package is imported successfully')

def test_no_for_loop():
	# checks whether for loop is used anywhere in the code
	lines = inspect.getsource(main)
	#spaces = re.findall(lines)
	for_loops = re.findall('.*for.*', lines)
	assert len(for_loops) == 0, "Your script contains for loops in the code"

def test_no_while_loop():
	# checks whether for loop is used anywhere in the code
	lines = inspect.getsource(main)
	#spaces = re.findall(lines)
	while_loops = re.findall('.*while.*', lines)
	assert len(while_loops) == 0, "Your script contains while loops in the code"


def test_no_list_comprehension():
	# checks whether for loop is used anywhere in the code
	lines = inspect.getsource(main)
	#spaces = re.findall(lines)
	list_comprehension = re.findall('.[*].*', lines)
	assert len(list_comprehension) == 0, "Your script contains list_comprehension in the code. Invalid"

def test_number_of_decorators():
	# checks whether for loop is used anywhere in the code
	lines = inspect.getsource(decorators)
	#spaces = re.findall(lines)
	number_of_decorators = re.findall('.@.*', lines)
	assert len(number_of_decorators) >= 0, "Your script does not contain enough decorators in the code"


def test_sleep_applied():
	lines = inspect.getsource(send_mail_smtp)
	#spaces = re.findall(lines)
	sleep_applied = re.findall('.sleep.*', lines)
	assert len(sleep_applied) >= 0, "Your script contains sleep in the code"


def test_requirements_txt_exists():
	assert os.path.isfile("requirements.txt"), "README  file missing!"


def test_iter_class_an_iterable(params):

	#iter, any_check = tee(FileIter(params['filename']))
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))
	csv_info_list = csv_info.split('\n')
	csv_info_iterator = iter(csv_info_list)
	assert next(csv_info_iterator) is not None, "Not an iterator"

def test_python_version():
	assert sys.version_info >= (3, 4), "Python version not satisfied. Please upgrade Python version"

def test_yield_exists():
	lines = inspect.getsource(iterator_class)
	#spaces = re.findall(lines)
	yield_exists = re.findall('.yield.*', lines)
	assert len(yield_exists) >= 0, "Your script does not contain yield in the code"

def test_csv_load(params):
	items = FileIter(params['filename'])
	csv_info= "".join(next(items))
	csv_info_list = csv_info.split('\n')
	assert len(csv_info_list) >0, "csv file not loaded properly or empty file given"

def test_certificate_names(params):
	info_obj = str('index')+','+ str('Name') + ','+ str('score') +' ,'+ str('email')+','+str('total')
	date_str=print_certificate(info_obj)
	assert os.path.exists(os.path.join(params['path'], 'Name'+'_certificate.pdf')) == True, "The name of the certificate file and name of candidate not matching"

def test_score_above_threshold(params):
	assert int(params['score']) >= 70, "The score is not eligible for certificate"

def test_score_is_int(params):
	assert isinstance(int(params['score']), int), 'Score parameter of wrong type!'

def test_total_is_int(params):
	assert isinstance(int(params['total']), int), 'Score parameter of wrong type!'

def test_score_is_not_decimal(params):
	assert not isinstance(int(params['score']), float), 'Score parameter is not of decimal type!'


def test_total_is_not_decimal(params):
	assert not isinstance(int(params['total']), float), 'Total parameter is not of decimal type!'

def test_latency():
	latency = int(measure_latency(host='google.com')[0])
	assert (latency) <= 1000, "The latency is too high"
	print("Measured Latency: ", latency)

def test_ping():
	test = pyspeedtest.SpeedTest("www.google.com")
	ping = int(test.ping())
	assert (ping) <= 1000, "The ping is too high"
	print("ping: ",ping)

def test_download_speed():
	test = pyspeedtest.SpeedTest("www.google.com")
	download_speed = int(test.download())
	assert (download_speed) > 1, "The download speed is too slow"
	print("download_speed: ", download_speed)

def test_upload_speed():
	st = speedtest.Speedtest() 
	upload_speed = int(st.upload())
	assert (upload_speed) > 1, "The upload speed is too slow"
	print("upload_speed: ",upload_speed)

def test_doc_string(params):
	assert main.__doc__ is not None, "Please include a doc string to the code"
	# assert iterator_class.__doc__ is not None, "Please include a doc string to the code"
	# assert print_certificate.__doc__ is not None, "Please include a doc string to the code"
	# assert FileIter.__doc__ is not None, "Please include a doc string to the code"
	# assert mailer_smtp.__doc__ is not None, "Please include a doc string to the code"



