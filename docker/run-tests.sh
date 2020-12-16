#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# runs the unittests
pip3 install pip --upgrade
pip3 install -e .[dev]
make nosetest

# do some cleanup
if [ -d "/repos/" ]; then
    rm -Rf /repos/
fi

mkdir /repos

# now we really create a repo here and add a package
# the gpg key is build into the docker image for testing purposes
simpleapt create-repo myrepo /repos --gpgkey AC46C6AAD5792E7E
simpleapt add-component myrepo test
simpleapt list-repos
cp /usr/local/src/vdt/simpleaptrepo/tests/testdata/*.deb /repos/myrepo/test
simpleapt update-repo myrepo test
simpleapt update-repo myrepo test --skip-signed
