"""
A standalone test runner script, since we don't ship a Django manage.py file.

"""

# SPDX-License-Identifier: BSD-3-Clause

from django.core.management import execute_from_command_line


def run_tests():
    """
    Run the tests, using Django's test runner.

    """
    execute_from_command_line(["runtests.py", "test", "--verbosity", "2"])


if __name__ == "__main__":
    run_tests()
