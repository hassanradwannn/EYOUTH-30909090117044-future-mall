"""Future Mall Keras Product Classifier
Project ID: EYOUTH-30909090117044

This program uses the supplied training images. It trains for one epoch,
tests the three new images, then trains for one more epoch and compares the
confidence values. Finally, it saves the Keras model inside a ZIP file.
"""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

import numpy as np
import tensorflow as tf


# The category folder names are kept in this order for clear results.
CATEGORIES = ["fruit", "veg", "dairy"]
IMAGE_SIZE = (64, 64)
BASE_FOLDER = Path(__file__).parent.parent / "Task1_Product_Classifier" / "data"
TRAINING_FOLDER = BASE_FOLDER / "training"
TEST_FOLDER = BASE_FOLDER / "test"
MODEL_FILE = "EYOUTH-30909090117044_Product Classifier.keras"
ZIP_FILE = "EYOUTH-30909090117044_Product Classifier.zip"


def load_image(image_path):
    """Open one image, resize it, and return its pixel values."""
    image = tf.keras.utils.load_img(image_path, target_size=IMAGE_SIZE)
    return tf.keras.utils.img_to_array(image)


def load_training_data():
    """Read every training image from the three category folders."""
    images = []
    labels = []

    for label, category in enumerate(CATEGORIES):
        category_folder = TRAINING_FOLDER / category
        image_paths = list(category_folder.glob("*.jpg"))
        print(category, "training images:", len(image_paths))

        for image_path in image_paths:
            images.append(load_image(image_path))
            labels.append(label)

    return np.array(images), np.array(labels)


def test_images(model):
    """Predict every test image and return the results."""
    results = []

    for image_path in TEST_FOLDER.glob("*.jpg"):
        image = load_image(image_path)
        image = np.expand_dims(image, axis=0)
        probabilities = model.predict(image, verbose=0)[0]
        best_index = int(np.argmax(probabilities))
        confidence = float(probabilities[best_index] * 100)
        results.append((image_path.name, CATEGORIES[best_index], confidence))

    return results


def print_results(title, results):
    """Print each filename, prediction, and confidence."""
    print("\n" + title)
    print("-" * 60)
    for name, prediction, confidence in results:
        print(name, "|", prediction, "| {:.2f}%".format(confidence))


def main():
    # The fixed seed makes this small training experiment repeatable.
    tf.keras.utils.set_random_seed(7)
    images, labels = load_training_data()

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(64, 64, 3)),
        tf.keras.layers.Rescaling(1.0 / 255),
        tf.keras.layers.Conv2D(8, 3, activation="relu"),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(16, activation="relu"),
        tf.keras.layers.Dense(3, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    # First training epoch and its test confidence.
    model.fit(images, labels, epochs=1, batch_size=4, verbose=0)
    first_results = test_images(model)
    print_results("Results after epoch 1", first_results)

    # One additional epoch, as required, then test again.
    model.fit(images, labels, epochs=1, batch_size=4, verbose=0)
    second_results = test_images(model)
    print_results("Results after epoch 2", second_results)

    print("\nConfidence comparison")
    for first, second in zip(first_results, second_results):
        change = second[2] - first[2]
        print(first[0], "| {:.2f} percentage points".format(change))

    # Save the real trained Keras model, then place it in the required ZIP.
    model.save(MODEL_FILE)
    with ZipFile(ZIP_FILE, "w", ZIP_DEFLATED) as zip_file:
        zip_file.write(MODEL_FILE)
    print("\nSaved:", ZIP_FILE)


if __name__ == "__main__":
    main()
