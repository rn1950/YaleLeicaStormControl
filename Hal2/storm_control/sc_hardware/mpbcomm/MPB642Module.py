import storm_control.hal4000.halLib.halMessage as halMessage


from PyQt5 import QtCore
import storm_control.sc_hardware.baseClasses.amplitudeModule as amplitudeModule
import storm_control.sc_library.parameters as params

import subprocess
import sys


class MPBFunctionality(amplitudeModule.AmplitudeFunctionalityBuffered):
    def __init__(self, mpb_laser=None, channel=None, **kwds):
        super().__init__(**kwds)


        # self.mpb_laser = mpb_laser



    def onOff(self, power, state):
        print('mpb module line 23 not impelemented')
        # fake_arg = 0
        # if state:
        #     self.mustRun(task=self.genesis_laser.turnOn, args=[fake_arg])
        # else:
        #     self.mustRun(task=self.genesis_laser.turnOff, args=[fake_arg])

    def output(self, state):
        print('not implemented 1234')
        fake_arg = 0
        if state:
            subprocess.run([sys.executable, "C:/Users/Light-saver/Documents/storm_control/Hal2/storm_control/sc_hardware/mpbcomm/turnOnMPB642.py"])

            # self.genesis_laser.turnOn(fake_arg)
            # self.maybeRun(task=self.genesis_laser.turnOn, args=[fake_arg])
        else:
            subprocess.run([sys.executable, "C:/Users/Light-saver/Documents/storm_control/Hal2/storm_control/sc_hardware/mpbcomm/turnOffMPB642.py"])
            # self.genesis_laser.turnOff(fake_arg)
            # self.maybeRun(task=self.genesis_laser.turnOff, args=[fake_arg])


    def startFilm(self, power):
        print('not implemented 12345')


class MPB642Module(amplitudeModule.AmplitudeModule):
    def __init__(self, module_params = None, qt_settings = None, **kwds):
        super().__init__(**kwds)
        # self.lsr = genesis.Genesis(0, 50)


        self.mpb_fns = {}
        self.lsr_mutex = QtCore.QMutex()

        configuration = module_params.get("configuration")
        for fn_name in configuration.getAttrs():
            fn_params = configuration.get(fn_name)
            if isinstance(fn_params, params.StormXMLObject):

                mpb_fn_name = self.module_name + "." + fn_name
                channel = fn_params.get("channel")

                self.mpb_fns[mpb_fn_name] = MPBFunctionality(channel=None, device_mutex=self.lsr_mutex)


    def cleanUp(self, qt_settings):
        print('not implemented mpb module line 45')


    def getFunctionality(self, message):
        mpb_fn_name = message.getData()["name"]
        if mpb_fn_name in self.mpb_fns:
            message.addResponse(halMessage.HalMessageResponse(source=self.module_name,
                                                          data={"functionality": self.mpb_fns[mpb_fn_name]}))
