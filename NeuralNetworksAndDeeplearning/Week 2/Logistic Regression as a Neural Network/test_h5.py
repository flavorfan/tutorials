# from lr_utils import load_dataset
import numpy as np
import h5py

f = h5py.File('datasets/train_catvnoncat.h5', "r")
f.keys()

# train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
