import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    filename='logtest.log', 
    format='(%(asctime)s) [ %(levelname)s ] : %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG)

logging.warning('Warning!')
logging.info('Info!!')
logging.debug('Debug!!')

logger = logging.getLogger('test logger')
logger.setLevel(logging.DEBUG)

# logger.disabled = True

fileMaxByte = 1024*1024*1

fh = RotatingFileHandler('filelog.log', maxBytes=fileMaxByte, backupCount=2)
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

while 1:
    try :
            
        logger.debug('-DEBUG')
        logger.info('-INFO')
        logger.warning('-WARNING')
        logger.error('-ERROR')
        logger.critical('-CRITICAL')
    except KeyboardInterrupt() :
        break
