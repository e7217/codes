from serial.tools import list_ports as lp
import logging, os
from logging.handlers import RotatingFileHandler

# logging.basicConfig(
#     filename='logtest.log',
#     filemode='a',
#     format='(%(asctime)s) [ %(levelname)s ] : %(message)s',
#     datefmt='%m/%d/%Y %I:%M:%S %p',
#     level=logging.DEBUG)
#
logger = logging.getLogger('test logcode')
logger.setLevel(logging.DEBUG)

# logcode.disabled = True

# 10MB
fileMaxByte = 1024*1024*10

fh = RotatingFileHandler('usbConnections.log', maxBytes=fileMaxByte, backupCount=2)
fh.setLevel(0)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def checkUSB():
    lplist = lp.comports('/dev/')
    logger.info(' [ check connection ] ')
    for i in lplist:
        if i.device == '/dev/ttyUSB0':
            logger.info('connection : True')
            return True
        else :
            logger.warning('connection : False')
            os.system("sudo reboot")
            return False




