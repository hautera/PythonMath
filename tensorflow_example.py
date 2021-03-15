import tensorflow as tf 
from tensorflow import keras 

class Linear(keras.layers.Layer):
    """y = w.x + b"""

    def __init__(self, units=32):
        super(Linear, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True,
        )
        self.b = self.add_weight(
            shape=(self.units,), initializer="random_normal", trainable=True
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b



(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()

dataset = tf.data.Dataset.from_tensor_slices(
	((x_train.reshape(60000, 784).astype("float32") / 255 ), y_train))
dataset = dataset.shuffle(buffer_size=1024).batch(64)

linear_layer = Linear(10)

#Instalize a loss function that expects integer targets 
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.SGD(learning_rate=1e-3)

for step, (x, y) in enumerate(dataset):
	with tf.GradientTape() as tape: 

		logits = linear_layer(x) 
		loss = loss_fn(y,logits)

		gradients = tape.gradient(loss, linear_layer.trainable_weights)
		optimizer.apply_gradients(zip(gradients, linear_layer.trainable_weights))

		# Logging.
	if step % 100 == 0:
		print("Step:", step, "Loss:", float(loss))

