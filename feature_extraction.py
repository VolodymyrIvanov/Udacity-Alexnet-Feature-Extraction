import time
import tensorflow as tf
import numpy as np
import pandas as pd
from scipy.misc import imread
from caffe_classes import class_names
from alexnet import alexnet

sign_names = pd.read_csv('signnames.csv')
nb_classes = 43

# TODO: define placeholders and resize operation
x = tf.placeholder(tf.float32, (None, 32, 32, 3))
resized = tf.image.resize_images(x, (227, 227))

# TODO: setup AlexNet for feature extraction and
# define the last layer.
fc7 = alexnet(..., feature_extract=True)

# TODO: assign the softmax of the logits to probs
probs = ...

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# Read Images
im1 = (imread("./construction.jpg")[:, :, :3]).astype(np.float32)
im1 = im1 - np.mean(im1)

im2 = (imread("./stop.jpg")[:, :, :3]).astype(np.float32)
im2 = im2 - np.mean(im2)

# Run Inference
t = time.time()
output = sess.run(probs, feed_dict={x: [im1, im2]})

# Print Output
for input_im_ind in range(output.shape[0]):
    inds = np.argsort(output)[input_im_ind, :]
    print("Image", input_im_ind)
    for i in range(5):
        print("%s: %.3f" % (class_names[inds[-1 - i]], output[input_im_ind, inds[-1 - i]]))
        print("%s: %.3f" % (sign_names.ix[inds[-1 - i]][1], output[input_im_ind, inds[-1 - i]]))
    print()

print("Time: %.3f seconds" % (time.time() - t))
