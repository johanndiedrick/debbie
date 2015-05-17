import smtplib
from debbie_globals import debbie_email, debbie_password


def sendMail(recipient, objectNumber):
	sender = debbie_email 
	password = debbie_password
	msg = "Your object is on view! \nFind out where at http://www.metmuseum.org/collection/the-collection-online/search/" + str(objectNumber)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)
	print msg
	server.sendmail(sender, recipient, msg)
	server.quit()
