import json
import numpy as np
import cv2 as cv

def get_json_file(filename):
	with open(filename, "r") as f:
		json_file = f.read()
	return dict(json.loads(json_file))

def draw_pcb(pcb_data, ratio = 15):
	# Create a black background
	w_x = int(pcb_data["edges_bbox"]["maxx"] * ratio) - int(pcb_data["edges_bbox"]["minx"] * ratio)
	w_y = int(pcb_data["edges_bbox"]["maxy"] * ratio) - int(pcb_data["edges_bbox"]["miny"] * ratio)
	img = np.full((w_y, w_x, 3), (48, 44, 37),np.uint8)

	# Draw PCB edge cuts
	draw_edge_cuts(pcb_data, img, ratio)

	# Draw PCB net
	draw_net(pcb_data, img, ratio)

	# Show context
	cv.imshow("AugmentedBOM", img)
	cv.waitKey(0)

def scale(pos, ratio):
	for i in range (len(pos)):
		pos[i] *= ratio
	return pos

def draw_edge_cuts(pcb_data, canvas, ratio = 1, color=(255, 255, 255)):
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
			cv.line(canvas, start, stop, color)
		elif edge["type"] == "arc":
			radius = edge["radius"] * ratio
			start_angle = edge["startangle"]
			end_angle = edge["endangle"]
			cv.ellipse(canvas, start, (radius, radius), 0, start_angle, end_angle, color)

def draw_net(pcb_data, canvas, ratio):
	# Get base offset
	minx = pcb_data["edges_bbox"]["minx"]
	miny = pcb_data["edges_bbox"]["miny"]

	fg_color = (52, 52, 200)
	bg_color = (196, 127, 77)
	oth_color = (182, 89, 155)

	# Reverse layer drawing
	layers = []
	for layer in pcb_data["tracks"]:
		layers.append(layer)
	
	# For each layer
	for layer in layers[::-1]:
		# Draw each tracks of the layer
		for track in pcb_data["tracks"][layer]:
			#print(f"{layer=} {track}")
			start = track["start"]
			start[0] -= minx;start[1] -= miny
			start = scale(start, ratio)
			start = list(map(int,start))

			stop = track["end"]
			stop[0] -= minx;stop[1] -= miny
			stop = scale(stop, ratio)
			stop = list(map(int,stop))

			width = track["width"] * ratio / 2
			if layer == "B":
				color = bg_color
			elif layer == "F":
				color = fg_color
			else:
				color = oth_color
			cv.line(canvas, start, stop, color, int(width))


if __name__ == "__main__":
	pcb_data = get_json_file("data.txt")

	draw_pcb(pcb_data, 15)
	
