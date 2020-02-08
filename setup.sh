#!/bin/sh

SCRIPT_DIR="$( cd "$( dirname "$0" )" >/dev/null 2>&1 && pwd )"
echo ${SCRIPT_DIR}

sudo apt update
sudo apt install \
     emacs \
     git \
     zsh \
     python3-pip \
     i3

i3_setup()
{
    I3_CONF_DIR="${HOME}/.config/i3/"
    mkdir -p ${I3_CONF_DIR}
    cp ${SCRIPT_DIR}/i3.config  ${I3_CONF_DIR}/config

    cp ${SCRIPT_DIR}/winmenu.py ${I3_CONF_DIR}
    sudo pip3 install --upgrade i3-py

    I3STATUS_CONF_DIR="${HOME}/.config/i3status/"
    mkdir -p ${I3STATUS_CONF_DIR}
    cp ${SCRIPT_DIR}/i3status.config ${I3STATUS_CONF_DIR}/config
}

zsh_setup()
{
    cp ${SCRIPT_DIR}/.zshrc ${HOME}
}

i3_setup
zsh_setup
