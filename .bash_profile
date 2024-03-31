#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc


# *****FOR SWAY*****
#export QT_SCREEN_SCALE_FACTORS="1;1"

#export QT_QPA_PLATFORM=wayland
#export MOZ_ENABLE_WAYLAND=1
#export AVALONIA_GLOBAL_SCALE_FACTOR=1

#export XDG_CURRENT_DESKTOP=sway
#export XDG_SESSION_DESKTOP=sway # systemd
#export XDG_SESSION_TYPE=wayland # xdg/systemd
# *****FOR SWAY*****

export PATH=$PATH:$HOME/.bin:$HOME/.dotnet/tools
. "$HOME/.cargo/env"