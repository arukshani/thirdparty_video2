#!/bin/bash

shopt -s extglob
cd /tmp/ruk/user-prof && sudo rm -rf !(*Default*)
cd /tmp/ruk/user-prof/Default && sudo rm -rf !(*Cookies*)
cd /users/rukshani/upload && sudo rm -rf *
pkill chrome
VAR="$(lsof -t -i:19282)"
if test -z "$VAR" 
then
      echo "\$VAR is empty"
else
      kill -9 $(lsof -t -i:19282)
fi
# kill -9 $(lsof -t -i:19282)