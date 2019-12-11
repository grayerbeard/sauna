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

# title           :pwm.py
# description     :pwm control for Sauna Stove
# author          :David Torrens
# start date      :2019 12 12
# version         :0.1
# python_version  :3

import RPi.GPIO as GPIO

class class_cpu:  # For monitoring R Pi 4 Cpu 
	def __init__(self,config):				
		self.pwm_speed  = 0
		self.pwm_freq = 2
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(config.sauna_GPIO_port, GPIO.OUT)
		self.pwm_out = GPIO.PWM(config.sauna_GPIO_port,1)
		self.pwm_out.start(0)
		self.pwm_out.ChangeFrequency(self.pwm_freq)
		self.pwm_out.ChangeDutyCycle(self.pwm_speed)

	def set_pwm_control_heater(self,freq,speed):
		self.pwm_speed  = speed
		self.pwm_freq = freq

	def control_heater(self):
		self.pwm_out.ChangeFrequency(self.pwm_freq)
		self.pwm_out.ChangeDutyCycle(self.pwm_speed)
