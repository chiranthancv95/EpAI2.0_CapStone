import sendgrid
import os
from sendgrid.helpers.mail import *
import img2pdf
from PIL import Image
import base64
from utils_package.parser_args import filename, path, certificate_file, sleep_timer,name, score, total, email, single_mode, course_name, sender_email
from utils_package.decorators import *

import time


@timeit
@func_name
@is_connected
@logged
#@authenticatedOrNot
def mailer(info):
    #Waiting to send mail
    print(f"Waiting for {sleep_timer} seconds to send next mail")
    time.sleep(sleep_timer)
    a=info.split(',')
    index,name,score,mailid=a[0],a[1],a[2],a[3]

    total=str(100)

    try:
        total = a[4]
    except Exception as e:
        pass

    name = name.title()
    name="".join(name.split())

    SENDGRID_API_KEY = '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'
    os.environ['SENDGRID_API_KEY'] = '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'
    #sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY )
    
    # path 
    #path = '/home/cv/workspace2/EpAI2.0_CapStone/certificates'

    with open(os.path.join(path, name+'_certificate.pdf'), 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(os.path.join(path, name+'_certificate.pdf')),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    #mail.attachment = attachedFile
    
    #API_KEY='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'
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get(SENDGRID_API_KEY))
    #sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY))
    from_email = Email(sender_email)
    print("Sending to mailid: ", mailid)
    #to_email = To("chirantan.rude@gmail.com")

    to_email = To(mailid)
    subject = "Certificate of Course Completion_new7"
    content_str=(f'Dear {name},\nCongratulations! You have cleared the EPAI 2.0 Course with {score} marks out of {total} marks!\n We are excited to share the attached Award of Excellence for your performance!\n Regards')
    content = Content("text/plain",content_str)
    mail = Mail(from_email, to_email, subject, content)
    mail.attachment = attachedFile
#     mail.add_attachment(attachment)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return content_str