#pip install flask
#sudo apt install python3-flask
#pip install -U flask-cors

from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/postmethod', methods = ['POST'])
def get_post_data():
	rcv_data = request.form['javascript_data']
	jsdata = dict(json.loads(rcv_data))
	#print(jsdata["bom"])
	return "200"

if __name__ == "__main__":
	app.run(host="0.0.0.0")