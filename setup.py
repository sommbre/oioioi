# -*- coding: utf-8 -*-

from __future__ import print_function

try:
    from setuptools import find_packages, setup
except ImportError:
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

if os.getuid() == 0:  # root
    print("ERROR: This setup.py cannot be run as root.", file=sys.stderr)
    print("ERROR: If you want to proceed anyway, hunt this", file=sys.stderr)
    print("ERROR: message and edit the source at your own risk.", file=sys.stderr)
    sys.exit(2)

# All modules in the newest versions at the time of upgrade to Django 4.2
# unless specified otherwise.
requirements = [
    "Django>=4.2.2,<4.3",
    "pytz>=2023.3,<2023.4",
    "SQLAlchemy<2.0",
    "beautifulsoup4>=4.12.2,<4.13",
    "PyYAML>=6.0,<6.1",
    "python-dateutil>=2.8.2,<2.9",
    "django-two-factor-auth>=1.15.2,<1.16",
    "django-formtools>=2.4.1,<2.5",
    "django-registration-redux>=2.12,<2.13",
    "Celery==4.4.7",    # 5.0 is breaking
    "coreapi>=2.3.3,<2.4",
    "dj-pagination>=2.5.0,<2.6",
    "django-compressor>=4.3.1,<4.4",
    "Pygments>=2.15.1,<2.16",
    "django-libsass>=0.9,<0.10",
    "django-debug-toolbar>=4.1.0,<4.2",
    "django-extensions>=3.2.3,<3.3",
    "djangorestframework>=3.14.0,<3.15",
    "Werkzeug>=2.3.5,<2.4",
    "pytest>=7.3.1,<7.4",
    "pytest-cov>=4.1.0,<4.2",
    "pytest-django>=4.5.2,<4.6",
    "pytest-html>=3.2.0,<3.3",
    "pytest-metadata>=3.0.0,<3.1",
    "pytest-xdist>=3.3.1,<3.4",
    "requests>=2.31.0,<2.32",
    "fpdf>=1.7.2,<1.8",
    "unicodecsv>=0.14.1,<0.15",
    "shortuuid>=1.0.11,<1.1",
    "dnslib>=0.9.23,<0.10",
    "bleach>=6.0.0,<6.1",
    "chardet>=5.1.0,<5.2",
    "django-gravatar2>=1.4.4,<1.5",
    "django-mptt>=0.14.0,<0.15",
    "mistune<2.0",   # 2.0 is breaking
    "pika>=1.3.2,<1.4",
    "raven>=6.10.0,<6.11",
    "Unidecode>=1.3.6,<1.4",
    "sentry-sdk>=1.25.1,<1.26",
    "fontawesomefree>=6.4.0,<6.5",
    # A library allowing to nest inlines in django admin.
    # Used in quizzes module for adding new quizzes.
    "django-nested-admin>=4.0.2,<4.1",
    # SIO2 dependencies:
    "filetracker>=2.1.5,<3.0",
    "django-simple-captcha>=0.5.16,<=0.5.18",
    "phonenumbers>=8.13.13,<8.14",
    "pdfminer.six==20221105",
    # https://stackoverflow.com/questions/73929564/entrypoints-object-has-no-attribute-get-digital-ocean
    "importlib-metadata<5.0",
    "supervisor<4.3",  # previously http://github.com/Supervisor/supervisor/zipball/master#egg=supervisor==4.0.0.dev0
    "django-supervisor@git+https://github.com/sio2project/django-supervisor#egg=django-supervisor",  # previously http://github.com/badochov/djsupervisor/zipball/master#egg=djsupervisor==0.4.0
]

setup(
    name='oioioi',
    version='0.2.0.dev',
    description='The web frontend of the SIO2 Project contesting system',
    author='The SIO2 Team',
    author_email='sio2@sio2project.mimuw.edu.pl',
    url='http://sio2project.mimuw.edu.pl',
    install_requires=requirements,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='oioioi.runtests.runtests',
    entry_points={
        'console_scripts': [
            'oioioi-create-config = oioioi.deployment.create_config:main',
        ],
    },
)
