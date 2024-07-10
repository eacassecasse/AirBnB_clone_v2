#!/usr/bin/python3
"""
Fabfile to distribute an archive to a web server.
"""

import os
from fabric.api import env, put, run

# TODO: Change the hosts IP to my servers
env.hosts = ["34.207.154.215", "18.210.33.217"]


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Check if the archive file exists
    if not os.path.isfile(archive_path):
        return False

    # Extract file and directory names
    file_name = os.path.basename(archive_path)
    name = os.path.splitext(file_name)[0]

    # Transfer archive to remote server
    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False

    # Create directory for new release
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False

    # Unpack the archive
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
                   format(file_name, name)).failed:
        return False

    # Delete the archive file
    if run("rm /tmp/{}".format(file_name)).failed:
        return False

    # Move files to proper location
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed:
        return False

    # Remove redundant directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False

    # Update symbolic link
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
                   format(name)).failed:
        return False

    return True
