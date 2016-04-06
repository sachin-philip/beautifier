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


### Basic Usage

```python
from beautifier import Beautifier
beautifier = Beautifier()
```

**operations:** type of operations - email to domain, url to domain, url beautifier


## Specific Functions

*** email to domain ***

```python
beautifier.emailToDomain(email="me@imsach.in")
```
OUT : 'imsach.in' 

*** email to domain ***

```python
beautifier.domainCleanup(url="https://www.imsach.in")
```
OUT : 'imsach.in' 

*** email to domain ***

```python
beautifier.cleanUrl(url="https://imsach.in/?authtoken=887nasdadasd6hasdtg21&secret=98jy766yhhuhnjk")
```
OUT: 'https://imsach.in/'


