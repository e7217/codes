# internal modules
import os, logging, logging.config

# external modules
import yaml


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def init_logger():
    log_dir_lists = ["./logs", "./logs_date"]
    for log_dir in log_dir_lists:
        create_folder(log_dir)

    with open("config.yaml", "rb") as fr:
        config = yaml.load(fr, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)


if __name__ == "__main__":
    init_logger()
    logger = logging.getLogger("simpleExample")

    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
