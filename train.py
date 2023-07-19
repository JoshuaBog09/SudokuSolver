# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# Helper functions
def showFigure(figure) -> None:
    plt.figure()
    plt.imshow(figure)
    plt.colorbar()
    plt.grid(False)
    plt.show()

print(tf.__version__)

data_set = tf.keras.datasets.mnist

data = list(map(str, list(range(0,10))))

(train_img, train_labels), (test_img, test_labels) = data_set.load_data()

train_img = train_img / 255.0
test_img = test_img / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer='adam',
              loss="sparse_categorical_crossentropy",
              metrics=['accuracy'])

model.fit(train_img, train_labels, epochs=12)

model.save("DigitRecognition.model")