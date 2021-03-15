from svm import SVM
import picamera
from gpiozero import LED 
import time
import numpy as np

def load():
	file_name = "Samples/"	
	positives = []
	with np.load(file_name + "positive.npz") as file:
		for ar in file:
			positives.append(file[ar])
	positives = positives[0].reshape((20,230400))

	negatives = []
	with np.load(file_name + "negative.npz") as file:
		for ar in file:
			negatives.append(file[ar])
	# hard code for 320 x 240 resolution 
	negatives = negatives[0].reshape((20,230400))
	
	
	temp = np.ones(len(positives))
	temp2 = -1 * np.ones(len(negatives))
	
	X = np.concatenate((positives,negatives))
	Y = np.concatenate((temp, temp2))

	return X, Y

if __name__ == '__main__':
	X,Y = load()
	model = SVM()
	model.fit(X,Y)
	with picamera.PiCamera() as camera:
		led = LED(17)
		camera.resolution = (320,240)
		camera.framerate = 24 
		while True:
			time.sleep(2)
			output = np.empty((240,320,3), dtype=np.uint8)
			camera.capture(output, 'rgb')
			output = output.reshape((230400))
			if model.predict(output) == 1:
				led.on()
			else:
				led.off()
