Beautifier
------

Simple library to cleanup and prettify url patterns, domains and so on.
Library helps to clean unicodes, special charecters and unnessesary 
redirection patterns from the urls and gives you clean date.
 
 
## Documentation

### Installation

```bash
pip install beautifier
```

## Basic Usages

#### Email Function

EMAIL cleanup API's

```python
from beautifier import Email
email = Email('me@imsach.in')

>>> email.domain
'imsach.in'

>>> email.username
 'me'

>>> email.is_free_email
 False
``` 

#### Url Function

URL cleanup API's


```python
from beautifier import Url
url = Url('https://in.linkedin.com/in/sachinphilip?authtoken=887nasdadasd6hasdtg21&secret=98jy766yhhuhnjk')

>>> url.cleanup
'https://in.linkedin.com/in/sachinphilip'

>>> url.domain
 'in.linkedin.com'

>>> url.param
 ['authtoken': '887nasdadasd6hasdtg21',
  'secret': '98jy766yhhuhnjk' ]
``` 


