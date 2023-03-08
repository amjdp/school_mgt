import logging
logging.basicConfig(filename="log_msg.log", format='%(asctime)s %(message)s', filemode='w')

a = 10
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occured", exc_info=True)



# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

# logging.debug('The debug message is displaying')
# logging.info('The info message is displaying')
# logging.warning('The warning message is displaying')
# logging.error('The error message is displaying')
# logging.critical('The critical message is displaying')
