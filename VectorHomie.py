#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import anki_vector

# Create a Robot object
robot = anki_vector.Robot()

# Connect to Vector Robot
robot.connect()

# Vector Drives Off Charger, Says Greeting, and Fist Bumps
with anki_vector.Robot() as robot:
    robot.behavior.drive_off_charger()
    robot.anim.play_animation_trigger('GreetAfterLongTime')
    robot.behavior.say_text("Hey Homie, can I get a fistbump?")
    robot.anim.play_animation('anim_fistbump_requestonce_02')
    robot.behavior.say_text("Thanks, Homie, stay cool!")
      
# Disconnect from Vector Robot
robot.disconnect()
