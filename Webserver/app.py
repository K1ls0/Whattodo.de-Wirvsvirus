#!/usr/bin/python3

from flask import Flask, redirect, request, jsonify, render_template
import logging

from config import getConfigInstance

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


config = getConfigInstance()
if config.useDatabase:
    from mySQLAdapter import SQLAdapter
else:
    from mySqlDump import SQLAdapter

sqlAdapt = SQLAdapter()  # Adapter initialization
print(sqlAdapt)

app = Flask(__name__, template_folder='templates')


def getErrorMsg(code, msg):
    return {'success': False, 'payload': None, 'error': {'code': "{}".format(code), 'message': msg}}


# Main Route:


@app.route('/', methods=['GET'])
def redirectHome():
    return redirect('/home')


@app.route('/home', methods=['GET'])
def routeHome():
    return render_template('index.html')


# Tag requests


@app.route('/tags', methods=['GET'])
def getAllTags():
    # specifier = request.args['tags']
    return jsonify(sqlAdapt.getAllTags())


@app.route('/elements', methods=['GET'])
def getElementsByTags():

    if not request.is_json:
        return jsonify(getErrorMsg(400, "Invalid request structure"))
    asJson = request.get_json()
    tags = asJson.get('tags', [])  # Json cannot read String array???
    doInclude = asJson.get('include', True)
    print("include? " + str(doInclude))

    return jsonify(sqlAdapt.getByTags(tags, doInclude))


if __name__ == "__main__":
    print("{}:{}".format(config.serverHost, config.serverPort))
    app.run(host=config.serverHost, port=config.serverPort, debug=True)
