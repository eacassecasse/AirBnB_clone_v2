#!/usr/bin/python3
"""
Fabfile to delete out-of-date archives.
"""

import os
from fabric.api import env, local, run

# Define remote hosts
env.hosts = ["34.207.154.215", "18.210.33.217"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    # Ensure number is an integer
    number = int(number)

    # Sort the list of archives
    archives = sorted(os.listdir("versions"))

    # Remove specified number of oldest archives
    for _ in range(number):
        if archives:
            local("rm ./versions/{}".format(archives.pop(0)))

    # Connect to the server and remove out-of-date archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        for _ in range(number):
            if archives:
                run("rm -rf ./{}".format(archives.pop(0))))
