import os

import argparse

# required defines a mandatory argument 
# default defines a default value if not specified

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--filename', type=str, default='/home/cv/workspace2/EpAI2.0_CapStone/file2.csv', help="defines the csv file to be processed")
parser.add_argument('-s', '--sleep', type=str, default='1', help="defines the gap between mails sent, default is set to 30secs")
parser.add_argument('-p', '--path', type=str, default='/home/cv/workspace2/EpAI2.0_CapStone/certificates', help="defines the path where the certificates are to be stored")
parser.add_argument('-c', '--certificate_file', type=str, default="/home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg", help="defines the path where the certificate template is stored for loading")
parser.add_argument('-sm','--single_mode',type=str,default='1', help="If single_mode is set to 1, then we ask name, course name, score and total from the user, else 2 is for sending multiple")
parser.add_argument('-na','--name',type=str, help="Specify name to be written on certificate")
parser.add_argument('-cn','--course_name', type=str, default="EPAI 2.0 Course", help="Specify the course name to be written on the certificate")
parser.add_argument('-sc','--score',type=str, help="Specify the score to be written on the certificate")
parser.add_argument('-tot','--total',type=str, default='100', help="Specify the total score to be written on the certificate")
parser.add_argument('-em', '--email', type=str, help="Specify the email to be sent with the certificate")
parser.add_argument('-se_em', '--sender_email', type=str, default='chirantan.rude@gmail.com', help="defines the email through which certificates are sent out")
parser.add_argument('-pa','--passwords', type=str, help="Defines the password for th emailer's account")
args = parser.parse_args()


sleep_timer = args.sleep
path = args.path
filename = args.filename
certificate_file = args.certificate_file
single_mode = args.single_mode
name =args.name
course_name = args.course_name
score = args.score
total = args.total
email = args.email
sender_email = args.sender_email
passwords = args.passwords

