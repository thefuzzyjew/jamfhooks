import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-jamf-webhooks',
    version = '0.1',
    packages = ['jamf_webhook_connector'],
    include_package_data = True,
    license = 'BSD License',
    description = 'A webhook connector for jamf',
    long_description = README,
    url = 'http://www.example.com/',
    author = 'Alex Snyder',
    author_email = 'asnyder@nfv.k12.ia.us',
    classifiers =[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
