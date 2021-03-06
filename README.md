# Electric Sauna Heater Control

### Notes
### May 10th 2020 Starting a "Lockin Project" to report Sauna Status using a Google AIY Voice Kit V1
See https://github.com/grayerbeard/aiy

Aim is that the followinng voice commands will work to control Heater or report on the temperature

* "OK Google Report Sauna" >> reads out the sauna run time, Temperature, and Target Temperature.
* "OK Google Sauna Hotter" >> increases Target Temperature
* "OK Google Sauna Colder" >> decreases the Target Temperature
* "OK Google Sauna Off" >> turns off power and shuts down the R Pi.

### February 27th 2020
Note that in practice the settings of 70 and 80 results in the Sauna temperature staying in the range of about 70 to 75; a temperature range widely considered to be ideal.

#### December 14th to 16th
Tested Ok at higher temperature settings min 70 max 80 with min speed over 80 at 20%.
This was considered Ok although could be very slightly too high.
Minor debugs of the auto shutdown system (this shuts down the R Pi automatically when the stove is switched off at the switcg at the bottom of the stove).
That auto shutdown means dont need to shut down the R Pi via a terminal after usung sauna.

#### December 11th 2019 
Starting to adapt the fanshiim pwm code to control sauna heater
will need to use some of code from old sauna code see other repository
#### December 12th 2019
Tested and adjusted and worked OK, just need to test the auto shutdown.
The "auto shutdown" shuts down the R Pi Zero W when the sauna stove has been switched off so that although the Pi detects low temperature and switches on the heater at 100% the temperature keeps dropping.
#### December 13th 2019
Tested Auto shutdown now all working. Also raised temperatutre settings as 64/74 bit low changed to 70/80.

### Install

Clone or download into folder /home/pi/sauna.  Do this at the Terminal by typing this
'git clone https://github.com/grayerbeard/sauna.git /home/pi/sauna".

Install Tmux using 

'sudo apt-get install tmux'

Install  w1thermsensor (which is used to read in the temperature sensor(s)) using

'pip3 install w1thermsensor'

Install nginx server using

'sudo apt install nginx'

Then make the folder where the html files will be put writeable using

'sudo chown -R pi /var/www/html/'

Edit rc.local to autostart be calling the '/home/pi/sauna/tmux_start.sh' bash file.

enter:

'sudo nano /etc/rc.local'

add before the exit 0 this

'sudo -u pi bash /home/pi/sauna/tmux_start.sh &'  

then check rc.local works by going to /etc folder and entering './rc.local'

then when restart Pi the python program should start automatically.

Now you have several ways of starting the code
* go to /home/pi/sauna and enter 'python3 sauna.py'  (do that first to ensure all dependancies are installed)
* go to /home/pi/sauna and enter './tmux_start.sh' ((then view code output using 'tmux a')
* run by doing a reboot (then view code output using 'tmux a')

Code is now running in a tmux session and you can view it using 'tmux a -t sauna'
*reboot , code will also run in a tmux session.

### The headless chickens issue
So you can hardly sit at the sauna with a keyboard and monitor so the idea is to run the pi in what is called headless mode.
There is a lot of help on line about doing this e.g. [www.raspberrypi.org/documentation/configuration/wireless/headless.md](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md).  
The you can use various methods to monitor what is going on there are several ways:
* Log in using SSH and type 'tmux a' and then watch the program output
* Watch the HTML file at 'http://192.168.0.150/sauna_log.html' using your browser on your phone or other device, change that IP address to suite your R Pis IP address.
* Set up some other device such as a Google AIY Voice Kit to report on the Sauna Temperature.  (THIS IS TRHE CURRENT PROJECT)

### Hardware:
I do NOT recomend this mains voltage wiring for anyone without the necsessary electric safe knowledge; alternativly you could build and test all the low voltage parts and then ask a qualified person to install it. 

* Connect GT Pi PIO 18 to an SSR; if you Google for "Solid State Relay 240v". You will find a suitable item.  This is a solid state switch that you wire into the live wire powering the Sauna Stovve.
* The SSR input, from the R Pi that turns it on and off) is 3 to 32 volts DC usually 30ma which is too much for an R Pi to drive directly.  You need to buffer via a small relay or transister and drive with 5 volts via a resister. 
* Connect temperature probe. For these Google for "DS18b20 Waterproof Temperature Sensors" and you will find multiple suppliers.  Typically you can get 5 for around £10 but of course you only need one.  Position it behind the Temperature gauge as there I found I could drill the necessary small hole from the outside and it would be at about the right position and out of sighte.
* I put the R Pi and relay on the top of the sauna next to the existing JB for the electrical power to the stove.
* Our procedure is to turn on the supply at the wall, that powers up the R Pi and it boots up in a minute or two and the software starts automaticly bvia a TMUX command places in /etc/rc.local.
The config.cfg file needs to be edited with the code for your sensor.  Leave the config,cfg with my code in it , wrun the software and it will print out to the screen the code of any sensors it sees.
(This is done in the sensor.py module line 48.  If you look at that file you will see what is happening.) 
There are other ways toi find out what the temperature probes codes are but tis littlke dodge makes it much esier or run code and it will print out any codes oit finds, enter that in config.cfg for the "sensor4reading".
*
