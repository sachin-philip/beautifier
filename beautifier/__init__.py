import re

__version__ = "0.2"



class Beautifier(object):

	def __init__(self):
		pass


	def emailToDomain(self, email):
		"""
		function identifies email pattern from sentence and
		convert email to its domain
		"""
		try:
			sent = re.search('@.*', email).group().split(' ')[0]
			return sent.split('@')[1]
		except:
			return "no email patter found!"


	def domainCleanup(self, url):
		"""
		function cleans all http patterns and gives clear output 
		"""
		return url.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")


	def cleanUrl(self, url):
		"""
		function clean the url patterns
		"""
		return url.replace("\r\n", "").replace("\n", "").replace("\r", "").replace('"', '').split('?auth')[0]
		
		

		
		
		


