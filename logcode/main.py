import logging, logging.config, yaml

with open('config.yaml', 'rb') as fr:
    config = yaml.load(fr, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)

logger = logging.getLogger('simpleExample')

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
