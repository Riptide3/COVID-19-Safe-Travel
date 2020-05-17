import logging

logging.basicConfig(filename=r'travel.log', level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')


def get_log(msg):
    logging.info(msg)
