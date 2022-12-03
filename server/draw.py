import json
import numpy as np
import cv2 as cv

def get_json_file(filename):
	with open(filename, "r") as f:
		json_file = f.read()
	return dict(json.loads(json_file))

def draw_pcb(pcb_data):
	# Create a black background
	img = np.zeros((720,1280,3), np.uint8)

	# Draw PCB edge cuts
	draw_edge_cuts(pcb_data, img)

	# Show context
	cv.imshow("AugmentedBOM", img)
	cv.waitKey(0)

def scale(pos, ratio):
	for i in range (len(pos)):
		pos[i] *= ratio
	return pos

def draw_edge_cuts(pcb_data, canvas, ratio = 15):
	# Get base offset
	minx = pcb_data["edges_bbox"]["minx"]
	miny = pcb_data["edges_bbox"]["miny"]
	for edge in pcb_data["edges"]:
		#print(edge)
		start = edge["start"]
		start[0] -= minx;start[1] -= miny
		start = scale(start, ratio)
		start = list(map(int,start))

		if edge["type"] == "segment":
			stop = edge["end"]
			stop[0] -= minx;stop[1] -= miny
			stop = scale(stop, ratio)
			stop = list(map(int,stop))
			cv.line(canvas, start, stop, (255,255,255))
		elif edge["type"] == "arc":
			radius = edge["radius"] * ratio
			start_angle = edge["startangle"]
			end_angle = edge["endangle"]
			cv.ellipse(canvas, start, (radius, radius), 0, start_angle, end_angle, (255,255,255))


if __name__ == "__main__":
	pcb_data = get_json_file("data.txt")

	draw_pcb(pcb_data)
	
