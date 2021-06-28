from setuptools import setup
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name='ghstats',
    version='1.2.0',
    packages=['ghstats'],
    description='GitHub Release download count and other statistics.',
    long_description=readme,
    author='Alexander Gorishnyak',
    author_email='kefir500@gmail.com',
    license='MIT',
    url='https://github.com/kefir500/ghstats',
    keywords='github release download count stats statistics',
    entry_points={
        'console_scripts': [
            'ghstats = ghstats.ghstats:main_cli'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ]
)
