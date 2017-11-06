FROM jupyter/scipy-notebook

# From Jupyter Project <jupyter@googlegroups.com>
MAINTAINER Matthieu Boileau <matthieu.boileau@math.unistra.fr>

USER root

RUN apt-get update && apt-get -yq dist-upgrade \
 && apt-get install -yq --no-install-recommends \
    rsync \
    texlive-latex-recommended \
    texlive-fonts-recommended \
    python3-pip \
    zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN passwd -d $NB_USER && \
    adduser $NB_USER sudo

RUN pip3 install --upgrade pip && \
    pip3 install latex

# Switch back to fitzinger to avoid accidental container runs as root
USER $NB_USER
