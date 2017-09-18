#!/usr/bin/env python

from sys import argv

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.abc.com"
mail_user="user1"
mail_pass="passwd1"

sender = 'user1@abc.com'
receivers = argv[1]

message = MIMEText(argv[2], 'plain', 'utf-8')
message['From'] = Header("user1<user1@abc.com>", 'utf-8')
message['To'] = Header("warning list", 'utf-8')

message['Subject'] = Header("this is a warning", 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "success!"
	smtpObj.close()
except smtplib.SMTPException:
	print "Error!"
	