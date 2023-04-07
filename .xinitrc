#!/bin/sh


/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

numlockx &

nitrogen --restore &

flameshot &

picom --no-fading-openclose &

ssh-agent qtile start
