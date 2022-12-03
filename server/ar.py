from get_screenshots import get_screenshot
from get_cam import get_feed
import numpy as np
import os.path
import cv2

def get_homography_matrix(kp1, kp2, good):
	srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1 ,2)
	dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1 ,2)
	matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
	return matrix, mask

if __name__ == "__main__":
	if not os.path.exists("front.png"):
		get_screenshot("front.png")
	frontTargetImg = cv2.imread("front.png")
	hF, wF, cF = frontTargetImg.shape

	if not os.path.exists("back.png"):
		get_screenshot("back.png")
	backTargetImg = cv2.imread("back.png")

	circuit = cv2.imread("../circuit_draw.png")
	circuit = cv2.resize(circuit, (wF, hF))

	orb = cv2.ORB_create(2500)
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# FRONT
	kpfront, desfront = orb.detectAndCompute(frontTargetImg, None)
	front_target = cv2.drawKeypoints(frontTargetImg, kpfront, None)

	# BACK
	# kpback, desback = orb.detectAndCompute(backTargetImg, None)
	# back_target = cv2.drawKeypoints(backTargetImg, kpback, None)

	# cv2.imshow("front_target", front_target)
	# cv2.imshow("back_target", back_target)

	NB_FEATURES = 250

	# feed = get_feed()
	feed = get_feed(ip="192.168.59.242")
	# feed = cv2.VideoCapture(0)
	running = True
	while running:
		_, frame = feed.read()
		
		kp2, des2 = orb.detectAndCompute(frame,None)
	
		matches = bf.match(desfront,des2)
		matches = sorted(matches, key = lambda x:x.distance)
		if (len(matches) < NB_FEATURES):
			cv2.imshow("og",frame)
			if cv2.waitKey(1) == ord("q"):
				running = False
			continue

		
		print(len(matches))
		srcpts = np.float32([kpfront[p.queryIdx].pt for p in matches[:NB_FEATURES]]).reshape(-1, 1, 2)
		dstpts = np.float32([kp2[p.trainIdx].pt for p in matches[:NB_FEATURES]]).reshape(-1, 1, 2)

		matrix, mask = cv2.findHomography(srcpts, dstpts, cv2.RANSAC, 10)


		pts = np.float32([[0,0], [0, hF], [wF, hF], [wF, 0]]).reshape(-1, 1, 2)
		dst = cv2.perspectiveTransform(pts, matrix)

		cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)

		warped = cv2.warpPerspective(circuit, matrix, (frame.shape[1], frame.shape[0]))

		alpha = np.sum(warped, axis=-1) > 0
		alpha = np.uint8(alpha * 255)
		draw_with_alpha = cv2.merge((warped, alpha))

		alpha_calque = draw_with_alpha[:, :, 3] / 255.0
		alpha_autre = 1.0 - alpha_calque

		for c in range(3):
			frame[:, :, c] = alpha_calque * draw_with_alpha[:, :, c] + alpha_autre * frame[:, :, c]

		# cv2.imshow("image",img3)
		cv2.imshow("og",frame)
		# cv2.imshow("draw",circuit)
		# cv2.imshow("warped",warped)



		if cv2.waitKey(1) == ord("q"):
			running = False