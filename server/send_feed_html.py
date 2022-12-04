
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

if __name__ == "__main__":
	from get_cam import get_feed, show_feed
	from flask import Flask
	from flask import Response

	feed = get_feed()
	app = Flask(__name__)

	@app.route("/live")
	def live():
		try:
			return Response(frame_getter(feed), mimetype='multipart/x-mixed-replace; boundary=frame')
		except Exception as e:
			print(f"Exception : {e}")

	app.run(debug=True)
