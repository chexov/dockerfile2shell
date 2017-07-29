#
FROM ubuntu:xenial

MAINTAINER anton <anton@videogorillas.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common net-tools iputils-ping apt-transport-https && \
    rm -rf /var/lib/apt/lists/*
# enable multiverse packages
RUN apt-add-repository multiverse

# nodejs
COPY nodesource.list /etc/apt/sources.list.d/nodesource.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1655A0AB68576280
RUN apt-get update && \
    apt-get install -y --no-install-recommends nodejs && \
    rm -rf /var/lib/apt/lists/*

# java8
RUN apt-add-repository -y ppa:webupd8team/java
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends oracle-java8-set-default && \
    rm -rf /var/lib/apt/lists/*

# FFmpeg
RUN apt-add-repository -y ppa:sunab/kdenlive-release
RUN mkdir /opt/vg/
WORKDIR /opt/vg/
COPY ffmpeg3-build.sh /opt/vg/ffmpeg3-build.sh
RUN sh -xue ./ffmpeg3-build.sh && rm -rf /var/lib/apt/lists/* /tmp/*

# Redis
RUN apt-add-repository -y ppa:chris-lea/redis-server
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends redis-server && \
    rm -rf /var/lib/apt/lists/*

# Utilities
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    nginx letsencrypt apache2-utils pv sysstat vim nfs-common mediainfo vim unzip screen lsof runit && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

