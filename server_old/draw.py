import json
import numpy as np
import cv2 as cv
import math
import copy

def get_json_file(filename):
	with open(filename, "r") as f:
		json_file = f.read()
	return dict(json.loads(json_file))

def rotate(origin, point, angle):
	angle = np.deg2rad(angle)
	ox, oy = origin
	px, py = point

	qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
	qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
	return int(qx), int(qy)

def check_if_th(dico):
	if dico["pads"] == []:
		return True
	
	for p in dico["pads"]:
		if p["type"] == "th":
			return True
	return False

def draw_pcb(dico, net_list, comp_list, ratio = 15):
	pcb_data = copy.deepcopy(dico)
	# Create a black background
	w_x = int(pcb_data["edges_bbox"]["maxx"] * ratio) - int(pcb_data["edges_bbox"]["minx"] * ratio)
	w_y = int(pcb_data["edges_bbox"]["maxy"] * ratio) - int(pcb_data["edges_bbox"]["miny"] * ratio)
	color = (0, 0, 0)
	#color = (48, 44, 37)
	img = np.full((w_y, w_x, 3), color,np.uint8)

	# Draw PCB edge cuts
	draw_edge_cuts(pcb_data, img, ratio)

	# Draw PCB net
	draw_net(pcb_data, img, ratio, net_list)

	# Draw Componants bounding box
	draw_bounding_box(pcb_data, img, ratio, comp_list)

	# Draw Componants pads
	draw_pads(pcb_data, img, ratio, comp_list)

	cv.imwrite("circuit_draw.png", img)
	# Show context
	#cv.imshow("AugmentedBOM", img)
	#cv.waitKey(0)

def scale(pos, ratio):
	for i in range (len(pos)):
		pos[i] *= ratio
	return pos

def draw_edge_cuts(pcb_data , canvas, ratio = 1, color=(255, 255, 255)):
	
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
			radius = int(edge["radius"] * ratio)
			start_angle = edge["startangle"]
			end_angle = edge["endangle"]
			cv.ellipse(canvas, start, (radius, radius), 0, start_angle, end_angle, color)

def draw_net(pcb_data, canvas, ratio, net_list):
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
			if len(net_list) > 0 and track["net"] not in net_list:
				continue
			
			start = track["start"]
			start[0] -= minx;start[1] -= miny
			start = scale(start, ratio)
			start = list(map(int,start))

			stop = track["end"]
			stop[0] -= minx;stop[1] -= miny
			stop = scale(stop, ratio)
			stop = list(map(int,stop))

			width = track["width"] * ratio / 1.5
			if layer == "B":
				color = bg_color
			elif layer == "F":
				color = fg_color
			else:
				color = oth_color
			cv.line(canvas, start, stop, color, int(width))

def draw_bounding_box(pcb_data, canvas, ratio, comp_list):
	# Get base offset
	minx = pcb_data["edges_bbox"]["minx"]
	miny = pcb_data["edges_bbox"]["miny"]

	for f in pcb_data["footprints"]:
		if check_if_th(f):
			continue

		if len(comp_list) > 0 and f["ref"] not in comp_list:
				continue

		pos = f["bbox"]["pos"]
		pos[0] = (pos[0] - minx) * ratio 
		pos[1] = (pos[1] - miny) * ratio 
		size = f["bbox"]["size"]
		size[0] = size[0] * ratio
		size[1] = size[1] * ratio
		start = (int(pos[0] - size[0] / 2), int(pos[1] - size[1] / 2))
		stop = (int(pos[0] + size[0] / 2), int(pos[1] + size[1] / 2))

		angle = f["bbox"]["angle"]
		p1 = rotate(pos, (start[0], stop[1]), angle)
		p2 = rotate(pos, (stop[0], start[1]), angle)
		start = rotate(pos, start, angle)
		stop = rotate(pos, stop, angle)
		
		color = (255, 255, 255)
		cv.line(canvas, start, p1, color, 2)
		cv.line(canvas, start, p2, color, 2)
		cv.line(canvas, stop, p1, color, 2)
		cv.line(canvas, stop, p2, color, 2)

def draw_pads(pcb_data, canvas, ratio, comp_list):
	# Get base offset
	minx = pcb_data["edges_bbox"]["minx"]
	miny = pcb_data["edges_bbox"]["miny"]

	for f in pcb_data["footprints"]:
		if len(comp_list) > 0 and f["ref"] not in comp_list:
			continue
		for p in f["pads"]:
			pos = p["pos"]
			pos[0] = int((pos[0] - minx) * ratio) 
			pos[1] = int((pos[1] - miny) * ratio)
			size = p["size"]
			size[0] = int(size[0] * ratio / 2)
			size[1] = int(size[1] * ratio / 2)
			
			
			color = (255, 255, 255)
			if p["shape"] == "circle" or p["shape"] == "oval":
				cv.circle(canvas, pos, int(size[0] / 1.5), color, 2)
			elif p["shape"] == "rect" or p["shape"] == "roundrect":
				start = (int(pos[0] - size[0] / 2), int(pos[1] - size[1] / 2))
				stop = (int(pos[0] + size[0] / 2), int(pos[1] + size[1] / 2))
				angle = p["angle"]
				p1 = rotate(pos, (start[0], stop[1]), angle)
				p2 = rotate(pos, (stop[0], start[1]), angle)
				start = rotate(pos, start, angle)
				stop = rotate(pos, stop, angle)
				cv.line(canvas, start, p1, color, 2)
				cv.line(canvas, start, p2, color, 2)
				cv.line(canvas, stop, p1, color, 2)
				cv.line(canvas, stop, p2, color, 2)
				


if __name__ == "__main__":
	#pcb_data = get_json_file("data.txt")

	#draw_pcb(pcb_data, [], [], 15)
	pass
