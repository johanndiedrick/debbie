import requests
from debbieMailer import sendMail

def isOnView(object):
	objectNumber = object.json()['CRDID']
	objectOnViewStatus = object.json()['galleryLink']
	if objectOnViewStatus == 'This artwork is not on display':
		print 'not on view'
		return False
	else:
		print 'on view'
		recipient = 'jdiedrick@gmail.com'
		sendMail(recipient, objectNumber)	
		return True

artworkOnView = requests.get('http://scrapi.org/object/547802?fields=galleryLink') #temple of dendur

artworkNotOnView = requests.get('http://scrapi.org/object/483879?fields=galleryLink') #cy twombly


isOnView(artworkOnView)

isOnView(artworkNotOnView)
