import os
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()

server_handler = logging.StreamHandler()
server_handler.setLevel(logging.INFO)
server_handler.setFormatter(
logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

logger.addHandler(server_handler)
logger.debug("Logger Configured for Production)")

