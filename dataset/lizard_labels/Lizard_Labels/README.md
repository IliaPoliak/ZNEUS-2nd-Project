Lizard Dataset for Nuclear Instance Segmentation and Classification

The dataset contains image regions extracted from colon whole-slide images at 20x objective magnification along with their corresponding labels. Each label provides:

- Instance segmentation map
- Category of each nucleus
- Bounding box of each nucleus
- Centroid of each nucleus

The nuclear categories provided as part of this dataset are:

- Class 1: Neutrophil
- Class 2: Epithelial
- Class 3: Lymphocyte
- Class 4: Plasma
- Class 5: Neutrophil
- Class 6: Connective tissue

Each label is stored as a mat file. We provide some sample code (read_label.py) to provide information on how to read the labels. It should be noted that models trained on data at 40x may need to be adapted appropriately.

If using any part of this dataset, you must cite the below publication, which describes the dataset in more detail:

Graham, Simon, et al. "Lizard: A Large-Scale Dataset for Colonic Nuclear Instance Segmentation and Classification." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

IMPORTANT: Note, that the dataset provided here is for research purposes only. Commercial use is not allowed. The data is held under the following license: Attribution-NonCommercial-ShareAlike 4.0 International.

We are currently holding back the TCGA part of this dataset as we wish to use it in an upcoming challenge. This will be released in the near future. 

For further information, please visit warwick.ac.uk/lizard-dataset.
Contact: simon.graham@warwick.ac.uk 

