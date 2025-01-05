from dotenv import load_dotenv
from Utilities.Singleton import Singleton
import logging
import gspread
import json
import os

load_dotenv()
logger_instance = logging.getLogger(__name__)

class ConnectionSheet(Singleton):
    worksheet = None
    logger = logger_instance

    def __init__(self):
        try:
            configuration = os.getenv("SERVICE_ACCOUNT")

            if configuration is None:
                self.logger.error("SERVICE_ACCOUNT environment variable not set")
                raise ValueError("SERVICE_ACCOUNT not configured")

            configuration_json = json.loads(configuration)

            gc = gspread.service_account_from_dict(configuration_json)
            sh = gc.open('DB_Python') #set project
            self.worksheet = sh.sheet1  # set sheet project

            self.logger.info("Connection to Google Sheet 'DB_Python' established successfully.")

        except Exception as e:
            self.logger.exception("Failed to initialize ConnectionSheet.")
            raise e

    def get_Sheet(self):
        return  self.worksheet