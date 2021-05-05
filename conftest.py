# test/conftest.py
import pytest

def pytest_addoption(parser):
	# parser.addoption("--username", action="store", help="input useranme")
	# parser.addoption("--password", action="store", help="input password")
	parser.addoption('--filename', action="store",type=str, default='/home/cv/workspace2/EpAI2.0_CapStone/file2.csv', help="defines the csv file to be processed")
	parser.addoption('--sleep', action="store",type=str, default='1', help="defines the gap between mails sent, default is set to 30secs")
	parser.addoption('--path', action="store",type=str, default='/home/cv/workspace2/EpAI2.0_CapStone/certificates', help="defines the path where the certificates are to be stored")
	parser.addoption('--certificate_file',action="store", type=str, default="/home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg", help="defines the path where the certificate template is stored for loading")
	parser.addoption('--single_mode',action="store",type=str,default='1', help="If single_mode is set to 1, then we ask name, course name, score and total from the user, else 2 is for sending multiple")
	parser.addoption('--name',type=str, action="store",help="Specify name to be written on certificate")
	parser.addoption('--course_name', action="store",type=str, default="EPAI 2.0 Course", help="Specify the course name to be written on the certificate")
	parser.addoption('--score',type=str, action="store",help="Specify the score to be written on the certificate")
	parser.addoption('--total',type=str, action="store",default='100', help="Specify the total score to be written on the certificate")
	parser.addoption('--email', type=str, action="store",help="Specify the email to be sent with the certificate")
	parser.addoption('--sender_email', action="store",type=str, default='chirantan.rude@gmail.com', help="defines the email through which certificates are sent out")
	parser.addoption('--passwords', type=str, help="Defines the password for th emailer's account")

@pytest.fixture
def params(request):
	params = {}
	# params['username'] = request.config.getoption('--username')
	# params['password'] = request.config.getoption('--password')
	params['filename'] = request.config.getoption('--filename')
	params['sleep'] = request.config.getoption('--sleep')
	params['path'] = request.config.getoption('--path')
	params['certificate_file'] = request.config.getoption('--certificate_file')
	params['single_mode'] = request.config.getoption('--single_mode')
	params['name'] = request.config.getoption('--name')
	params['course_name'] = request.config.getoption('--course_name')
	params['score'] = request.config.getoption('--score')
	params['total'] = request.config.getoption('--total')
	params['email'] = request.config.getoption('--email')
	params['sender_email'] = request.config.getoption('--sender_email')
	params['passwords'] = request.config.getoption('--passwords')
	if params['name'] is None or params['course_name'] is None or params['score'] is None or params['total'] is None or params['email'] is None or params['sender_email'] is None:
		pytest.skip()
	return params