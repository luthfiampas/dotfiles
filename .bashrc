#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

eval "$(starship init bash)"

export LS_COLORS+=':tw=01;34:ow=01;34:st=01;34'

source /usr/share/fzf/key-bindings.bash
source /usr/share/fzf/completion.bash

# export PATH=$PATH:~/.bin

export SYSTEMD_EDITOR=vim
