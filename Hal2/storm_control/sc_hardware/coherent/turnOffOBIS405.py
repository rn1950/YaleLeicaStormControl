import serial
import time


serial_port = serial.Serial('COM4', timeout=.1)

command = b'SOUR:AM:STAT OFF\r\n'

lines_expected = 0
serial_port.reset_input_buffer()
serial_port.write(command)
reply = [serial_port.readline() for line in range(lines_expected)]
serial_port.reset_input_buffer()