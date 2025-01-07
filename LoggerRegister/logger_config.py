import logging

logging.basicConfig(filename="LoggerRegister/LoggerFiles/app.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')