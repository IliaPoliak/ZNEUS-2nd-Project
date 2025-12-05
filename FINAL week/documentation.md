# Lizard Nuclei Segmentation

# Project Documentation

## Overview

This project implements a binary nuclei segmentation pipeline using a Residual U-Net architecture on the Lizard nuclear instance segmentation dataset.

The workflow covers:

- Exploratory Data Analysis (EDA)
- Data preprocessing and normalization
- Data split
- Augmentations
- Configuration
- Experiment tracking
- Two experiments:
  - Baseline training on all datasets
  - Cross-dataset generalization

## Dataset Structure

The dataset consists of separate folders for images, labels, and overlays:

```
dataset/
├── lizard*images1/Lizard_Images1/*.png
├── lizard*images2/Lizard_Images2/*.png
├── lizard*labels/Lizard_Labels/Labels/*.mat
├── lizard*labels/Lizard_Labels/info.csv
├── overlay/Overlay/*.jpg
```

**Counts:**

- Images folder 1: 80
- Images folder 2: 158
- Labels (.mat): 238
- Overlay images: 238

**Each `.mat` file contains:**

- `inst_map` — instance segmentation mask
- `id`, `class`, `bbox`, `centroid`

## Exploratory Data Analysis (EDA)

**Label Visualization**

`inst_map` shows high variability in nucleus counts:

- **Typical images:** ~100–300 nuclei
- **Outliers:** >500 nuclei

**Image Size Variability**

Images vary in resolution - patch extraction (512×512) is used to normalize input to the model.

## Preprocessing Pipeline

**Core Steps:**

1. Load full-resolution image + instance mask

2. Convert to binary mask (nucleus = 1, background = 0)

3. Apply:

   - Random crop on training (512×512)
   - Center crop on validation/test

4. Apply consistent augmentations:

   - Horizontal/vertical flips
   - Small rotations (+-10°)

5. Normalize images using ImageNet means/std

6. Convert mask to `{0,1}` tensor

## Dataset Splits

**Global split (80/10/10)**

Applied within each dataset group (dpath, glas, consep, pannuke, crag).

**Cross-dataset setup:**

- Train/Val domains: `dpath`, `glas`, `consep`
- Test-only domains: `pannuke`, `crag`

## Model Architecture: Residual U-Net

**Main components:**

**Blocks**

- DoubleConv

  - Residual pathway
  - BatchNorm
  - Dropout2d (MC-dropout support)

- Down
- Up (with spatial alignment padding)
- OutConv - 1-channel output (binary segmentation)

**Model features:**

- Base channels: 48
- Depth: 5
- Residual connections inside downsampling/upsampling stages
- Optional Monte Carlo Dropout for uncertainty estimation

## Training Configuration

**Hyperparameters:**

```py
image_size: 512
batch_size: 5
num_epochs: 30
learning_rate: 1e-4
weight_decay: 1e-5
optimizer: "Adam"
loss: Dice + BCE + Focal (combined)
patience: 5
```

**Logging**

- Weights & Biases (W&B)
- Gradients + metrics per epoch

## Loss Functions

The loss is a weighted combination of:

- BCEWithLogitsLoss
- Dice Loss
- Focal Loss (α=0.25, γ=2)

Composite loss:

```
0.3 * BCE + 0.2 * Focal + 0.5 * Dice
```

## Metrics

Pixel-wise segmentation metrics:

- Dice score
- IoU
- Pixel accuracy
- Precision
- Recall

## Test-Time Augmentation (TTA)

Final prediction probability = mean over:

- original
- horizontal flip
- vertical flip
- horizontal+vertical flip

## Postprocessing

- Connected component labeling
- Removes small instances (`<20 px`)

## Experiments

**Experiment 1 – Baseline U-Net on All Datasets**

Test performance:

| Metric    | Score  |
| --------- | ------ |
| Dice      | 0.7712 |
| IoU       | 0.6281 |
| Accuracy  | 0.9226 |
| Precision | 0.7723 |
| Recall    | 0.7710 |

**Experiment 2 – Cross-Dataset Generalization**

Train on: dpath, glas, consep
Test on: pannuke, crag

This experiment evaluates how well the model performs on unseen domains.

Test performance:

| Metric    | Score  |
| --------- | ------ |
| Dice      | 0.7201 |
| IoU       | 0.5635 |
| Accuracy  | 0.9116 |
| Precision | 0.6695 |
| Recall    | 0.7844 |

# Conclusion

This project successfully implements a strong nuclei segmentation pipeline using a Residual U-Net on the Lizard dataset. The baseline model achieves solid in-domain performance (Dice ≈ 0.77), showing effective learning of nuclear structures. The cross-dataset experiment demonstrates reasonable generalization to unseen domains, though with expected performance drop. Overall, the combination of preprocessing, augmentations, and TTA produces reliable segmentation results and provides a solid foundation for future improvements or domain adaptation experiments.
