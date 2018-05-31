import cv2
from image import Image 
from detector import Detector
from classifier import Classifier
import time

video_capture = cv2.VideoCapture(0) # Create instance of videoCapture on Default WebCamera

haarcascade_classifier = Classifier("alt", "eye_glasses", "smile") # Create instance of Classifier with haarcascade classifier xml preferred.

video_capture.open(0) # Open Default WebCamera
time.sleep(5) # Wait Camera to respond
out = cv2.VideoWriter('output.avi', 0, 4.5, (640,480))
while True: 
	ret, image = video_capture.read()
	detector = Detector(image, 1.1, 5, (30, 30), cv2.DIST_L2, haarcascade_classifier,video_capture)
	detector.detect(image,video_capture)
	cv2.imshow("Video", image)

	while(video_capture.isOpened()):
			    #ret, frame = self.cap.read()
			    #if ret==True:
			        # write the flipped frame
		out.write(image)

			        #cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		key = cv2.waitKey(30) & 0xff
		if key == 27: # If Escape key is pressed video-capture ends.
			break
		else:
			break

			# Release everything if job is finished
	
	key = cv2.waitKey(30) & 0xff
	if key == 27: # If Escape key is pressed video-capture ends.
		break
out.release()
video_capture.release()
cv2.destroyAllWindows()
