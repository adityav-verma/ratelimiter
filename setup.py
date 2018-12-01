from setuptools import setup


setup(
    name='ratelimiter',
    version='0.1',
    maintainer='Aditya Verma',
    maintainer_email='aditya.verma.connect@gmail.com',
    packages=['ratelimiter'],
    install_requires=['redis>3,<3.1']
)
