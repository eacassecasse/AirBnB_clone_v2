#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run

# Hosts IP and user of the web server web-01 and web-02
env.hosts = ["54.157.136.194", "100.25.134.41"]
env.user = "ubuntu"


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.

    Returns:
        str: Path to the created archive if successful, None otherwise.
    """
    # Generate a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the file name
    file_name = "versions/web_static_{}.tgz".format(timestamp)

    # Create 'versions' directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the tar gzipped archive
    command = "tar -cvzf {} web_static".format(file_name)
    result = local(command)

    if result.failed:
        return None

    return file_name
