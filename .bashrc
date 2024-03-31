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

HISTSIZE=10000
HISTFILESIZE=10000

# export PATH=$PATH:~/.bin

export SYSTEMD_EDITOR=vim

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

eval "$(pyenv init -)"
. "$HOME/.cargo/env"