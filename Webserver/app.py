#!/usr/bin/python3
from flask import Flask, escape, request


app = Flask(__name__)


@app.route('/')
def index():
	return "True"


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=3000)