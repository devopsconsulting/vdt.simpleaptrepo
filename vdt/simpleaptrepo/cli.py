import os
import subprocess

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
    config = Config()
    repo_cfg = config.get_repo(name)
    path = os.path.join(repo_cfg.get('path'), component)
    if not os.path.exists(path):
        raise click.BadParameter("Component '%s' does not exist!" % component)
    if repo_cfg.get('gpgkey'):    
        subprocess.check_output("/usr/bin/gpg --output %s --armor --export %s" % (os.path.join(path, 'keyfile'), repo_cfg.get('gpgkey')), shell=True)
        for x in os.listdir(path):
            if x.endswith('.deb'):  # use glob!
                deb_file = os.path.join(path, x)
                click.echo("signed package %s" % x)
                subprocess.check_output("/usr/bin/dpkg-sig -k %s --sign builder %s" % (repo_cfg.get('gpgkey'), deb_file), shell=True)

    subprocess.check_output("/usr/bin/apt-ftparchive packages . > Packages", shell=True, cwd=path)
    subprocess.check_output("/bin/gzip -c Packages > Packages.gz", shell=True, cwd=path)

    if repo_cfg.get('gpgkey'):    
        subprocess.check_output("/usr/bin/apt-ftparchive release . > Release", shell=True, cwd=path)             
        subprocess.check_output("/usr/bin/gpg -u 0x%s --clearsign -o InRelease Release" % repo_cfg.get('gpgkey'), shell=True, cwd=path)
        subprocess.check_output("/usr/bin/gpg -u 0x%s -abs -o Release.gpg Release" % repo_cfg.get('gpgkey'), shell=True, cwd=path)             

@cli.command()
def listrepos():
    """List currently configured repos"""
    config = Config()
    for section in config.sections:  # tree.walk!!
        repo_cfg = config.get_repo(section)
        if repo_cfg.get('gpgkey'):
            section = "%s (gpgkey: %s)" % (section, repo_cfg.get('gpgkey'))
        click.echo(section)
        for component in os.listdir(repo_cfg.get('path')):
            click.echo("   %s" % component)


def main():
    cli()


if __name__ == "__main__":
    main()
