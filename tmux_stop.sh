#!/bin/bash
cd /home/pi/sauna
echo looking to kill any old tmux sauna session
tmux kill-session -t sauna
