from flaks import Flask, escape, request


app = Flask(__name__)

@app.route('/')
def index():
	return "True"