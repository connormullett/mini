
from setuptools import setup

setup(
    name='mini-notes',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'mini=mini:mini'
        ]
    }
)

