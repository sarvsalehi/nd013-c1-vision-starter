import argparse
import glob
import os
import random
import shutil
import numpy as np
import sklearn.model_selection

train_test_split= sklearn.model_selection.train_test_split


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    # take all the tfrecord filename from source
    dataset = glob.glob(source+'/*.tfrecord') 
    #default percentage for train is 75%
    train, val_tr = train_test_split(dataset, test_size=0.2)
    #from 25% of the whole 75% is stored for test and the rest for validation
    test, val = train_test_split(val_tr)
    # create paths for storing train, val and test files
    for file_path in train:
        shutil.move(file_path, os.path.join(destination, "train",os.path.basename(file_path)))
    for file_path in test:
        shutil.move(file_path, os.path.join(destination, "test",os.path.basename(file_path)))
    for file_path in val:
        shutil.move(file_path, os.path.join(destination, "val",os.path.basename(file_path)))
     


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', required=True,
                        help='source data directory')
    parser.add_argument('--destination', required=True,
                        help='destination data directory')
    args = parser.parse_args()

    split(args.source, args.destination)