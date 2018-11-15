import os
import glob
import random
import csv

class data_provider():

    def __init__(self, valid_percentage, test_percentage):
        self.training_set = []
        self.valid_set = []
        self.test_set = []
        self.valid_percentage = valid_percentage
        self.test_percentage = test_percentage

    def get_data_from_dir(self, img_dir):
        # get all the categories in the data directory
        sub_dirs = os.listdir(img_dir)
        for sub_dir in sub_dirs:
            # string for glob function to extract all the jpg images in sub_directory
            glob_var = os.path.join(img_dir, sub_dir, '*.jpg')
            img_paths = glob.glob(glob_var)
            training_set, valid_set, test_set = self.dataset_separate(img_paths, sub_dir)
            self.training_set.extend(training_set)
            self.valid_set.extend(valid_set)
            self.test_set.extend(test_set)

    def get_data_from_csv(self, csv_path):
        with open(csv_path, 'r') as f:
            self.training_set.extend(f.next)
            self.valid_set.extend(f.next)
            self.test_set.extend(f.next)

    def dataset_separate(self, img_paths, category_name):
        random.shuffle(img_paths)
        num_img = len(img_paths)
        if num_img < 10:
            print('the data set of {} is too small!'.format(category_name))
        num_test_set = int(self.test_percentage*num_img)
        num_valid_set = int(self.valid_percentage*num_img)
        test_set = img_paths[:num_test_set]
        valid_set = img_paths[num_test_set:num_test_set+num_valid_set]
        training_set = img_paths[num_test_set+num_valid_set:]
        return training_set, valid_set, test_set

    def get_training_set(self):
        return self.training_set

    def get_valid_set(self):
        return self.valid_set
    
    def get_test_set(self):
        return self.test_set

    def write_dataset_to_file(self, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for dataset in [self.training_set, self.valid_set, self.test_set]:
                writer.writerow(dataset)
