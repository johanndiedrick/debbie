import requests

def isOnView(object):
	if object.json()['galleryLink'] == 'This artwork is not on display':
		print 'not on view'
		return False
	else:
		print 'on view'
		return True

artworkOnView = requests.get('http://scrapi.org/object/547802?fields=galleryLink') #temple of dendur

artworkNotOnView = requests.get('http://scrapi.org/object/483879?fields=galleryLink') #cy twombly


isOnView(artworkOnView)

isOnView(artworkNotOnView)
