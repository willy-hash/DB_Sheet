import os
import LoggerRegister.logger_config #Establish global configuration of 'logging' package
from flask import Flask
from Routes.Main import main
import Config

app = Flask(__name__)

app.register_blueprint(main)

env = os.getenv('FLASK_ENV')

if env == 'production':
    app.config.from_object(Config.productionConfig)
else:
    app.config.from_object(Config.developmentConfig)