import os
import platform
import sys

unbuffered_output = os.fdopen(sys.stdout.fileno(), 'w', 0)


def write_to_stdout(message):
    unbuffered_output.write("%s\n" % message)


def platform_is_debian():
    current_platform = platform.dist()[0].lower()
    return current_platform in ["ubuntu", "debian"]
