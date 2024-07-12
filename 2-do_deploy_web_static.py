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


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.isfile(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    try:
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/{}".format(file))
        run("rm -rf {}{}/".format(path, name))
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(file, path, name))
        run("rm /tmp/{}".format(file))
        run("mv {}{}/web_static/* {}{}/".format(path, name, path, name))
        run("rm -rf {}{}/web_static".format(path, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, name))
        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
