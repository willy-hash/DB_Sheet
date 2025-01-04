from dotenv import load_dotenv
from Utilities.Singleton import Singleton
import gspread
import json
import os

load_dotenv()

class ConnectionSheet(Singleton):
    worksheet = None

    def __init__(self):
        configuration = os.getenv("SERVICE_ACCOUNT")
        configuration_json = json.loads(configuration)

        gc = gspread.service_account_from_dict(configuration_json)
        sh = gc.open('DB_Python') #set project
        self.worksheet = sh.sheet1  # set sheet project

    def get_Sheet(self):
        return  self.worksheet