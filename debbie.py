import requests

def isOnView(object):
	if object.json()['galleryLink'] == 'This artwork is not on display':
		print 'not on view'
	else:
		print 'on view'

artworkOnView = requests.get('http://scrapi.org/object/553045?fields=galleryLink') #egyptian statue

artworkNotOnView = requests.get('http://scrapi.org/object/483879?fields=galleryLink') #cy twombly


isOnView(artworkOnView)

isOnView(artworkNotOnView)
