#!/usr/bin/python3

from flask import Flask, redirect, render_template
import logging

from config import getConfigInstance

from requestBP import fileRequests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


config = getConfigInstance()
if config.useDatabase:
    from mySQLAdapter import SQLAdapter
else:
    from mySqlDump import SQLAdapter

sqlAdapt = SQLAdapter()  # Adapter initialization
app = Flask(__name__, template_folder='templates')
app.register_blueprint(fileRequests)
fileRequests.template_folder = '../web/src'


@app.route('/', methods=['GET'])
def redirectHome():
    return redirect('/home')


@app.route('/home', methods=['GET'])
def routeHome():
    return render_template('index.html')


if __name__ == "__main__":
    print("{}:{}".format(config.serverHost, config.serverPort))
    app.run(host=config.serverHost, port=config.serverPort, debug=True)
