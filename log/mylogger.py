import logging

log = logging.getLogger("myLogger")
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(threadName)s - %(funcName)s - %(message)s",
                              "%Y-%m-%d %H:%M:%S")
ch.setFormatter(formatter)
log.addHandler(ch)


def get_logger():
    return log
