# EpAI CapStone Project
# Mailer App
## Problem Statement

You are going to build a Python app that can:<br>
read a CSV file that has NAME, SCORE and EMAIL (10+, use the fact that admin@theschoolofai.in and ad.min@theschoolofai.in are the same email ids, so 
you can use your own for testing)<br>
loads this image (Links to an external site.) (you can use OpenCV, PIL, or anything else you want)<br>
copies each name from the CSV file and adds it to the image (again use OpenCV and font support there to write it on the image) along with other details.<br> The certificate should finally read:<br>
Award of Excellence for "COURSE NAME" Awarded to "NAME". Date 24th April 2021. Signature "FIXED NAME". You must make sure that the items are placed exactly at the location they should be and with the appropriate font size. <br>
learn how to send emails using Python using this tutorial (Links to an external site.). <br>
Then compose an email that:<br>
will send the final certificate to the email address<br>
reads another file where this email content is written:<br>
Dear NAME,<br>

Congratulations! You have cleared the COURSE NAME with SCORE marks out of TOTAL marks!<br>

We are excited to share the attached Award of Excellence for your performance!<br>

Regards<br>

These are the things that are expected:<br>

your code is well documented<br>
your code has at least 50 test cases that test various problems that might be there. Some tests that are expected:<br>
regex check for emails<br>
can handle 1000+ emails without getting crashed <br>
check if names have only characters<br>
checks if internet connection exists<br>
checks if all required (including external) packages are installed<br>
NAME, COURSE NAME, SCORE, TOTAL are variables and can be changed while calling your Python App<br>
you are using at least 2 different custom modules<br>
you are using at least 1 or more packages<br>
you are NOT using while or for loop anywhere<br>
you are use generators and NOT list comprehension anywhere<br>
you are using your OWN Iterator class for creating your name, email and scores database.<br>
you are using:<br>
named tuples<br>
Python's datetime module<br>
at least 2 decorators (eg, a decorator that "knows" if internet connection is there, etc).<br>
the certificates you attach have a proper name (not image1, etc)<br>
all certificates are finally stored in a folder<br>
checks internet connection before doing anything<br>
checks if the external packages that are required (like PIL, OpenCV are already installed)<br>
checks if the certificate already exists in the folder, and if yes, then do not create it again<br>
emails must be sent out at a gap of 30-60 seconds (selectable while running the app)<br>
your code automatically converts names to their "proper form", e.g. ROHAN SHRAVAN to Rohan Shravan<br>
your app can be called from the command line while providing the variable details as well as the CSV file location<br>
your app first runs "some of the tests" before actually sending emails<br>
**In your final submission, you need to send emails to yourself 10+ times, then add the 10+ certificates in the folder on Github along with the code, as well as the screenshot of your Gmail box showing these 10+ email along with the time stamp<br>**

## Introduction

This is a repo which helps the user to generate certificates with the candidate's name, marks scored, total marks, course name, date issued, signature of the instructor. <br>
The user can then send the certificates to the candidates through mail.<br>
The user is given option whether to use a csv file with format of 'name, score, total' to send mails in bulk.<br>
Otherwise, the user can send a single mail using the command line arguments.<br>
The usage and other instructions are provided below.<br>


## Installation and Requirements
opencv-python
pytest
email_validator
urllib3
tcp-latency
pyspeedtest
speedtest-cli
pillow
img2pdf
sendgrid

Note - All these can be installed using the requirements.txt<br>

Command - 
'''shell
pip install -r requirements.txt
'''

##  Usage

Two Modes are provided for the user which can be used on the need - 
1. Bulk Mode<br>
2. Single Mode<br>


1. Bulk Mode - 
Using this mode, the user can send multiple mails to the candidates whose information is given in the form of a csv file.<br>
For using this mode, please give a csv file which is in the format of 'name, score, email'<br>

Command - 

```shell
python main.py --filename <file-path-for-csv> --sleep <sleep-timer-in-int> --path <path-to-store-certificates> --certificate_file <path-for-certificate-file> --single_mode <bulk-mode-or-single-mode-selector> --sender_email <mailer_address> --password <mailer-password>
```

Sample Command -

```shell
python main.py --filename /home/cv/workspace2/EpAI2.0_CapStone/file2.csv --sleep 0 --path /home/cv/workspace2/EpAI2.0_CapStone/certificates --certificate_file /home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg --single_mode 1
```


2. Single Mode - 
Using this mode, the user can send a single mail to the candidate whose information is to be given as a command line argument instead of a csv file <br>

Command - 

```shell
python main.py --filename <file-path-for-csv> --sleep <sleep-timer-in-int> --path <path-to-store-certificates> --certificate_file <path-for-certificate-file> --single_mode <bulk-mode-or-single-mode-selector> --name <string> --course_name <string> --score <int> --total <int> --email <email_address> --sender_email <mailer_address> --password <mailer-password>
```

Sample Command -

```shell 
python main.py --filename /home/cv/workspace2/EpAI2.0_CapStone/file2.csv --sleep 0 --path /home/cv/workspace2/EpAI2.0_CapStone/certificates --certificate_file /home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg --single_mode 2 --name chiru --course_name new1111 --score 80 --total 101 --email some@example.net --sender_email some@gmail.com --password some
```

## Command-line-arguments 

**--filename** 
defines the csv file to be processed

**--sleep**
defines the gap between mails sent, default is set to 30secs

**--path**
defines the path where the certificates are to be stored

**--certificate_file**
defines the path where the certificate template is stored for loading

**--single_mode**
If single_mode is set to 1, then we ask name, course name, score and total from the user, else 2 is for sending multiple

**--name**
Specify name to be written on certificate

**--course_name**
Specify the course name to be written on the certificate

**--score**
Specify the score to be written on the certificate

**--total**
Specify the total score to be written on the certificate

**--email**
Specify the email to be sent with the certificate

**--sender_email**
defines the email through which certificates are sent out

**--password**
Defines the password for th emailer's account

## Testing of Code
The code contains around 50 test codes to ensure the standard quality of the code.<br>
The codes are written using the pytest module.<br>
The file named "test_capstone.py" contains all the test cases.<br>
The user can test out the code using the following commands for both the modes.<br>

Command - 

Pytest Command for multiple - 

```shell
pytest -s test_capstone.py --filename /home/cv/workspace2/EpAI2.0_CapStone/file2.csv --sleep 0 --path /home/cv/workspace2/EpAI2.0_CapStone/certificates --certificate_file /home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg --single_mode 1 --name chiru --course_name new1111 --score 80 --total 101 --email some@example.net --sender_email some@gmail. --password some
```

Pytest Command for single mail - 

```shell
pytest -s test_capstone.py --filename /home/cv/workspace2/EpAI2.0_CapStone/file2.csv --sleep 0 --path /home/cv/workspace2/EpAI2.0_CapStone/certificates --certificate_file /home/cv/workspace2/EpAI2.0_CapStone/certificate.jpg --single_mode 2 --name chiru --course_name new1111 --score 80 --total 101 --email some@example.net --sender_email some@gmail.com --password some
```


## Module Explanation

### iterator_class

This module is to create a generator using custom iterator class.

### parser_args

This module is used to get all the command-line arguments from the user.

### send_mail

This module is used to send mails to candidates using a third-party offering from sendgrid.

### send_mail_smtp

This module is used to send mails with certificates to candidates using the python's built-in library.(It's freeeee)

### decorators

This module is used to create the decorators used for better functioning of other modules.

### certificate_creator

This module is used to create certificates with the given information from the user in both .jpg and .pdf file which can be attached while sending the mail.

### conftest

This module is used to fix the arguments for the testing of code using pytest.

### test_capstone

This module is the one which contains all the test cases for testing purposes.


**Note - Apart from conftest, test_capstone are contained in the utils_package which is a custom package.**

