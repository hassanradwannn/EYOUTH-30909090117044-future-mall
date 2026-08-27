"""Future Mall Product Classifier
Project ID: EYOUTH-30909090117044

This small offline classifier uses the supplied Fruits, Vegetables, and Dairy
training folders. It is intentionally simple: each image becomes a small RGB
colour grid, then the program compares test images with the average image for
each category.
"""

from pathlib import Path

import numpy as np
from PIL import Image


# The folders used for training.
CATEGORIES = ["fruit", "veg", "dairy"]
BASE_FOLDER = Path(__file__).parent / "data"
TRAINING_FOLDER = BASE_FOLDER / "training"
TEST_FOLDER = BASE_FOLDER / "test"


def image_to_features(image_path):
    """Resize one image and turn it into simple numeric RGB features."""
    image = Image.open(image_path).convert("RGB")
    image = image.resize((32, 32))
    pixels = np.array(image, dtype=np.float32) / 255.0
    return pixels.flatten()


def train_classifier():
    """Find the average feature values for each category."""
    class_averages = {}

    for category in CATEGORIES:
        features = []
        category_folder = TRAINING_FOLDER / category

        for image_path in category_folder.glob("*.jpg"):
            features.append(image_to_features(image_path))

        if not features:
            raise ValueError("No training images found for " + category)

        class_averages[category] = np.mean(features, axis=0)
        print(category, "training images:", len(features))

    return class_averages


def predict_image(image_path, class_averages):
    """Return the closest category and a simple confidence percentage."""
    test_features = image_to_features(image_path)
    distances = {}

    for category in CATEGORIES:
        distance = np.linalg.norm(test_features - class_averages[category])
        distances[category] = distance

    prediction = min(distances, key=distances.get)

    # This confidence is based on the relative distance to all three averages.
    total_distance = sum(distances.values())
    confidence = (1 - distances[prediction] / total_distance) * 100

    return prediction, confidence


def main():
    class_averages = train_classifier()
    print("\nTest results")
    print("-" * 55)

    for image_path in TEST_FOLDER.glob("*.jpg"):
        prediction, confidence = predict_image(image_path, class_averages)
        print("Image:", image_path.name)
        print("Prediction:", prediction)
        print("Confidence: {:.2f}%".format(confidence))
        print("-" * 55)


if __name__ == "__main__":
    main()
