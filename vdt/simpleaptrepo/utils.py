import os
import platform
import subprocess
import sys


def repo_root(path):
    """
    Returns the root directory from a repo/component

    >>> repo_root("/www/myrepo/test")
    '/www'

    >>> repo_root("/home/user/myrepo/staging")
    '/home/user'

    >>> repo_root("/myrepo/staging")
    '/'

    """
    return os.path.split(os.path.split(path)[0])[0]


def write_to_stdout(message):
    unbuffered_output = os.fdopen(sys.stdout.fileno(), 'w', 0)
    unbuffered_output.write("%s\n" % message)


def platform_is_debian():
    current_platform = platform.dist()[0].lower()
    return current_platform in ["ubuntu", "debian"]


def check_dependencies(output_command):
    try:
        subprocess.check_output("/usr/bin/gpg --help")
    except subprocess.CalledProcessError as e:
        output_command("gpg is required and not installed or raises an error")
        output_command(e)
        output_command("Please run 'apt-get install gnupg'")

    try:
        subprocess.check_output("/usr/bin/dpkg-sig --help")
    except subprocess.CalledProcessError as e:
        output_command("gpg is required and not installed or raises an error")
        output_command(e)
        output_command("Please run 'apt-get install dpkg-sig'")
    try:
        subprocess.check_output("/usr/bin/apt-ftparchive --help")
    except subprocess.CalledProcessError as e:
        output_command(
            "apt-ftparchive is required and not installed or raises an error")
        output_command(e)
        output_command("Please run 'apt-get install apt-utils'")
