import serial #pyserial module
import time

# port = '/dev/ttyUSB0'
port = 'com9'

code = 'A00101A2'
code2 = 'A00100A1'

def init_(port, code):
    ser = serial.Serial(port, 9600, timeout=1)
    ser.write(code.decode('hex'))
    ser.close()

settime = 1

while 1:
    try :
        init_(port,code)
        time.sleep(settime)
        init_(port, code2)
        time.sleep(settime)

    except KeyboardInterrupt:
        print 'KeyboardInterrupt'
        break

    except:
        print 'out'


