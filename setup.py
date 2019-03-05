import sys
from setuptools import setup

if sys.version_info < (3, 5):
    raise RuntimeError("aiojobs requires Python 3.5+")

setup(
    name='aiojobs',
    version='0.2.2',
    author='Andrew Svetlov',
    author_email='andrew.svetlov@gmail.com',
    license='Apache 2',
    python_requires='>=3.5',
    install_requires=[
        'aiohttp>=2.3.0',
        'async-timeout<4.0,>=3.0',
        'idna-ssl>=1.0',
        'chardet<4.0,>=2.0',
        'typing-extensions>=3.6.5',
        'yarl<2.0,>=1.0',
        'attrs>=17.3.0',
        'multidict<5.0,>=4.0',
        'idna>=2.0'],
    description='Jobs scheduler for managing background task (asyncio)',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: AsyncIO',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ],
    url='https://github.com/aio-libs/aiojobs',
    packages=['aiojobs']
)
