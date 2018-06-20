from setuptools import setup
from beautifier import __version__

setup(name='beautifier',
      version=__version__,
      description="Cleanup and beautifier emails, urls and patterns",
      url='https://github.com/labtocat/beautifier',
      author='Sachin Philip Mathew',
      author_email='me@imsach.in',
      license='MIT',
      packages=['beautifier'],
      zip_safe=False,
      include_package_data=True
    )
