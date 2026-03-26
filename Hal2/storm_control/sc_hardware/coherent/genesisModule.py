import storm_control.hal4000.halLib.halMessage as halMessage
import storm_control.sc_hardware.coherent.genesis as genesis

from PyQt5 import QtCore
import storm_control.sc_hardware.baseClasses.amplitudeModule as amplitudeModule
import storm_control.sc_library.parameters as params

import subprocess
import sys


class CoherentGenesisLaserFunctionality(amplitudeModule.AmplitudeFunctionalityBuffered):
    def __init__(self, genesis_laser=None, channel=None, **kwds):
        super().__init__(**kwds)
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')
        print('INITIALIZE COHERENT GENESIS LASER FUNCTIONALITY')


        self.genesis_laser = genesis_laser



    def onOff(self, power, state):
        print('genesis module onoff line 15')
        fake_arg = 0
        if state:
            self.mustRun(task=self.genesis_laser.turnOn, args=[fake_arg])
        else:
            self.mustRun(task=self.genesis_laser.turnOff, args=[fake_arg])

    def output(self, state):
        print('not implemented 1234')
        fake_arg = 0
        if state:
            subprocess.run([sys.executable, "C:/Users/Light-saver/Documents/storm_control/Hal2/storm_control/sc_hardware/coherent/turnOnCoherent0.py"])

            # self.genesis_laser.turnOn(fake_arg)
            # self.maybeRun(task=self.genesis_laser.turnOn, args=[fake_arg])
        else:
            subprocess.run([sys.executable, "C:/Users/Light-saver/Documents/storm_control/Hal2/storm_control/sc_hardware/coherent/turnOffCoherent0.py"])
            # self.genesis_laser.turnOff(fake_arg)
            # self.maybeRun(task=self.genesis_laser.turnOff, args=[fake_arg])


    def startFilm(self, power):
        print('not implemented 12345')


class CoherentGenesisModule(amplitudeModule.AmplitudeModule):
    def __init__(self, module_params = None, qt_settings = None, **kwds):
        super().__init__(**kwds)
        self.lsr = genesis.Genesis(0, 50)


        self.genesis_fns = {}
        self.lsr_mutex = QtCore.QMutex()

        configuration = module_params.get("configuration")
        for fn_name in configuration.getAttrs():
            fn_params = configuration.get(fn_name)
            if isinstance(fn_params, params.StormXMLObject):

                genesis_fn_name = self.module_name + "." + fn_name
                channel = fn_params.get("channel")

                self.genesis_fns[genesis_fn_name] = CoherentGenesisLaserFunctionality(genesis_laser=self.lsr,channel=None,device_mutex=self.lsr_mutex)


    def cleanUp(self, qt_settings):
        print('not implemented genesis module line 45')


    def getFunctionality(self, message):
        genesis_fn_name = message.getData()["name"]
        if genesis_fn_name in self.genesis_fns:
            message.addResponse(halMessage.HalMessageResponse(source=self.module_name,
                                                          data={"functionality": self.genesis_fns[genesis_fn_name]}))
