from get_cam import get_feed, show_feed
import numpy as np
import cv2


def get_screenshot():
	feed = get_feed()
		# feed = cv2.VideoCapture("/dev/video4")	
	_, frame = feed.read()
	print(f"{_}")
	print(f"{frame = }")
	
	#show_feed(feed, )

	return frame



def get_xy_minmax(points):
	minx = points[0][0]
	miny = points[0][1]
	maxx = points[0][0]
	maxy = points[0][1]

	for point in points:
		x, y = point

		if x < minx: minx = x
		if x > maxx: maxx = x
		if y < miny: miny = y
		if y > maxy: maxy = y

	return (int(minx if minx > 0 else 0), int(miny if miny > 0 else 0)), (int(maxx), int(maxy))

def get_crop_img(image,rect):
	x,y,w,h = rect
	return image[y:y+h,x:x+w]

def get_corners_of_pcb_in_frame(frame):
	"""returns the corner of the pcb in the given frame

	args:
		frame (np.array): grayscale frame taken from the camera

	returns:
		list(tuple): List of the 4 contours of the pcb
	"""

	# Create the kernel for the dilate function
	KERNEL_SHAPE = cv2.MORPH_RECT
	KERNEL_SIZE = 3
	kernel = cv2.getStructuringElement(KERNEL_SHAPE, (KERNEL_SIZE, KERNEL_SIZE))

	# Blue the image to remove the noise before finding the edges
	blur = cv2.blur(frame, (3, 3))
	# Edge detection using the canny algorithm
	edges = cv2.Canny(blur, 40, 160)
	# Dilate the edges to have better edges
	edges = cv2.dilate(edges, kernel, iterations=5)

	cv2.imwrite("edges.png", edges)

	# Find all the contours in the frame
	contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	# Find the contour of the pcb
	sorted_contours = sorted(contours, key=lambda cnt: cv2.arcLength(cnt, True), reverse=True)
	pcb_contour = sorted_contours[0]

	# Find the 4 corners of the pcb
	top_left_corner = sorted(pcb_contour, key=lambda p: p[0][0] + p[0][1], reverse=False)[0][0]
	top_right_corner = sorted(pcb_contour, key=lambda p: p[0][0] - p[0][1], reverse=True)[0][0]
	bottom_left_corner = sorted(pcb_contour, key=lambda p: p[0][1] - p[0][0], reverse=True)[0][0]
	bottom_right_corner = sorted(pcb_contour, key=lambda p: p[0][0] + p[0][1], reverse=True)[0][0]

	corners = [top_left_corner, top_right_corner, bottom_left_corner, bottom_right_corner]

	return corners

def get_cropped_pcb_from_frame(frame, corners):
	"""Crop the frame to have only the pcb. The image will be used for the features extraction

	args:
		frame (np.array): RGB Frame from the camera
		corners (list(tuple)): List of the 4 corners of the pcb

	returns:
		np.array: Cropped image containing only the pcb
	"""

	original_frame = frame.copy()

	cv2.imwrite("COPY.png", frame)

	# Find the angle we need to rotate the frame. We need to pcb parallel to the x axis
	# to have a clean crop and a clean feature extraction
	dx = corners[0][0] - corners[1][0]
	dy = corners[0][1] - corners[1][1]
	rot_angle = np.rad2deg(np.arctan(dy/dx))

	print(f"{rot_angle = }")
	print()

	w, h = frame.shape[:2]
	origin = (h/2, w/2)

	# Rotate the frame
	matrix = cv2.getRotationMatrix2D(origin, rot_angle, 1)

	# Modify the matrix to avoid cropping the image.
	# rotation calculates the cos and sin, taking absolutes of those.
	abs_cos = abs(matrix[0,0]) 
	abs_sin = abs(matrix[0,1])

	# find the new width and height bounds
	bound_w = int(h * abs_sin + w * abs_cos)
	bound_h = int(h * abs_cos + w * abs_sin)

	# subtract old image center (bringing image back to origin) and adding the new image center coordinates
	matrix[0, 2] += bound_w/2 - origin[0]
	matrix[1, 2] += bound_h/2 - origin[1]

	new_frame = cv2.warpAffine(original_frame, matrix, (bound_w,bound_h))
	cv2.imwrite("new_frame.png", new_frame)

	# transform points
	# don't remember what the hell is going on here
	points = np.array(corners)
	ones = np.ones(shape=(len(points), 1))
	points_ones = np.hstack([points, ones])
	transformed_points = matrix.dot(points_ones.T).T

	# Find the new possition of the pcb in the rotated frame
	mins, maxs = get_xy_minmax(transformed_points)
	rect = (mins[0], mins[1], maxs[0]-mins[0], maxs[1]-mins[1])

	# crop only the pcb
	print(f"{rect =}")
	crop = get_crop_img(new_frame, rect)

	return crop

if __name__ == "__main__":
	frame = get_screenshot()
	print(type(frame))                                 
	corners = get_corners_of_pcb_in_frame(frame)
	crop = get_cropped_pcb_from_frame(frame, corners)

	# print(f"{crop =}")
	print(f"{corners =}")

	cv2.imwrite("cropped.png", crop)

# def draw_circle_on_click(event, x, y, flags, param):
# 	global frame
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		frame = cv2.circle(frame, (x, y), 5, (0,0,255), -5)
# 		pcb_edge.append((x,y))


# def get_screenshot(filename):
# 	global frame
# 	feed = get_feed()
# 	# feed = cv2.VideoCapture("/dev/video4")
# 	cv2.namedWindow("image")
# 	cv2.setMouseCallback("image", draw_circle_on_click)
	
# 	_, frame = feed.read()
# 	original_frame = frame.copy()

# 	running = True
# 	while running:
# 		cv2.imshow(f"image", frame)

# 		match cv2.waitKey(1):
# 			# q : exit
# 			case 113:
# 				running = False
# 			# enter : save the screenshot
# 			case 13:
# 				if len(pcb_edge) <= 1: continue
# 				# Get the rotation angle
# 				dx = pcb_edge[0][0] - pcb_edge[1][0]
# 				dy = pcb_edge[0][1] - pcb_edge[1][1]
# 				rot_angle = np.rad2deg(np.arctan(dy/dx))
				
# 				h, w = frame.shape[:2]
# 				origin = (h/2, w/2)

# 				# Rotate the frame
# 				matrix = cv2.getRotationMatrix2D(origin, rot_angle, 1)

# 				# Modify the matrix to avoid cropping the image.
# 				# rotation calculates the cos and sin, taking absolutes of those.
# 				abs_cos = abs(matrix[0,0]) 
# 				abs_sin = abs(matrix[0,1])

# 				# find the new width and height bounds
# 				bound_w = int(h * abs_sin + w * abs_cos)
# 				bound_h = int(h * abs_cos + w * abs_sin)

# 				# subtract old image center (bringing image back to origo) and adding the new image center coordinates
# 				matrix[0, 2] += bound_w/2 - origin[0]
# 				matrix[1, 2] += bound_h/2 - origin[1]

# 				new_frame = cv2.warpAffine(original_frame, matrix, (bound_w,bound_h))

# 				# transform points
# 				points = np.array(pcb_edge)
# 				ones = np.ones(shape=(len(points), 1))
# 				points_ones = np.hstack([points, ones])
# 				transformed_points = matrix.dot(points_ones.T).T
# 				# print(points)
# 				# print(ones)
# 				# print(points_ones)
				
# 				mins, maxs = get_xy_minmax(transformed_points)

# 				# new_frame = cv2.rectangle(new_frame, mins, maxs, (255,0,0), 2)

# 				rect = (mins[0], mins[1], maxs[0]-mins[0], maxs[1]-mins[1])

# 				crop = getSubRect(new_frame, rect)
# 				cv2.imwrite(filename, crop)
# 				# cv2.imshow("image", crop)
# 				# cv2.waitKey(0)
# 				cv2.destroyAllWindows()
# 				running = False

# 			# delete : Delete point
# 			case 8:
# 				if len(pcb_edge) <= 0: continue
# 				pcb_edge.pop()
# 				frame = original_frame.copy()
# 				for point in pcb_edge:
# 					x,y = point
# 					frame = cv2.circle(frame, (x, y), 5, (0,0,255), -5)


# if __name__ == "__main__":
# 	get_screenshot("temp.png")