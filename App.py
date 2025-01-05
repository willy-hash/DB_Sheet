from logging import Logger

import LoggerRegister.logger_config #Establish global configuration of 'logging' package
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

Add new module: [LoggerRegister].
