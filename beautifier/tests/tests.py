import unittest
from beautifier import Email, Url

class EmailMethods(unittest.TestCase):
    '''
    Tests for methods of email parsing

    '''
    def __init__(self, *args, **kwargs):
        super(EmailMethods, self).__init__(*args, **kwargs)
        self.email = Email('me@imsach.in')
        
    def test_is_valid(self):
        '''
        Tests if the domain is vaild or not
        '''
        self.assertEqual(self.email.is_valid, True)

    def test_is_free_email(self):
        '''
        Check if its free email or a company email
        '''
        self.assertEqual(self.email.is_free_email, False)
   
    def test_email_domain(self):
        '''
        Checks if it returns proper domain of the given email
        '''
        self.assertEqual(self.email.domain, 'imsach.in')

    def test_email_username(self):
        '''
        Checks if it returns proper username of the given email
        '''
        self.assertEqual(self.email.username, 'me')


class UrlMethods(unittest.TestCase):
    '''
    Tests for methods of url parsing

    '''
    def __init__(self, *args, **kwargs):
        super(UrlMethods, self).__init__(*args, **kwargs)
        self.url = Url('https://in.linkedin.com/in/sachinphilip?authtoken=887nasdadasd6hasdtg21&secret=98jy766yhhuhnjk')

    def test_cleanup(self):
        '''
        Checks the url is properly cleaned
        '''
        self.assertEqual(self.url.cleanup, 'https://in.linkedin.com/in/sachinphilip')

    def test_url_domain(self):
        '''
        Checks the url is domain returned
        '''
        self.assertEqual(self.url.domain, 'in.linkedin.com')


if __name__ == '__main__':
    unittest.main()