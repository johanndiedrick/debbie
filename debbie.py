import grequests
from debbieMailer import sendMail
from debbie_globals import debbie_recipient
import ssl_fix
import sqlite3

objectIDs = [547802, 483879, 45417, 76970, 265169, 480895, 292043, 45434, 467642, 500666]

def scrapiURLFromOID(objectID):
	scrapiURL = "http://scrapi.org/object/" + str(objectID)
	return scrapiURL

def isOnView(object, *args, **kwargs):
	objectNumber = object.json()['CRDID']
	objectOnViewStatus = object.json()['galleryLink']
	print objectOnViewStatus
	if objectOnViewStatus == 'This artwork is not on display':
		print 'not on view'
		return None
	else:
		print 'on view'
		recipient = debbie_recipient
		sendMail(recipient, objectNumber, True)	
		return None

def hook_factory(*factory_args, **factory_kwargs):
	def response_hook(object, *request_args, **request_kwargs):
		objectNumber =object.json()['CRDID']
		objectOnViewStatus = object.json()['galleryLink']
		#print objectOnViewStatus
		if objectOnViewStatus == 'This artwork is not on display':
		#print 'not on view'
			return None
		else:
		#print 'on view'
			new_username = factory_kwargs['new_recipient']
			print "after request " + "u: " + new_username + " obj: " + str(objectNumber)
			sendMail(new_username, objectNumber, False)	
			return None
		return None
	return response_hook

#db code
db = sqlite3.connect('db/debbie.sqlite')
cursor = db.cursor()
cursor.execute('SELECT username, objectID, is_on_view, has_sent FROM objects')

#turn our objects into something managable
objects = []

#requests
rs = []

for object in cursor.fetchall():
	username = object[0]
	objectid = object[1]
	url = scrapiURLFromOID(object[1])
	is_on_view = object[2]
	has_sent = object[3]
	newObject = {
			'username': username, 
			'url': url, 
			'is_on_view': is_on_view, 
			'has_sent': has_sent, 
			'object_id': objectid
			}
	objects.append(newObject) 
	new_username=newObject['username']
	url = newObject['url']
	objid = newObject['object_id']
	print "before request: " + "u: " + new_username + " and " + " obj: " + str(objid)
	rs.append( grequests.get(url, hooks={'response': [hook_factory(new_recipient=new_username)]}) ) 

grequests.map(rs)
