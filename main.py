# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

# Scikit-image
import skimage

# PIL
from PIL import Image

model = tf.keras.models.load_model("DigitRecognition.model")

# file = tf.keras.preprocessing.image.load_img("test_digits/0x00.png", target_size=(28, 28))
# file = tf.keras.preprocessing.image.img_to_array(file)[:,:,0]

file = Image.open("test_digits/0x06.png")
file = file.resize((28,28))
file = tf.keras.preprocessing.image.img_to_array(file)[:,:,1]

# file = file.resize((28,28))
# file.save("test_digits/0x04.png", optimize=True, quality=95)

# file = skimage.io.imread("test_digits/0x04.png")[:,:,0]

# file = skimage.transform.resize(file, (28, 28), order=0, anti_aliasing=False)

print(file.shape)

file = 255 - file
file = file / 255.0
file = np.array([file])

# for i in range(file[0].shape[0]):
#     for j in range(file[0].shape[1]):
#         if file[0][i, j] != 0:
#             file[0][i, j] = 1


# file = np.invert(np.array([file]))


plt.imshow(file[0], cmap="binary")
plt.show()

# print(file)

# # print(file.shape, type(file))

# # test_loss, test_acc = model.evaluate(test_img,  test_labels, verbose=2)

# # print('\nTest accuracy:', test_acc)

prediction = model.predict(file)
print(prediction)
print(np.argmax(prediction))

# plt.imshow(file[0])
# plt.show()