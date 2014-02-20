#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'words.tests.persistent_settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)











    """
    if sys.argv[1] == 'test':
        from django.test.runner import DiscoverRunner
        

        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
            'words.tests.test_settings')

        test_runner = DiscoverRunner(verbosity=1)
        failures = test_runner.run_tests(['words',])
        if failures:
            sys.exit(failures)

    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                            'words.tests.persistent_settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
"""