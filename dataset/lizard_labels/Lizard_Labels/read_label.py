"""Loading the labels within the Lizard dataset."""

import scipy.io as sio
import numpy as np

label = sio.loadmat('consep_1.mat') #! This filename is a placeholder!

# Load the instance segmentation map.
# This map is of type int32 and contains values from 0 to N, where 0 is background
# and N is the number of nuclei. 
# Shape: (H, W) where H and W is the height and width of the image.
inst_map = label['inst_map'] 

# Load the index array. This determines the mapping between the nuclei in the instance map and the
# corresponing provided categories, bounding boxes and centroids.
nuclei_id = label['id'] # shape (N, 1), where N is the number of nuclei.

# Load the nuclear categories / classes. 
# Shape: (N, 1), where N is the number of nuclei.
classes = label['class']

# Load the bounding boxes.
# Shape: (N, 4), where N is the number of nuclei.
# For each row in the array, the ordering of coordinates is (y1, y2, x1, x2). 
bboxs = label['bbox'] 

# Load the centroids.
# Shape: (N, 2), where N is the number of nuclei.
# For each row in the array, the ordering of coordinates is (x, y).
centroids = label['centroid'] 

# Matching each nucleus with its corresponding class, bbox and centroid:

# Get the unique values in the instance map - each value corresponds to a single nucleus.
unique_values = np.unique(inst_map).tolist()[1:] # remove 0

# Convert nuclei_id to list.
nuclei_id = np.squeeze(nuclei_id).tolist()
for value in unique_values:
	# Get the position of the corresponding value
	idx = nuclei_id.index(value)
	
	class_ = classes[idx]
	bbox = bboxs[idx]
	centroid = centroids[idx]




