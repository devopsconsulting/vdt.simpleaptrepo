import os

import click

from vdt.simpleaptrepo.config import Config


HOME = os.path.expanduser("~")


@click.group()
def cli():
    pass


@cli.command()
@click.argument('name')
@click.argument('path', default=".")
@click.option('--gpgkey', help='The GPG key to sign the packages with')
def createrepo(name, path, gpgkey=""):
    """Creates a repository"""
    if not os.path.exists(path):
        raise click.BadParameter("Path does not exists!")

    repo_dir = os.path.abspath(os.path.join(path, name))
    if os.path.exists(repo_dir):
        raise click.BadParameter("Directory %s already exists!" % repo_dir)

    os.mkdir(repo_dir)

    config = Config()
    config.add_repo(name, repo_dir, gpgkey)
    click.echo("Repository '%s' created" % name)
    click.echo("Now add a component with the 'addcomponent' command")


@cli.command()
@click.argument('name')
@click.argument('component', default="main")
def addcomponent(name, component):
    """Creates a component (ie, 'main', 'production')"""
    config = Config()
    repo_cfg = config.get_repo(name)
    path = os.path.join(repo_cfg['path'], component)
    if os.path.exists(path):
        raise click.BadParameter("Directory %s already exists!" % path)

    os.mkdir(path)

    click.echo("Component '%s' created in repo '%s'" % (component, name))


@cli.command()
@click.argument('name')
@click.argument('component', default="main")
def updaterepo(name, component):
    """Updates a repo by scanning the debian packages
    and add the index files"""
    click.echo("do the magic here")


@cli.command()
def listrepos():
    """List currently configured repos"""
    config = Config()
    for section in config.sections:
        click.echo(section)


def main():
    cli()


if __name__ == "__main__":
    main()
