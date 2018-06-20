from setuptools import setup
from beautifier import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='beautifier',
        version=__version__,
        description="Cleanup and beautifier emails, urls and patterns",
        url='https://github.com/labtocat/beautifier',
        author='Sachin Philip Mathew',
        author_email='me@imsach.in',
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        packages=['beautifier'],
        zip_safe=False,
        include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
