#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static directory.
"""

import os
from datetime import datetime
from fabric.api import local

# Hosts IP and user of the web server web-01 and web-02
env.hosts = ["54.157.136.194", "100.25.134.41"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    sudo('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
