=================
vdt.simpleaptrepo
=================

Simple command line tool to create apt repositories. This will work on debian and ubuntu.

Installation:
=============

First install from pypi:

.. code-block:: bash

    pip install vdt.simpleaptrepo
    
This tool is a wrapper for some debian specific packages, so you will need to install them first:

.. code-block:: bash

    apt-get install gnupg dpkg-sig apt-utils


To show which commands are available:
 
.. code-block:: bash
 
    simpleapt --help

Create a repository:
====================
First you need to create a gpg key to sign your packages with. This is not mandatory but highly recommended.

.. code-block:: bash

    simpleapt create-gpg-key
    
Copy and remember the key's hash. The output looks something like this:

.. code-block:: bash

    gpg: key 10FB8BDC marked as ultimately trusted
    
So copy the `10FB8BDC` hash, you will need it later.

Now create a repository:

.. code-block:: bash

    simpleapt create-repo myrepo /www/ --gpgkey 10FB8BDC
    
    Repository 'myrepo' created
    Now add a component with the 'add-component' command


Create a component:
===================

In one repository you have multiple components:

.. code-block:: bash

    simpleapt add-component myrepo test

You will see what you need to do now:

.. code-block:: bash

    Component 'test' created in repo 'myrepo'

    Now add some unsigned debian packages in the directory
    and run the 'update-repo' command (see the 'add packages' section below)

    Configure your webservice to set the www-root to /www/
    Add http://<hostname>/myrepo/test / to your sources.list
    
    Add the key on the host where you want to install the packages.
    (This is only needed once per repository)
    wget -qO - http://<hostname>/myrepo/test/keyfile | sudo apt-key add -

Add some more if you like:

.. code-block:: bash

    simpleapt add-component myrepo staging
    simpleapt add-component myrepo production

See that our repo is there:

.. code-block:: bash

    simpleapt list-repos
    
    myrepo (gpgkey: 10FB8BDC)
       test
       staging
       main

Add packages:
=============

Copy some debian package into a component's directory and update the repo:

.. code-block:: bash

    simpleapt update-repo myrepo test

    Exported key 10FB8BDC to /www/myrepo/test/keyfile

    Signed package /www/myrepo/test/my-package_0.0.1_all.deb
    Creates Packages
    Creates Packages.gz
    Create Release with key 10FB8BDC
    Create InRelease with key 10FB8BDC
    Create Releases.gpg with key 10FB8BDC

Now you can install these packages!


Useful URLS:
============

http://blog.packagecloud.io/eng/2014/10/28/howto-gpg-sign-verify-deb-packages-apt-repositories/

https://keyring.debian.org/creating-key.html

https://wiki.debian.org/SecureApt#How_apt_uses_Release.gpg

https://help.ubuntu.com/community/CreateAuthenticatedRepository

http://lists.gnupg.org/pipermail/gnupg-users/2004-May/022471.html
