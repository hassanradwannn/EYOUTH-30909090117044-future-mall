"""Future Mall Keras Product Classifier Template
Project ID: EYOUTH-30909090117044

Run this after installing TensorFlow. It uses the supplied training folders.
"""

from pathlib import Path
import tensorflow as tf

DATA_FOLDER = Path(__file__).parent / "data"
TRAINING_FOLDER = DATA_FOLDER / "training"
TEST_FOLDER = DATA_FOLDER / "test"

# Read images from the three category folders.
training_data = tf.keras.utils.image_dataset_from_directory(
    TRAINING_FOLDER,
    image_size=(128, 128),
    batch_size=8,
    shuffle=True
)

class_names = training_data.class_names
print("Categories:", class_names)

# A very small model: resize pixels, find patterns, then choose one category.
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1.0 / 255),
    tf.keras.layers.Conv2D(8, 3, activation="relu"),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train once, then train one additional epoch as the requirement asks.
model.fit(training_data, epochs=1)
model.fit(training_data, epochs=1)

# Save the real Keras model after training.
model.save("EYOUTH-30909090117044_Product Classifier.keras")

# Test each separate image and print its prediction and confidence.
for image_path in TEST_FOLDER.glob("*.jpg"):
    image = tf.keras.utils.load_img(image_path, target_size=(128, 128))
    image_array = tf.keras.utils.img_to_array(image)
    image_array = tf.expand_dims(image_array, 0)
    result = model.predict(image_array, verbose=0)[0]
    best_index = int(tf.argmax(result))
    print(image_path.name, "|", class_names[best_index], "|", float(result[best_index]) * 100)
