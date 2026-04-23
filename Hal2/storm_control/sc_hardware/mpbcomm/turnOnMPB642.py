import serial
import time

print('turning on mpb')
port = 'COM3'
serial_port = serial.Serial(port, 9600, timeout=0.5)

try:
    serial_port.open()
except serial.SerialException:
    print('port already open or could not open port')

power_cmd = ('setpower 2 ' + str(800)).encode()
cmd = b'%b\r\n' % power_cmd

serial_port.reset_input_buffer()
serial_port.write(cmd)
lines_expected = 1
reply = [serial_port.readline() for line in range(lines_expected)]
print(reply)
serial_port.reset_input_buffer()

time.sleep(2)

command = b'setldenable 1'
cmd = b'%b\r\n' % command

serial_port.reset_input_buffer()
serial_port.write(cmd)
lines_expected = 1
reply = [serial_port.readline() for line in range(lines_expected)]
serial_port.reset_input_buffer()
serial_port.close()
