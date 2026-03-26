import serial
import time

lines_expected = 0
serial_port = serial.Serial('COM4', timeout=.1)



command = b'SOUR:AM:STAT ON\r\n'


serial_port.reset_input_buffer()
serial_port.write(command)
reply = [serial_port.readline() for line in range(lines_expected)]
serial_port.reset_input_buffer()
time.sleep(1)

power = 50
power_cmd = b'SOUR:POW:LEV:IMM:AMPL %f\r\n' % (power / 1e3)


serial_port.reset_input_buffer()
serial_port.write(power_cmd)
reply = [serial_port.readline() for line in range(lines_expected)]
serial_port.reset_input_buffer()