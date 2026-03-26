#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Connect to a PI stage using the E873 controller and the Q-545.140 translation stages

using Physik Instrumente (PI) GmbH & Co. KG
sc_hardware.physikInstrumente.E873.py

Alistair Boettiger, April 2019

V1.1
Functional connection to x-y axes of PI piezo stage
V1.2
Functional connection to both xy axes as a stage and z-axis as a separate z-stage

Notes: 
This module requires the PIPython library that ships with the PI controllers.
It also requires the path to this library to be added to the python path (see below).
There is probably a more elegant way to do this. 
"""


from __future__ import print_function

# Update the path to the PIPython Library: 
#
# Note: This might be better done by creating a xyz.pth module in the Python
#       library folder?
# 
import sys

from copy import deepcopy

import storm_control.sc_library.parameters as params

from pipython import GCSDevice, pitools

CONTROLLERNAME = 'E-816'  # 'C-884' will also work
STAGES = ['P-726.1CD']  #, 'Q-545.140', .1CD
REFMODES = 'FRF' # ['FNL', 'FRF']



class piE625(object):

    ## __init__
    #
    # Connect to the PI E873 stage.
    #
    #
    def __init__(self, serialnum = '14240'):   # should become a parameter, see other stages
        print(serialnum)
    
        # Connect to the PI E873 stage.
        # with GCSDevice(CONTROLLERNAME) as pidevice:    
        pidevice = GCSDevice(CONTROLLERNAME) 
        pidevice.ConnectUSB(serialnum = '14240') #   pidevice.ConnectUSB(serialnum='119006811')
        print('connected: {}'.format(pidevice.qIDN().strip()))

        # Show the version info which is helpful for PI support when there
        # are any issues.

        if pidevice.HasqVER():
            print('version info:\n{}'.format(pidevice.qVER().strip()))

        # In the module pipython.pitools there are some helper
        # functions to make using a PI device more convenient. The "startup"
        # function will initialize your system. There are controllers that
        # cannot discover the connected stages hence we set them with the
        # "stages" argument. The desired referencing method (see controller
        # user manual) is passed as "refmode" argument. All connected axes
        # will be stopped if they are moving and their servo will be enabled.

        print('initialize connected stages...')
        pitools.startup(pidevice) #, stages=STAGES , refmodes=REFMODES
        # Now we query the allowed motion range and current position of all
        # connected stages. GCS commands often return an (ordered) dictionary
        # with axes/channels as "keys" and the according values as "values".

        self.pidevice = pidevice
        
        self.wait = 1 # move commands wait for motion to stop
        self.unit_to_um = 100.0 # needs calibration
        self.um_to_unit = 1.0/self.unit_to_um


        # Connect to the stage.
        self.good = 1

        # get min and max range
        # self.rangemin = pidevice.qTMN("A")
        # self.rangemax = pidevice.qTMX("A")
        self.rangemin = 10
        self.rangemax = 80
        self.curpos = pidevice.qPOS("A")
        print(self.curpos)
        self.zMoveTo(40)
        

    ## getStatus
    #
    # @return True/False if we are actually connected to the stage.
    #
    def getStatus(self):
        return self.good

    ## goRelative
    #
    # @param dx Amount to displace the stage in x in um.
    # @param dy Amount to displace the stage in y in um.
    #

    def goRelative(self, dx):
        print('go rel command for ' + str(dx))
        if self.good:
            # self.jog(0.0,0.0)
            x0 = self.pidevice.qPOS("A")["A"]
            X = x0 - dx
            self.zMoveTo(X)


            
            
    ## position
    #
    # @return [stage x (um), stage y (um), stage z (um)]
    #
    def position(self):
        if self.good:
            x0 = self.pidevice.qPOS(1)[1]  # query single axis
            y0 = self.pidevice.qPOS(2)[2]  # query single axis
            return {"x" : x0,
                "y" : y0}

            
     
    def zMoveTo(self, z):
        """
        Move the z stage to the specified position (in microns).
        """
        if self.good:
            # Z = z * self.um_to_unit
            Z = z
            # print(Z)
            if Z > 15 and Z < 70:
                # print('moving ------------------------------------')
                self.pidevice.MOV("A", Z)
            else:
                print('requested move outside max range! .')
        

    def zPosition(self):
        """
        Query for current z position in microns.
        """
        if self.good:
            z0 = self.pidevice.qPOS("A")["A"]  # query single axis
            # print(z0)
            return {"z" : z0}

    def zSetVelocity(self, z_vel):
        pass
        
    def zZero(self):
        pass
        # if self.good:
        #     pitools._ref_with_pos(self, self.pidevice.axes([2])) # added axes [0,1], not sure this ever worked anyway

    ## jog
    #
    # @param x_speed Speed to jog the stage in x in um/s.
    # @param y_speed Speed to jog the stage in y in um/s.
    #
    def jog(self, x_speed, y_speed):
        pass
        # figure out how to do something here
        # if self.good:
        #     c_xs = c_double(x_speed * self.um_to_unit)
        #     c_ys = c_double(y_speed * self.um_to_unit)
        #     c_zr = c_double(0.0)
        #     tango.LSX_SetDigJoySpeed(self.LSID, c_xs, c_ys, c_zr, c_zr)

    ## joystickOnOff
    #
    # @param on True/False enable/disable the joystick.
    #
    def joystickOnOff(self, on):
        pass
        # No joystick used

    ## lockout
    #
    # Calls joystickOnOff.
    #
    # @param flag True/False.
    #
    def lockout(self, flag):
        pass
        # self.joystickOnOff(not flag)

            

    ## setVelocity
    #
    # FIXME: figure out how to set velocity..
    #
    def setVelocity(self, x_vel, y_vel):
        pass

    ## shutDown
    #
    # Disconnect from the stage.
    #
    def shutDown(self):
        # Disconnect from the stage
        if self.good:
            self.pidevice.StopAll(noraise=True)
            pitools.waitonready(self.pidevice)  # there are controllers that need some time to halt all axes

    ## zero
    #
    # Set the current position as the new zero position.
    #
    def zero(self):
        pass
        # if self.good:
        #     pitools._ref_with_pos(self, self.pidevice.axes([0,1])) # added axes [0,1], not sure this ever worked anyway

