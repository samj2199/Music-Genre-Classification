# -*- coding: utf-8 -*-
"""02_train_ann_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/134V3VZoZNz6Vh0wEHCsaftTD_DWKaN3E
"""

# Import necessary libraries
import json
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

# Load data from JSON
def load_mfcc_data(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    features = np.array(data["mfcc_features"])
    labels = np.array(data["labels"])
    return features, labels

# Load and split the data
features, labels = load_mfcc_data(r"./mfcc_data.json")
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Build the model
model = Sequential([
    Flatten(input_shape=(features.shape[1], features.shape[2])),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)