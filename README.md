# sauna

### Notes
December 11th 2019 
Starting to adapt the fanshiim pwm code to control sauna heater
will need to use some of code from old sauna code see other repository
December 12th 2019
Tested and adjusted and worked OK, just need to test the auto shutdown.
The "auto shutdown" shuts down the R Pi Zero W when the sauna stove has been switched off so that although the Pi detects low temperature and switches on the heater at 100% the temperature keeps dropping.
December 13th 2019
Tested Auto shutdown now all working. Also raised temperatutre settings as 64/74 bit low changed to 70/80.

### Install
clone or download into folder /home/pi/sauna
Install Tmux using sudo apt-get install tmux
Edit rc.local to autostart be calling the tmux_start.sh bash file.
  Add "sudo -u pi bash /home/pi/sauna/tmux_start.sh &" to jsut before the "exit 0" 
then when restart Pi the python program should start automatically
run by doing a reboot or by going to /sauna and entering ./tmux_start.sh.

Hardware:
Connect GPIO 18 via a relay or transistoir to drive input to SCR switch.
connect temperature probe.
find out the temperature probes code or run code and it will print out any codes oit finds, enter that in config.cfg for the "sensor4reading".
