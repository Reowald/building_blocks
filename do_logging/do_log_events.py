import logging
import time

logging.basicConfig(filename='example.log',  level=logging.INFO, format='%(asctime)s %(message)s')
time.sleep(0.1)
logging.debug('This message should go to the log file')
time.sleep(0.1)
logging.info('So should this')
time.sleep(0.1)
logging.warning('And this, too')
time.sleep(0.1)
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')