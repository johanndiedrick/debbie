import smtplib
from debbie_globals import debbie_email, debbie_password
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


def sendMail(recipient, objectNumber, debug):
	if debug:
		print "debug mode. will send object number " + str(objectNumber) + " to recipient: " + recipient 
	else:
		sender = debbie_email 
		password = debbie_password
		msg = MIMEMultipart()
		msg['From'] = sender
		msg['To'] = recipient
		msg['Subject'] = "Your object is on view at the Met!"
		body = "Your object is on view! \nFind out where at http://www.metmuseum.org/collection/the-collection-online/search/" + str(objectNumber)
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(sender, password)
		text = msg.as_string()
		server.sendmail(sender, recipient, text)
		print "sending mail to " + recipient
		server.quit()
