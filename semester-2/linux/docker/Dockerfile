ARG VERSION=lunar
ARG NJS_VER=20

FROM ubuntu:${VERSION} AS builder

# Switch the source
RUN sed -i 's/ports.ubuntu.com/ftp.ubuntu-tw.org\/mirror/g' /etc/apt/sources.list

# Install and upgrade packages
RUN apt update && apt upgrade

RUN apt install -y \
            bash \
            fish \
            sudo \
            neovim \
            curl \
            wget \
            git \
            build-essential \
            python3 \
            python3-pip

# Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_${NJS_VER}.x | sudo -E bash - \
        && sudo apt install -y nodejs npm

## corepack
RUN npm install -g corepack && \
    corepack enable && \
    corepack prepare --all

# Create a new user
RUN useradd -m -s /bin/bash -G sudo pan93412 \
        && echo "pan93412:p934" | chpasswd

# Switch to user
USER pan93412

# Install oh-my-fish
WORKDIR /tmp
RUN curl -o installer https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install \
        && fish installer --noninteractive --yes \
        && rm installer

# Set the default shell
WORKDIR /home/pan93412
CMD ["/bin/fish"]
