import serial


port = 'COM3'
serial_port = serial.Serial(port, 9600, timeout=0.5)

try:
    serial_port.open()
except serial.SerialException:
    pass

command = b'setldenable 0'
cmd = b'%b\r\n' % command

serial_port.reset_input_buffer()
serial_port.write(cmd)
lines_expected = 1
reply = [serial_port.readline() for line in range(lines_expected)]
serial_port.reset_input_buffer()
serial_port.close()
