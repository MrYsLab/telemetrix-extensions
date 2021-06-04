#!/usr/bin/env python3

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='telemetrix',
    packages=['telemetrix_pca9685', ],
    install_requires=['telemetrix', 'telemetrix-aio', 'telemetrix-rpi-pico',
                      'tmx-pico-aio'],

    version='0.1',
    description="i2c Extensions For Telemetrix Clients",
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    url='https://github.com/MrYsLab/telemetrix-extensions',
    download_url='https://github.com/MrYsLab/telemetrix-extensions',
    keywords=['telemetrix', 'Arduino', 'Raspberry Pi Pico', 'Protocol', 'Python'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

