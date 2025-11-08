# test_defects.py
# Test Script for IoT Defect Detection System

import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("../models/demo_cnn_model.h5")

# Dummy image for testing
sample_image = np.random.rand(1, 64, 64, 3)

pred = model.predict(sample_image)
print("🔍 Predicted Class:", np.argmax(pred))

