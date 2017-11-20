FROM ubuntu
MAINTAINER Martijn Jacobs <martijn@devopsconsulting.nl>

ENV DEBIAN_FRONTEND noninteractive

# install the debian related packages for this tool + python pip
RUN apt-get update && apt-get install python-pip gnupg dpkg-sig apt-utils --yes

# Make sure you mounted the source coude in /usr/local/src
WORKDIR /usr/local/src/

ENTRYPOINT ["make", "test"]