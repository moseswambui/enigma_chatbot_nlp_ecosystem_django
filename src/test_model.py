# scripts/test_model.py

import tensorflow as tf
import os

# Load the test data (using MNIST as an example)
(_, _), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Normalize the images
test_images = test_images / 255.0

# Load the trained model
model_path = "../models/my_model.keras"
if not os.path.exists(model_path):
    raise ValueError(f"Model not found at {model_path}")

model = tf.keras.models.load_model(model_path)

# Evaluate the model
loss, accuracy = model.evaluate(test_images, test_labels)

print(f"Test Accuracy: {accuracy*100:.2f}%")
