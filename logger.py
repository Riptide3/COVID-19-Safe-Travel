import logging

logging.basicConfig(filename=r'travel.log', filemode='w', level=logging.INFO, format='%(message)s')


def get_log(msg):
    logging.info(msg)
