# CV-Midterm-Fall-2022-Practical
Ritti Bhogal's Submission for the Fall 2022 CV Midterm - Practical Portion

Prompt 1

The Capture class essentially captured the color frames from a video feed using opencv. Then, it detected plates in each frame using a yolov5 model. The ColorDetection class was designed to determine whether there are more blue or red pixels in a given color frame. The ColorDetection class using thresholding to determine the color of the plate. In several ways, this implementation does the barest of minimums and could use some improvements. An example would be that rather than using red and blue HSV values to determine the color of the plate, it would be better to use a model that is trained to detect blue plates or red plates.

Prompt 2

This solution used the DepthCamera class to take live feed from the realsense depth camera and determine the coordinates of a detected plate's bounding box, and then place an angle offset on the box determined using the X and Y resolution and FOV. While the solution didn't give the correct results, it may have been able to do so with a video feed instead.

Prompt 3

The systemd service file displays the version of pytorch on the Jetson/Xavier right after reboot. The service type "simple" felt most appropriate since the goal of the service file was only to display the version of torch. The launch statement was concise since the service itself is a simple type.
