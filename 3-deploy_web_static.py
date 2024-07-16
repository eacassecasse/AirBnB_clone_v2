#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers.
"""

from os.path import exists
from datetime import datetime
from fabric.api import env, local, put, sudo

# Hosts IP and user of the web server web-01 and web-02
env.hosts = ["54.157.136.194", "100.25.134.41"]


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


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}{}/'.format(path, no_ext))
        sudo('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        sudo('rm /tmp/{}'.format(file_n))
        sudo('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        sudo('rm -rf {}{}/web_static'.format(path, no_ext))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    """Creates and distributes an archive to web servers"""
    try:
        file_path = do_pack()
        return do_deploy(file_path)
    except:
        return False
