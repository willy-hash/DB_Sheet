import os
import logging
from logging.handlers import RotatingFileHandler

env = os.getenv('RENDER') == 'True'

logging.basicConfig(level=logging.DEBUG if not env else logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger()

if env:
    server_handler = logging.StreamHandler()
    server_handler.setLevel(logging.INFO)
    server_handler.setFormatter(
    logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

    logger.addHandler(server_handler)
    logger.debug("Logger Configured for Production)")

else:
    local_handler = RotatingFileHandler(
        filename="LoggerRegister/LoggerFiles/app.log",
        maxBytes=100000,
        backupCount=3
    )
    local_handler.setLevel(logging.DEBUG)
    local_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    logger.addHandler(local_handler)
    logger.debug("Logger Configured for Development)")