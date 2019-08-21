from flask import Flask

app = Flask(__name__)

from dispatcher_api import routes
