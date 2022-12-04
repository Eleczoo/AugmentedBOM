from get_cam import get_feed, show_feed
from ar import generator, get_screenshot
from flask import Flask, request
from flask import Response
from flask_cors import CORS
import json
import draw
import cv2
import os 
import flag


def frame_getter(feed):  
	import time
	import cv2
	# source : https://stackoverflow.com/questions/72138213/serving-local-webcam-video-stream-to-web-with-multipart-mixed-replace-http-res
	while(True):
		ret, frame = feed.read()
		if not ret:
			time.sleep(0.5)
			continue
		else:
			# encode frame to jpg
			ret, buffer = cv2.imencode('.jpg', frame)
			frame = buffer.tobytes()
			# Yield returns a generator, to allow getting things live
			yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

feed = get_feed()
app = Flask(__name__)
CORS(app)
jsdata = dict()
bounding_list = []

@app.route("/live")
def live():

	try:
		if not os.path.exists("front.png"):
			get_screenshot("front.png")
		frontTargetImg = cv2.imread("front.png")

		orb = cv2.ORB_create(1000)
		bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

		# FRONT
		kpfront, desfront = orb.detectAndCompute(frontTargetImg, None)

		feed = get_feed()
		return Response(generator(feed, kpfront, desfront, bf, orb, frontTargetImg.shape, flag.flag_redraw), mimetype='multipart/x-mixed-replace; boundary=frame')
	except Exception as e:
		print(f"Exception : {e}")

@app.route('/postmethod', methods = ['POST'])
def get_post_data():
	global jsdata
	rcv_data = request.form['javascript_data']

	#WRITE RECEIVE DATA IN A FILE
	#with open("data.txt", "w") as f:
		#f.write(rcv_data)
	jsdata = dict(json.loads(rcv_data))

	draw.draw_pcb(jsdata, [], [], 15)
	#print(jsdata["bom"])
	return "200"

@app.route('/postnet', methods = ['POST'])
def get_net_data():
	global jsdata
	rcv_data = request.form['javascript_data']
	#print(rcv_data)
	draw.draw_pcb(jsdata, [rcv_data], [], 15)
	flag.flag_redraw = True
	return "200"

@app.route('/postbound', methods = ['POST'])
def get_bounding_data():
	global jsdata, bounding_list
	rcv_data = request.form['javascript_data']
	data = json.loads(rcv_data)

	action = data.pop(0)

	if action == "ADD":
		bounding_list.extend(data)
	elif action == "DEL":
		for ref in data:
			try:
				bounding_list.remove(ref)
			except:
				pass
	
	draw.draw_pcb(jsdata, [rcv_data], [], 15)
	flag.flag_redraw = True
	return "200"

@app.route('/postdraw', methods = ['POST'])
def get_drawing_data():
	global jsdata, bounding_list
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
			bounding_list.extend(data)
		elif action == "DEL":
			for ref in data:
				try:
					bounding_list.remove(ref)
				except:
					pass
	

	draw.draw_pcb(jsdata, netlist, bounding_list, 15)
	flag.flag_redraw = True
	return "200"

if __name__ == "__main__":
	app.run()

