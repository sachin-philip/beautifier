import re
import os

__version__ = "0.5.5"


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

    @property
    def is_free_email(self):
        free_domain_list = open(os.path.dirname(os.path.abspath(__file__)) + "/helpers/free_domain_list.txt")
        free_domains = free_domain_list.read().split('\n')
        return True if self.domain in free_domains else False


class Url(object):
    """docstring for Url"""

    def __init__(self, url):
        self._main_url = url
        self.cleanup = url.replace("\r\n", "").replace("\n", "").replace(
            "\r", "").replace('"', '').split('?auth')[0]
        self.parameters = None

    @property
    def param(self):
        """
        Returns params
        """
        try:
            self.parameters = self._main_url.split('?')[1]
            return self.parameters.split('&')
        except:
            return self.parameters

    @property
    def username(self):
        if 'linkedin.com' in self.cleanup:
            return self.cleanup.split("/")[-1]
        else:
            return {'msg': 'feature is currently available only with linkedin urls'}

    @property
    def domain(self):
        """
        Return domain from the url
        """
        remove_pac = self.cleanup.replace(
            "https://", "").replace("http://", "").replace("www.", "")
        try:
            return remove_pac.split('/')[0]
        except:
            return None
