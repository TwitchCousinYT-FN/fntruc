from setuptools import setup,find_packages

setup(
    name='FNTwitchSetup',
    version='0.0.1',
    description='Private module',
    url='',
    author_email='',
    packages=find_packages(),
    install_requires=['fortnitepy==1.7.1','sanic','requests','aiofiles']
)
