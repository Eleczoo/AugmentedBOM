from get_cam import get_feed
import numpy as np
import cv2


pcb_edge = []
frame = None

def draw_circle_on_click(event, x, y, flags, param):
	global frame
	if event == cv2.EVENT_LBUTTONDOWN:
		frame = cv2.circle(frame, (x, y), 5, (0,0,255), -5)
		pcb_edge.append((x,y))


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

	return (int(minx), int(miny)), (int(maxx), int(maxy))

def getSubRect(image,rect):
    x,y,w,h = rect
    return image[y:y+h,x:x+w]


def get_screenshot(filename):
	global frame
	feed = get_feed()
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", draw_circle_on_click)
	
	_, frame = feed.read()
	original_frame = frame.copy()

	running = True
	while running:
		cv2.imshow(f"image", frame)

		match cv2.waitKey(1):
			# q : exit
			case 113:
				running = False
			# enter : save the screenshot
			case 13:
				if len(pcb_edge) <= 1: continue
				# Get the rotation angle
				dx = pcb_edge[0][0] - pcb_edge[1][0]
				dy = pcb_edge[0][1] - pcb_edge[1][1]
				rot_angle = np.rad2deg(np.arctan(dy/dx))
				
				h, w = frame.shape[:2]
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

				# subtract old image center (bringing image back to origo) and adding the new image center coordinates
				matrix[0, 2] += bound_w/2 - origin[0]
				matrix[1, 2] += bound_h/2 - origin[1]

				new_frame = cv2.warpAffine(original_frame, matrix, (bound_w,bound_h))


				# transform points
				points = np.array(pcb_edge)
				ones = np.ones(shape=(len(points), 1))
				points_ones = np.hstack([points, ones])
				transformed_points = matrix.dot(points_ones.T).T
				# print(points)
				# print(ones)
				# print(points_ones)
				
				mins, maxs = get_xy_minmax(transformed_points)

				# new_frame = cv2.rectangle(new_frame, mins, maxs, (255,0,0), 2)

				rect = (mins[0], mins[1], maxs[0]-mins[0], maxs[1]-mins[1])

				crop = getSubRect(new_frame, rect)
				cv2.imwrite(filename, crop)
				cv2.imshow("image", crop)
				cv2.waitKey(0)
				running = False

			# delete : Delete point
			case 8:
				if len(pcb_edge) <= 0: continue
				pcb_edge.pop()
				frame = original_frame.copy()
				for point in pcb_edge:
					x,y = point
					frame = cv2.circle(frame, (x, y), 5, (0,0,255), -5)


if __name__ == "__main__":
	get_screenshot("temp.png")