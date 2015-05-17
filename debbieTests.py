import unittest
import requests
from debbie import isOnView

onView = requests.get('http://scrapi.org/object/547802?fields=galleryLink') #temple of dendur
notOnView = requests.get('http://scrapi.org/object/483879?fields=galleryLink') #cy twombly

class isOnViewTests(unittest.TestCase):
	print 'setting up'
	
	def testIsOnView(self):
		self.assertTrue(isOnView(onView))
	
	def testIsNotOnView(self):
		self.assertFalse(isOnView(notOnView))

def main():
	unittest.main()

if __name__ == '__main__':
	main()
