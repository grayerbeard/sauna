#!/bin/bash
cd /home/pi/fanshim
echo looking to kill any old tmux sauna session
tmux kill-session -t sauna
echo now new tmux sauna session 
tmux new-session -d -s sauna 'python3 sauna.py'

