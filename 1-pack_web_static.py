#!/usr/bin/python3
"""
Fabfile to generate a .tgz archive from the contents of web_static directory.
"""

import os
from datetime import datetime
from fabric.api import local


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
