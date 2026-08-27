"""Two-epoch experiment for the Future Mall image classifier.

This file is separate from the simple baseline classifier. It uses a small
softmax model so that a real training epoch can be compared with a second epoch.
"""

from pathlib import Path

import numpy as np
from PIL import Image


CATEGORIES = ["fruit", "veg", "dairy"]
BASE_FOLDER = Path(__file__).parent / "data"


def image_to_features(image_path):
    image = Image.open(image_path).convert("RGB")
    image = image.resize((16, 16))
    return np.asarray(image, dtype=np.float32).reshape(-1) / 255.0


def softmax(values):
    values = values - values.max(axis=1, keepdims=True)
    exponentials = np.exp(values)
    return exponentials / exponentials.sum(axis=1, keepdims=True)


def load_training_data():
    features = []
    labels = []

    for label, category in enumerate(CATEGORIES):
        for image_path in (BASE_FOLDER / "training" / category).glob("*.jpg"):
            features.append(image_to_features(image_path))
            labels.append(label)

    return np.array(features), np.array(labels)


def test_model(weights, bias, mean, std):
    results = []

    for image_path in (BASE_FOLDER / "test").glob("*.jpg"):
        features = (image_to_features(image_path) - mean) / std
        scores = features @ weights + bias
        scores = np.exp(scores - scores.max())
        probabilities = scores / scores.sum()
        label = int(probabilities.argmax())
        results.append((image_path.name, CATEGORIES[label], probabilities[label] * 100))

    return results


def main():
    features, labels = load_training_data()
    mean = features.mean(axis=0)
    std = features.std(axis=0) + 0.000001
    features = (features - mean) / std

    # Fixed seed makes the experiment reproducible.
    np.random.seed(7)
    weights = np.zeros((features.shape[1], len(CATEGORIES)))
    bias = np.zeros(len(CATEGORIES))
    targets = np.eye(len(CATEGORIES))[labels]

    for epoch in range(1, 3):
        probabilities = softmax(features @ weights + bias)
        error = (probabilities - targets) / len(features)
        weights = weights - 0.05 * (features.T @ error)
        bias = bias - 0.05 * error.sum(axis=0)

        print("Epoch", epoch)
        for name, prediction, confidence in test_model(weights, bias, mean, std):
            print(name, "|", prediction, "| {:.2f}%".format(confidence))
        print()


if __name__ == "__main__":
    main()
