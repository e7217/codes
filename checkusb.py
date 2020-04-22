from serial.tools import list_ports as lp

def checkUSB():
    lplist = lp.comports('/dev/')

    for i in lplist:
        if i.device == '/dev/ttyUSB0':
            return True
        else :
            return False

print 'USB CONNECTION : ', checkUSB()
