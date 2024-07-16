#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static directory.
"""

import os
from datetime import datetime
from fabric.api import env, local, sudo

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

    # Local cleanup
    gotodir = 'cd versions && ls -t'
    print(f"Cleaning local archives, keeping {number-1} most recent.")
    local('{}'.format(gotodir))
    local('{} | tail -n +{} | xargs -r rm -rf'.format(gotodir, number))
    local('cd versions && ls -t')

    # Remote cleanup
    path = '/data/web_static/releases'
    print("Remote cleanup at {}, {} most recent only.".format(path, number-1))
    sudo('ls -t {}'.format(path))
    sudo('cd {} && ls -t | tail -n +{} | xargs -r rm -rf'.format(path, number))
    sudo('ls -t {}'.format(path))
