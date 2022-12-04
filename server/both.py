from get_cam import get_feed, show_feed
from flask import Flask, request
from flask import Response
import json
import draw

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
jsdata = dict()

@app.route("/live")
def live():
	try:
		return Response(frame_getter(feed), mimetype='multipart/x-mixed-replace; boundary=frame')
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
	return "200"

if __name__ == "__main__":
	app.run()

