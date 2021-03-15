import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import random
vls = []


def sigmoid(x):
	return 1 / (1+np.exp(-x))


# Stores and produces output for a layer of a neural network
class Layer:
	def __init__(self, input_size, output_size, generation=None, prev_layer=None):
		self.input_size, self.output_size = input_size, output_size
		self.weights = np.random(size=(input_size, output_size))
		self.bias = np.zeros(output_size, dtype=np.float64)
		self.prev_layer = prev_layer
		self.running_activation = 0
		self.num_examples = 0

	def output_size(self):
		return self.output_size

	def __call__(self, x, train=False):
		if len(x) == self.input_size:
			activation = self.weights * x + self.bias
			if train:
				self.running_activation += activation
				self.num_examples += 1 
			return sigmoid(activation)
		else:
			raise ValueError( "Incorrect input size of %d! \nInput size = %d".format(len(x), self.input_size)  )

	#Back propagates the error, and adjusts the layers of the network
	def backprop(self, delta, STEP_SIZE=0.01):
		# calculate ave activation for this layer
		ave_activation = self.running_activation / self.num_examples
		self.running_activation, self.num_examples = 0, 0  # book keeping :)
		
		# chain rulez 
		delta = delta * sigmoid(ave_activation) * sigmoid(ave_activation - 1)
		self.weights -= STEP_SIZE * delta * ave_activation
		self.bias -= STEP_SIZE * delta

		# back propagate error to previous layers 
		if self.prev_layer is not None:
			delta = np.dot(self.weights.T, delta)
			self.prev_layer.backprop(delta, STEP_SIZE=STEP_SIZE)

	def __repr__(self):
		return str(self.weights) + str(self.bias)
		
		
# Shows an image on the screen 
# image_vector is a vector of length 28^2
def show_image(image_vector):
	print(image_vector)
	image = []
	for i in range(28):
		row = []
		for j in range(28):
			row.append(image_vector[i*28+j])
		image.append(row)
	plt.imshow(image)
	plt.show()

# Returns the proper label given an index (0-9)
def label(index):
	ls = [0 for i in range(10)]
	ls[index] = 1
	return ls


# Reads all labels 
def read_labels():
	with open('labels', 'rb') as f:
		f.read(4)
		num_labels = int.from_bytes(f.read(4),byteorder="big")
		list_of_labels = []
		for _ in range(num_labels):
			index = int.from_bytes(f.read(1),byteorder="big")
			list_of_labels.append(label(index))
	return list_of_labels


# Reads all images 
# Returns them as a list of Vectors 
def read_images():
	with open('images', 'rb') as f:
		f.read(4)
		num_images = int.from_bytes(f.read(4),byteorder="big")
		
		num_rows = int.from_bytes(f.read(4),byteorder='big')
		num_cols = int.from_bytes(f.read(4),byteorder='big')
		
		list_of_images = []
		for image in range(num_images):
			image_vector = []
			for i in range(num_rows):
				
				for l in f.read(num_cols):
					image_vector.append(l)
			else:
				image_vector = Vector(image_vector)
				list_of_images.append(image_vector)
		else:
			return list_of_images


class Network():
	
	def __init__(self, X_size):
		self.layers = []
		self.X_size, self.Y_size = X_size, 0


	# Returns the prediction of N(x) 
	def __call__(self, X):
		for Lk in self.layers: 
			X = Lk(X)

		return X
	
	##
	## adds layer to network of given size 
	##
	def append_layer(size):
		if len(self.layers) > 0:
			L0 = self.layers[-1]
		else:
			L0 = self.X_size
		L1 = size	
		temp = Layer(L0, L1)
		self.layers.append(temp) 


	def __len__(self):
		return self.layers[-1].output_size()	

	##
	## Trains the model on X and Y
	##
	def train(X, Y, batch_size=100, STEP_SIZE=0.01):
		pass 


#image = read_images()[0]	
#label = read_labels()[0]	
x = Layer(1, 3)
error = Vector.ones(3)
def_input = Vector.ones(1)
print("Before our backpropagation")
pprint(x)
x.backprop(error,def_input)
print("After our backpropagation")
pprint(x)




		
