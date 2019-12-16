#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This file is part of pwm_fanshim.
# Copyright (C) 2015 Ivmech Mechatronics Ltd. <bilgi@ivmech.com>
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# title           :sensors_test.py
# description     :get temperatures that simulate heat up and cool down of a sauna
# author          :David Torrens
# start date      :2019 12 12
# version         :0.1
# python_version  :3

# Standard library imports
# None

# Third party imports
from w1thermsensor import W1ThermSensor

# Local application imports
from utility import pr,make_time_text,send_by_ftp

class class_my_sensors:
	def __init__(self,config):
		self.sensor4readings = config.sensor4readings
    
    # set up a dummy value starting at typical ambient temperature
    self.test_temp = 25
    self.going_up = True
    self.turn_around = config.max_temp + 2

	def get_temp(self,sensor4readings):
		# gets the temperature of the sensor for readings
    
		# Comment out all the normal code
    #found = False
		#sensors = W1ThermSensor.get_available_sensors()
		#for individual_sensor in W1ThermSensor.get_available_sensors():
		#	if sensor4readings == individual_sensor.id:
		#		temp = individual_sensor.get_temperature()
		#		found = True
		#	else:
		#		print("Found other sensor code : ",individual_sensor.id, "  please correct entry in config.cfg")
		#if found:
		#	return temp
		#else:
		#	return -100
    
    if self.going_up:
      self.test_temp += 0.5
      if if self.test_temp > self.turn_around:
        self.going_up = False
    else:
      self.test_temp -= 0.5
    
    return self.test_temp
