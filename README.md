# Augmented BOM (Lauzhack 2022 project)
This project is inspired by [InspectAR](https://www.inspectar.com/). The goal is to allow people to **mount**, **toubleshoot** and **inspect** PCBs with ease by showing them what they need in augmented Reality. We've decided to embed the video feed into an already existing web Tool: [Interactive BOM for KiCad.
](https://github.com/openscopeproject/InteractiveHtmlBom). This tool allows us to sort, select, name and filter specific nets, components etc.

> Note: This project has been done as a group of 3 students in only 2 days at the Lauzhack (EPFL Hackathon).

## Demo
![](assets/demo.gif)

## How does it work
In order to get the selected nets and plans from the PCB into a video feed in augmented reality, we've implemented a simple pipeline:
1. `Calibration` : The user gets the board under the camera and put points on the corners of the board (This allows a better edge detection)  
2. `Data extraction` : We Extract selected nets, pads and plans of the PCB from Interactive BOM and Send them to a python server.
3. `Get video feed` : From the server, we get the original video stream of only the PCB from the camera. 
4. `Image warping` : Still on the server, we adapt the nets and pads to the angle and distance of the PCB to fit well.
5. `Merge and send` : We merge the fitted nets and the original video feed into a single feed and send it to the Interactive BOM to show it. 