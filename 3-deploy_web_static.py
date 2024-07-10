#!/usr/bin/python3
"""
Fabfile to create and distribute an archive to a web server.
"""

import os.path
from datetime import datetime
from fabric.api import env, local, put, run

# Define remote hosts
env.hosts = ["34.207.154.215", "18.210.33.217"]


def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.

    Returns:
        str: Path to the created archive on success, None on failure.
    """
    # Generate timestamp for file name
    dt = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)
    # Create 'versions' directory if it doesn't exist
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    # Create the tar.gz archive
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Check if the archive file exists
    if os.path.isfile(archive_path) is False:
        return False
    # Extract file name and name of the directory
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Transfer archive to the server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    # Remove existing directory
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Create new directory
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Unpack archive into the new directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False
    # Remove the archive file from the server
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    # Move the content from the unpacked directory to the new one
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    # Remove the now-empty web_static directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    # Delete the symbolic link
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    # Create a new symbolic link
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Create and distribute an archive to a web server.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    # Create the archive
    file = do_pack()
    if file is None:
        return False
    # Deploy the archive
    return do_deploy(file)
