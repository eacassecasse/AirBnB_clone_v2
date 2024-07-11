#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static directory.
"""

import os
from datetime import datetime
from fabric.api import local

# Hosts IP and user of the web server web-01 and web-02
env.hosts = ["54.157.136.194", "100.25.134.41"]
env.user = "ubuntu"

def do_pack():
    """
    Create a tar gzipped archive of the directory web_static.

    Returns:
        str: Path to the created archive if successful, None otherwise.
    """
    # Get current UTC time
    dt = datetime.utcnow()

    # Define file name with timestamp
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                              dt.month,
                                                              dt.day,
                                                              dt.hour,
                                                              dt.minute,
                                                              dt.second)

    # Create 'versions' directory if not exists
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the tar gzipped archive
    command = "tar -cvzf {} web_static".format(file_name)
    if local(command).failed:
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
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        new_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        file_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, new_path)
        run("mkdir -p {}".format(file_path))
        run("tar -xzf {} -C {}".format(new_path, file_path))
        run("rm {}".format(new_path))
        run("mv -f {}web_static/* {}".format(file_path, file_path))
        run("rm -rf {}web_static".format(file_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(file_path))
        return True
    return False


def deploy():
    """
    Create and distribute an archive to a web server.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)


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

    if number == 0:
        number = 1

    # Sort the list of archives
    archives = sorted(os.listdir("versions"))
    archive_to_delete = archives[:-number]

    # Remove specified number of oldest archives
    for archive in archives_to_delete:
        local("rm ./versions/{}".format(archive))

    # Connect to the server and remove out-of-date archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        archives_to_delete = archives[:-number]

        for archive in archives_to_delete:
            run("rm -rf ./{}".format(archive))
