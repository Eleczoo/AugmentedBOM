# Augmented Reality module 
# Date : refactored 30/09/23 
# This contains the code to warp and align the traces and bounding boxes with the PCB

from get_screenshots import get_screenshot
from get_cam import get_feed

import numpy as np

import cv2

# Global variable telling if the traces and bounding boxes need to be redrawn
flag_redraw = True

def stack_images(base_img, img):
	"""
	Stack the base image with the warped image

	args :
		- base_img : the base image (video feed)
		- img 	   : the warped image (circuit = traces + bounding boxes)
	"""
	alpha = np.sum(img, axis=-1) > 0
	alpha = np.uint8(alpha * 255)
	img_with_alpha = cv2.merge((img, alpha))

	alpha_calque = img_with_alpha[:, :, 3] / 255.0
	alpha_autre = 1.0 - alpha_calque

	for c in range(3):
		base_img[:, :, c] = alpha_calque * img_with_alpha[:, :, c] + alpha_autre * base_img[:, :, c]


def stacked_feed_generator(feed, 
						   keypoints_front, 
						   description_front, 
						   bruteforce_matcher, 
						   orb, 
						   target_shape, 
						   flag_redraw, 
						   NB_FEATURES=250):
	"""
	Generator yields the video feed stacked with the warped traces and bounding boxes
	Yield allows us to get the data live, unlike an iterator, it does not store the incoming data
	but generates it on the fly
	args : 
		- feed 				 : the original video feed
		- keypoints_front 	 : the keypoints of the front image (distinct identifiable features even with different colors)
		- description_front  : the descriptors of the front image
		- bruteforce_matcher : the bruteforce matcher
		- orb 				 : the orb detector (feature detector)
		- target_shape 		 : the shape of the target image 
		- flag_redraw 		 : a flag that indicates if the traces and bounding boxes need to be redrawn
		- NB_FEATURES 		 : the number of features to use for the homography matrix
	"""

	height_front, width_front = target_shape[:2]
	running = True

	while running:

		# Redraw the traces and bounding boxes if needed
		if flag_redraw:
			flag_redraw = False
			circuit = cv2.imread("circuit_draw.png")
			circuit = cv2.resize(circuit, (width_front, height_front))

		_, frame = feed.read()
		
		# Complex stuff to detect and warp circuit to align with the PCB
		kek = cv2.imread("front.png")
		kp2, des2 = orb.detectAndCompute(kek, None)
	
		#print(f"{type(frame) = }")
		#print(f"{type(description_front) = }")
		#print(f"{type(kp2) = }")
		#print(f"{type(des2) = }")

		matches_front = bruteforce_matcher.match(description_front, des2)
		matches_front = sorted(matches_front, key = lambda x:x.distance)

		srcpts = np.float32([keypoints_front[p.queryIdx].pt for p in matches_front[:NB_FEATURES]]).reshape(-1, 1, 2)
		dstpts = np.float32([kp2[p.trainIdx].pt for p in matches_front[:NB_FEATURES]]).reshape(-1, 1, 2)

		matrix, _ = cv2.findHomography(srcpts, dstpts, cv2.RANSAC, 5)

		pts = np.float32([[0,0], [0, height_front], [width_front, height_front], [width_front, 0]]).reshape(-1, 1, 2)
		dst = cv2.perspectiveTransform(pts, matrix)

		cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

		try:
			warped = cv2.warpPerspective(circuit, matrix, (frame.shape[1], frame.shape[0]))
		except:
			flag_redraw = True
			continue

		# Stack the original feed and the circuit (traces and boxes)
		stack_images(frame, warped)

		_, buffer = cv2.imencode(".jpg", frame)
		frame = buffer.tobytes()
		yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




if __name__ == "__main__":
	# ONLY USED FOR TESTING PURPOSES
	import os.path
	if not os.path.exists("front.png"):
		get_screenshot("front.png")
	frontTargetImg = cv2.imread("front.png")
	height_front, width_front, cF = frontTargetImg.shape

	# if not os.path.exists("back.png"):
	# 	get_screenshot("back.png")
	# backTargetImg = cv2.imread("back.png")

	circuit = cv2.imread("circuit_draw.png")
	circuit = cv2.resize(circuit, (width_front, height_front))

	orb = cv2.ORB_create(1000)
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# FRONT
	keypoints_front, description_front = orb.detectAndCompute(frontTargetImg, None)
	# front_target = cv2.drawKeypoints(frontTargetImg, keypoints_front, None)

	# BACK
	# kpback, desback = orb.detectAndCompute(backTargetImg, None)
	# back_target = cv2.drawKeypoints(backTargetImg, kpback, None)

	# cv2.imshow("front_target", front_target)
	# cv2.imshow("back_target", back_target)

	NB_FEATURES = 250

	feed = get_feed()
	# feed = get_feed(ip="192.168.59.242")
	# feed = cv2.VideoCapture("/dev/video4")
	stacked_feed_generator(feed, keypoints_front, description_front, bf, orb, frontTargetImg.shape, circuit)