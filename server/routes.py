from flask import Flask, request
from flask import Response
from flask_cors import CORS

from ar import stacked_feed_generator, get_front_pcb_image, flag_redraw
from get_cam import get_feed_camera, get_feed_network, show_feed

import cv2
import json
import draw
import os

# from __main__ import app

app = Flask(__name__)
CORS(app)

# Global variable containing the data fetched once
# Used in multiple routes, Global to only fetch once  
js_data = dict()

# Global list containing the bounding boxes of the selected components
# It's global because it's used in multiple routes
bounding_boxes = []

@app.route("/live", methods = ['GET'])
def live():
	try:
		feed = get_feed_camera()

		# At start, the front image does not exist
		# So we're gonna take a screenshot of the PCB
		# in order to use it for feature detection
		if not os.path.exists("front.png"):
			get_front_pcb_image(feed, "front.png")

		front_target_image = cv2.imread("front.png")

		# Initiate some stuff for the feature detection
		orb = cv2.ORB_create(1000)
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

		# Detect the features of the front image
		kpfront, desfront = orb.detectAndCompute(front_target_image, None)


		# Return a generator of the base video feed stacked with
		# warped drawn traces and bouding boxes 
		return Response(stacked_feed_generator(	feed,
									kpfront, 
									desfront,
									bf, 
									orb, 
									front_target_image.shape, 
									flag_redraw), 
									mimetype='multipart/x-mixed-replace; boundary=frame')

	except Exception as e:
		print(f"Exception : {e}")

@app.route('/postmethod', methods = ['POST'])
def get_post_data():
	global js_data
	rcv_data = request.form['javascript_data']

	#WRITE RECEIVE DATA IN A FILE
	#with open("data.txt", "w") as f:
		#f.write(rcv_data)
	js_data = dict(json.loads(rcv_data))

	draw.draw_pcb(js_data, [], [], 15)
	#print(js_data["bom"])
	return "200"

@app.route('/postnet', methods = ['POST'])
def get_net_data():
	global js_data, flag_redraw
	rcv_data = request.form['javascript_data']
	#print(rcv_data)
	draw.draw_pcb(js_data, [rcv_data], [], 15)
	flag_redraw = True
	return "200"

@app.route('/postbound', methods = ['POST'])
def get_bounding_data():
	global js_data, bounding_boxes, flag_redraw
	rcv_data = request.form['javascript_data']
	data = json.loads(rcv_data)

	action = data.pop(0)

	if action == "ADD":
		bounding_boxes.extend(data)
	elif action == "DEL":
		for ref in data:
			try:
				bounding_boxes.remove(ref)
			except Exception as e:
				print(f"Exception : {e}")
	
	draw.draw_pcb(js_data, [rcv_data], [], 15)
	flag_redraw = True
	return "200"

@app.route('/postdraw', methods = ['POST'])
def get_drawing_data():
	global js_data, bounding_boxes, flag_redraw
	netlist = []
	rcv_data = request.form['javascript_data']
	data = json.loads(rcv_data)

	type_drawing 	= data.pop(0)
	action 			= data.pop(0)

	if type_drawing == "NET":
		if data[0] != None:
			netlist.append(data[0])
	
	elif type_drawing == "BOX":
		if action == "ADD":
			bounding_boxes.extend(data)
		elif action == "DEL":
			for ref in data:
				try:
					bounding_boxes.remove(ref)
				except:
					pass

	draw.draw_pcb(js_data, netlist, bounding_boxes, 15)
	flag_redraw = True
	return "200"

if __name__ == "__main__":
	app.run()

