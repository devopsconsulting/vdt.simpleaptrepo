import ConfigParser
import os

import click

HOME = os.path.expanduser("~")


class Config(object):
    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.path = os.path.join(HOME, ".simpleapt.ini")
        self.config.read(self.path)
        self.sections = self.config.sections()

    def save(self):
        self.config.write(open(self.path, "w"))

    def add_repo(self, name, path, gpgkey=""):
        if not self.config.has_section(name):
            self.config.add_section(name)
        self.config.set(name, 'path', path)
        if gpgkey:
            self.config.set(name, 'gpgkey', gpgkey)
        self.save()

    def get_repo(self, name):
        if not self.config.has_section(name):
            raise click.UsageError("'%s' does not exist!" % name)
        return dict(self.config.items(name))
