import os, logging, logging.config, yaml


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


log_dir_lists = ["./logs", "./logs_date"]
for log_dir in log_dir_lists:
    createFolder(log_dir)

with open("config.yaml", "rb") as fr:
    config = yaml.load(fr, Loader=yaml.FullLoader)
    logging.config.dictConfig(config)

logger = logging.getLogger("simpleExample")

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
