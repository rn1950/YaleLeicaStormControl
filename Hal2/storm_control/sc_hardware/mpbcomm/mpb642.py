

import serial
import time

class MPBCWLaser:

    def __init__(self):
        serial_port = 'COM3'
        self.serial_port = serial.Serial(serial_port, 9600, timeout=0.5)

    def query(self, command, lines_expected=1):
        """
        Get value from laser via serial port.
        """
        cmd = b'%b\r\n' % command

        self.serial_port.reset_input_buffer()
        self.serial_port.write(cmd)
        reply = [self.serial_port.readline() for line in range(lines_expected)]
        self.serial_port.reset_input_buffer()
        return reply


    def IsOn(self):
        """
        Returns
        -------
        is_on: bool
            Initialization status of the laser

        Notes
        -----
        Would be nice to check explicitly that everything is working, e.g. (self.is_on and
        self.polling_thread is not None and self.polling_thread.is_alive() and self.serial_port.is_open and self.check_on()),
        but this function is called to update the microscope state, so a serial command is too expensive.

        """
        return self.is_on


    def check_on(self):
        response = self.query(b'getldenable', lines_expected=1)[0]
        return bool(response.split(b'\n')[0])


    def TurnOn(self):
        # make sure serial is open
        try:
            self.serial_port.open()
        except serial.SerialException:
            pass

        self.is_on = True

        # turn on the laser
        self.query(b'setldenable 1', lines_expected=1)


    def TurnOff(self):
        self.query(b'setldenable 0', lines_expected=1)
        self.is_on = False


    def SetPower(self, power):
        self.query(('setpower 2 ' + str(power)).encode(), lines_expected=1)
        self.power = power


    def GetPower(self):
        return self.power


    def GetRealPower(self):
        return float(self.query(b'power 0', lines_expected=1)[0].split(b'\r')[0])


    def Close(self):
        print('Shutting down %s' % self.name)
        self.TurnOff()
        time.sleep(.1)
