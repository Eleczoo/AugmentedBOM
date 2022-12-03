
# eleczoo - 69eleczoo69

import cv2

def get_feed(username ="eleczoo", password="69eleczoo69", ip="10.177.243.195", port="8080"):
	"""
	Get the video feed
	args: 
		Authentication stuff
		- username
		- password
		- ip
		- port
	"""
	return cv2.VideoCapture(f"http://{username}:{password}@{ip}:{port}/video")

def show_feed(feed, title="Title", ):
	while(True):
		ret, frame = feed.read()
		cv2.imshow(f"{title}", frame)   
		if cv2.waitKey(1) == ord("q"):
			break
	feed.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	feed = get_feed(ip="192.168.59.242")
	show_feed(feed)