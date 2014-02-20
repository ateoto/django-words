#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

from words.tests import test_settings


if not settings.configured:
	settings.configure(**test_settings.__dict__)

def runtests(*test_args):
	if hasattr(django, 'setup'):
		django.setup()

	apps = sys.argv[1:] or ['words',]
	TestRunner = get_runner(settings)
	test_runner = TestRunner(verbosity=2, interactive=True)
	failures = test_runner.run_tests(apps)
	sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])