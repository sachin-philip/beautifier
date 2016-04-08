import re

__version__ = "0.3.1"

		
class Email(object):

	"""function identifies email pattern from sentence and
		convert email to its domain"""

	def __init__(self, email):
		self.domain = None
		self.username = None
		try:
			sent = re.search('@.*', email).group().split(' ')[0]
			self.domain = sent.split('@')[1]
			self.username = email.split('@')[0]
			self.is_valid = True
		except:
			self.is_valid = False
		return


	@property
	def is_free_email(self):
		free_domain_list = open("beautifier/helpers/free_domain_list.txt")
		free_domains = free_domain_list.read().split('\n')
		return True if self.domain in free_domains else False

	@property
	def has_site(self):
	    return self._has_site
	



class Url(object):
	"""docstring for Url"""

	def __init__(self, url):
		self.main_url = url
		self.cleanup = url.replace("\r\n", "").replace("\n", "").replace("\r", "").replace('"', '').split('?auth')[0]

	@property
	def param(self):
		try:
			self.parameters = self.url.split('?')[1]
			return self.parameters.split('&')
		except:
			return

	@property
	def username(self):
		if 'linkedin.com' in self.cleanup:
			return self.cleanup.split("/")[-1]
		else:
			return

	@property
	def domain(self):
	    remove_pac =  self.cleanup.replace("https://", "").replace("http://", "").replace("www.", "")
	    try:
	    	return remove_pac.split('/')[0]
	    except:
	    	return

	@property
	def meta(self):
	    return self.meta



	

	

		

		
		
		


