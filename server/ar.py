# Augmented Reality module 
# Date : refactored 02/04/2024
# This contains the code to warp and align the traces and bounding boxes with the PCB

from get_cam import *
import numpy as np
import os.path
import cv2

# Global variable telling if the traces and bounding boxes need to be redrawn
flag_redraw = True

def get_homography_matrix(kp1, kp2, good):
	srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1 ,2)
	dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1 ,2)
	matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
	return matrix, mask

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

def get_corners_of_pcb_in_frame(frame):
	"""Returns the corner of the pcb in the given frame

	Args:
		frame (np.array): grayscale frame taken from the camera

	Returns:
		list(tuple): List of the 4 contours of the pcb
	"""

	# Create the kernel for the dilate function
	KERNEL_SHAPE = cv2.MORPH_RECT
	KERNEL_SIZE = 3
	kernel = cv2.getStructuringElement(KERNEL_SHAPE, (KERNEL_SIZE, KERNEL_SIZE))

	# Blue the image to remove the noise before finding the edges
	blur = cv2.blur(frame, (5, 5))
	# Edge detection using the canny algorithm
	edges = cv2.Canny(blur, 40, 160)
	# Dilate the edges to have better edges
	edges = cv2.dilate(edges, kernel, iterations=5)

	# Find all the contours in the frame
	contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Find the contour of the pcb
	sorted_contours = sorted(contours, key=lambda cnt: cv2.arcLength(cnt, True), reverse=True)
	sudoku_contour = sorted_contours[0]

	# Find the 4 corners of the pcb
	top_left_corner = sorted(sudoku_contour, key=lambda p: p[0][0] + p[0][1], reverse=False)[0][0]
	top_right_corner = sorted(sudoku_contour, key=lambda p: p[0][0] - p[0][1], reverse=True)[0][0]
	bottom_left_corner = sorted(sudoku_contour, key=lambda p: p[0][1] - p[0][0], reverse=True)[0][0]
	bottom_right_corner = sorted(sudoku_contour, key=lambda p: p[0][0] + p[0][1], reverse=True)[0][0]

	corners = np.array([top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner], dtype=np.int32)

	return corners


def get_new_image_corners(corners):
	"""Finds the size of the new image after the rotation without modifying the pcb size

	Args:
		corners (np.array): list of the 4 corners of the pcb in the following order : 
		top_left, top_right, bottom_left, bottom_right

	Returns:
		np.array: array containing the list of the new corners. Last element represents the size of the new image
	"""
	top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner = corners

	width = round(np.linalg.norm(top_left_corner - top_right_corner))
	height = round(np.linalg.norm(top_left_corner - bottom_left_corner))

	new_corners = np.array([[0, 0], [width, 0], [0, height], [width, height]], dtype=np.int32)

	return new_corners

def get_clean_image_from_frame(frame):
	"""Finds the pcb in the frame and returns a clean picture of the pcb

	Args:
		frame (np.array): Image from the camera

	Returns:
		np.array: clean picture of the pcb
	"""
	# Get corners of the pcb in the frame
	corners = get_corners_of_pcb_in_frame(frame)
	# Get the new size of the image and the pos of the new corners
	new_corners = get_new_image_corners(corners)
	# Get the transformation matrix
	matrix = cv2.getPerspectiveTransform(corners.astype(np.float32), new_corners.astype(np.float32))
	# Apply transformation matrix
	return cv2.warpPerspective(frame, matrix, new_corners[-1])

def get_front_pcb_image(feed, filename: str):
	_, frame = feed.read()

	# TODO: Remove, tmp fix with my webcam app
	frame = frame[60:-60,]

	clean = get_clean_image_from_frame(frame)

	cv2.imwrite(filename, clean)


def stacked_feed_generator(feed, keypoints_front, description_front, bf, orb, targetShape, flag_redraw, NB_FEATURES=250):
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

	height_front, width_front = targetShape[:2]
	running = True

	while running:

		# Redraw the traces and bounding boxes if needed
		if flag_redraw:
			flag_redraw = False
			circuit = cv2.imread("circuit_draw.png")
			circuit = cv2.resize(circuit, (width_front, height_front))

		_, frame = feed.read()
		
		# TODO: Remove, tmp fix with my webcam app
		frame = frame[60:-60,]

		kp2, des2 = orb.detectAndCompute(frame, None)

		matches_front = bf.match(description_front, des2)
		matches_front = sorted(matches_front, key = lambda x:x.distance)

		srcpts = np.float32([keypoints_front[p.queryIdx].pt for p in matches_front[:NB_FEATURES]]).reshape(-1, 1, 2)
		dstpts = np.float32([kp2[p.trainIdx].pt for p in matches_front[:NB_FEATURES]]).reshape(-1, 1, 2)
		
		matrix, mask = cv2.findHomography(srcpts, dstpts, cv2.RANSAC, 5)

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
		# get_screenshot("front.png")
		pass
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

	feed = get_feed_camera()
	# feed = get_feed(ip="192.168.59.242")
	# feed = cv2.VideoCapture("/dev/video4")
	stacked_feed_generator(feed, keypoints_front, description_front, bf, orb, frontTargetImg.shape, circuit)