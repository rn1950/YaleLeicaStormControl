##

## COHERENT 561

##

##

## END COHERENT 561

##
import ctypes
import os

# Define the path to the DLL file
# dll_path = os.path.join(os.getcwd(), 'C:/Users/Light-saver/Documents/LabVIEW/Lasers/Coherent Genesis/Win64/CohrHOPS.dll')
#
# my_dll = ctypes.CDLL(dll_path)
#
# resp = []
# print(my_dll.CohrHOPS_SendCommand("?P", resp))
#
# print(resp)
#

##

## COHERENT 488

##

##

## END COHERENT 488

##

##

## COHERENT 405

##


import serial
import time




class CoherentOBISLaser():
    powerControlable = True

    def __init__(self, serial_port='COM8', turn_on=False, name='OBIS', init_power=5, reply_ok=False, **kwargs):
        """

        Parameters
        ----------
        serial_port: str
            serial port
        turn_on: bool
            Whether or not to turn on the laser on instantiating the class
        name: str
            Name of the laser
        init_power: float
            In units of mW
        reply_ok: bool
            Whether this laser is configured to reply 'OK' after each message or not.
            Note this has been observed when communicating throughthe OBIS power supply
            rather than directly with the head unit.
        kwargs
        """
        self.serial_port = serial.Serial('COM4', timeout=.1)
        self._reply_OK = int(reply_ok)
        self.name = name



        time.sleep(1)

        # self.power = 0

        # self.MIN_POWER = 1e3 * float(self.query(b'SOUR:POW:LIM:LOW?\r\n', lines_expected=1)[0])
        # self.MAX_POWER = 1e3 * float(self.query(b'SOUR:POW:LIM:HIGH?\r\n', lines_expected=1)[0])
        print(self.query(b'SOUR:POW:LIM:LOW?\r\n', lines_expected=1)[0])
        print(self.query(b'SOUR:POW:LIM:HIGH?\r\n', lines_expected=1)[0])
        # self.is_on = False

        # self.query(b'SYST:COMM:HAND OFF\r\n', lines_expected=0)





    def query(self, command, lines_expected=1):
        """
      Send serial command and return a set number of reply lines from the device before clearing the device outputs

      Parameters
      ----------
      command: bytes
          Command to send to the device. Must be complete, e.g. b'command\r\n'
      lines_expected: int
          Number of interesting lines to be returned from the device. Any remaining output from the device will be
          cleared. Note that having lines_expected larger than the actual number of reply lines for a given command
          will not crash, but will take self.timeout seconds for each extra line requested.

      Returns
      -------
      reply: list
          list of lines retrieved from the device. Blank lines are possible

      Notes
      -----
      serial.Serial.readlines method was not used because our device requires a wait until each line is read before
      it writes the next line.
      """

        self.serial_port.reset_input_buffer()
        self.serial_port.write(command)
        reply = [self.serial_port.readline() for line in range(lines_expected + self._reply_OK)]
        self.serial_port.reset_input_buffer()

        return reply




    def IsOn(self):
        # Would be nice to check, but there is a performance hit (this gets tracked as a scope state to update the GUI)
        return self.is_on

    def TurnOn(self):
        self.query(b'SOUR:AM:STAT ON\r\n', lines_expected=0)
        self.is_on = True

    def TurnOff(self):
        self.query(b'SOUR:AM:STAT OFF\r\n', lines_expected=0)
        # FIXME - would be nice to check this worked
        self.is_on = False

    def SetPower(self, power):
        """

        Parameters
        ----------
        power: float
            Power in units of mW, note that laser API takes units of W

        Returns
        -------

        """
        self.query(b'SOUR:POW:LEV:IMM:AMPL %f\r\n' % (power / 1e3), lines_expected=0)
        self.power = power

    def GetPower(self):
        return self.power





if __name__ == "__main__":
    print('testing laser communications OBIS')
    serial_port = 'COM4'
    obis = CoherentOBISLaser()
    obis.TurnOff()
    time.sleep(10)
    obis.TurnOn()
    obis.SetPower(50)
    time.sleep(20)
    obis.TurnOff()





##

## END COHERENT 405

##









##

## MPB

##




# import serial
# import time
#
# class MPBCWLaser:
#
#     def __init__(self):
#         serial_port = 'COM3'
#         self.serial_port = serial.Serial(serial_port, 9600, timeout=1)
#
#     def query(self, command, lines_expected=1):
#         """
#         Get value from laser via serial port.
#         """
#         cmd = b'%b\r\n' % command
#
#         self.serial_port.reset_input_buffer()
#         self.serial_port.write(cmd)
#         reply = [self.serial_port.readline() for line in range(lines_expected)]
#         self.serial_port.reset_input_buffer()
#         return reply
#
#
#     def IsOn(self):
#         """
#         Returns
#         -------
#         is_on: bool
#             Initialization status of the laser
#
#         Notes
#         -----
#         Would be nice to check explicitly that everything is working, e.g. (self.is_on and
#         self.polling_thread is not None and self.polling_thread.is_alive() and self.serial_port.is_open and self.check_on()),
#         but this function is called to update the microscope state, so a serial command is too expensive.
#
#         """
#         return self.is_on
#
#
#     def check_on(self):
#         response = self.query(b'getldenable', lines_expected=1)[0]
#         return bool(response.split(b'\n')[0])
#
#
#     def TurnOn(self):
#         # make sure serial is open
#         try:
#             self.serial_port.open()
#         except serial.SerialException:
#             print('port is already open OR could not connect to serial port')
#
#         self.is_on = True
#
#         # turn on the laser
#         self.query(b'setldenable 1', lines_expected=1)
#
#
#     def TurnOff(self):
#         self.query(b'setldenable 0', lines_expected=1)
#         self.is_on = False
#
#
#     def SetPower(self, power):
#         self.query(('setpower 2 ' + str(power)).encode(), lines_expected=1)
#         self.power = power
#
#
#     def GetPower(self):
#         return self.power
#
#
#     def GetRealPower(self):
#         return float(self.query(b'power 0', lines_expected=1)[0].split(b'\r')[0])
#
#
#     def Close(self):
#         print('Shutting down %s' % self.name)
#         self.TurnOff()
#         time.sleep(.1)
#
#
#
#
# if __name__ == "__main__":
#     print('testing laser communications MPB')
#     serial_port = 'COM3'
#
#     mpb = MPBCWLaser()
#     print(mpb.GetRealPower())
#     print(mpb.check_on())
#     mpb.SetPower(200)
#     print(mpb.GetRealPower())
#
#     mpb.TurnOn()
#
#     time.sleep(20)
#     print(mpb.GetRealPower())
#
#     mpb.TurnOff()
#
#
#     # serial_port.reset_input_buffer()
#     # cmd = b'%b\r\n' % b'power 0'
#     # serial_port.write(cmd)
#     # reply = [serial_port.readline() for line in range(1)]
#     # print(reply)
#     # serial_port.reset_input_buffer()



##

## END MPB

##