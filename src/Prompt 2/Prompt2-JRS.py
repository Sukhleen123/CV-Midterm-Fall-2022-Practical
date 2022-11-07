from utils.DepthCamera import *
from utils.DepthCamera import DepthCamera

# Configure depth and color streams
cam = DepthCamera()

oldCords = None
depth = None

while True:
    # Start Video Capture
    try:
        # get depth frame and color frame
        ret, depth_frame, color_frame = cam.get_frame()
    except:
        print("Error getting frame")

    # If frame is not empty
    if ret:

        key = cv2.waitKey(1)
        if key == 27:
            break

        # Get bbox coordinates from color frame
        try:
            coordinates = cam.get_coordinates(color_frame, cam.model)

        except:
            print("Error getting cordinates\n")

        if coordinates != None:
            # Get Median Depth from depth frame
            try:
                depth = cam.process_frame(
                    depth_frame, coordinates[0], coordinates[1], coordinates[2], coordinates[3])
            except:
                print("Error processing_frame")

            # Debug mode
            if Debug_flag == 1:
                print("In: ", coordinates)
                print(coordinates)
                print(depth)
                cam.show_frame(color_frame, depth_frame, depth, coordinates)

            # calculate final coordinates with offset
            final_cords = cam.det_move(
                (coordinates[0]+coordinates[2])/2,
                (coordinates[1]+coordinates[3])/2,
                640,
                480)
            print(final_cords)