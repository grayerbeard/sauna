#!/bin/bash
cd /home/pi/fanshim
echo looking to kill any old tmux fanshim session
tmux kill-session -t sauna
echo now new tmux fanshim session 
tmux new-session -d -s sauna 'python3 sauna.py'

