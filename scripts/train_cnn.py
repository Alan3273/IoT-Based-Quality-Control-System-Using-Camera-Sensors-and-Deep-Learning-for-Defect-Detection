
# train_cnn.py
# Simple CNN Training Script (Demo for IoT Defect Detection System)
# Author: Bodanapati Vinay, Lovely Professional University

import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Dummy dataset (for demo)
X_train = np.random.rand(100, 64, 64, 3)
y_train = np.random.randint(0, 2, 100)

# CNN model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=3, verbose=1)

# Save model
model.save("../models/demo_cnn_model.h5")
print("✅ Model training complete and saved!")
