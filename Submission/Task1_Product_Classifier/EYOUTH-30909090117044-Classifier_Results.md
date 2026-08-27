# Product Classifier Results

**Project ID:** EYOUTH-30909090117044

## Training data used

| Category | Training images available |
|---|---:|
| fruit | 9 |
| veg | 10 |
| dairy | 9 |

The supplied folders contain 28 training images, not 30. The classifier uses every supplied training image.

## Test results

| Image | Prediction | Confidence | Note |
|---|---|---:|---|
| `360_F_231842968_qThCnmslPbEAwhg7nuW9rAy8qRNhRli7.jpg` | fruit | 68.98% | Recorded exactly as produced by the program. |
| `Marketvegetables.jpg` | dairy | 69.37% | The prediction is incorrect for a vegetables image; it is recorded honestly as required. |
| `Oranges_-_whole-halved-segment.jpg` | fruit | 69.03% | Recorded exactly as produced by the program. |

## Classifier method

The program resizes each image to a small RGB grid. During training it calculates an average feature set for each category, then it compares a new image with the three category averages. This is a simple local substitute because the supplied `Future_Mall_Product_Classifier_Template.py` file was not available.
