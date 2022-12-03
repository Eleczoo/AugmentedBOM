
# eleczoo - 69eleczoo69

import cv2










if __name__ == "__main__":
	username = "eleczoo"
	password = "69eleczoo69"
	ip = "10.177.243.195"
	port = "8080"

	feed = f"http://{username}:{password}@{ip}:{port}/video"
	capture = cv2.VideoCapture(feed)
	while(True):
		ret, frame = capture.read()
		cv2.imshow("Phone Camera", frame)   
		if cv2.waitKey(1) == ord("q"):
			break

	capture.release()
	cv2.destroyAllWindows()