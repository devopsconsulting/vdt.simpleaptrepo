#!/bin/bash
# runs the unittests
make test
# do some cleanup
if [ -d "/repos/" ]; then
      rm -Rf /repos/
fi

mkdir /repos
# # now we really create a repo here and add a package
# # the gpg key is build into the docker image for testing purposes
simpleapt create-repo myrepo /repos --gpgkey D2E0953C
simpleapt add-component myrepo test
simpleapt list-repos
cp /usr/local/src/vdt/simpleaptrepo/tests/testdata/*.deb /repos/myrepo/test
simpleapt update-repo myrepo test
simpleapt update-repo myrepo test --skip-signed