#!/usr/bin/python3

from flask import Flask, redirect, render_template
import logging

from config import getConfigInstance

from requestBP import fileRequests

logger = logging.getLogger(__name__)


config = getConfigInstance()
if config.useDatabase:
    from mySQLAdapter import SQLAdapter
else:
    from mySqlDump import SQLAdapter

sqlAdapt = SQLAdapter()  # Adapter initialization
app = Flask(__name__)
app.register_blueprint(fileRequests)
fileRequests.template_folder = '../web/src'


@app.route('/', methods=['GET'])
def redirectHome():
    return redirect('/home')


@app.route('/home', methods=['GET'])
def routeHome():
    return render_template('/static/index.html')


if __name__ == "__main__":
    app.run(host=config.serverHost, port=config.serverPort, debug=True)
