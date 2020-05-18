# ~/.bashrc: executed by bash(1) for non-login shells.

#Colours

reset=$(tput sgr0)
bold=$(tput bold)
black=$(tput setaf 0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
blue=$(tput setaf 4)
magenta=$(tput setaf 5)
cyan=$(tput setaf 6)
white=$(tput setaf 7)

user_color=$green

[ "$UID" -eq 0 ] && { user_color=$green; }

PS1="\[$reset\][\[$cyan\]\A\[$reset\]]\[$user_color\]\u@\h\
\[$white\]:\[$reset\] "


eval "`dircolors`"



alias ll='ls $LS_OPTIONS -l'
alias l='ls $LS_OPTIONS -lA'
alias ls="ls --color=auto"

