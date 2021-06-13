import pandas as pd
from sklearn.preprocessing import LabelEncoder


class Preprocessing:
    def __init__(self, path, num_of_bins):
        self.attributes = {}
        self.path = path
        self.train_df = pd.read_csv(path+"\\train.csv")
        self.test_df = pd.read_csv(path+"\\test.csv")
        self.num_of_bins = num_of_bins

    # -- Reads the structure file --
    def read_structure_file(self):
        f = open(self.path + "\\Structure.txt", "r")
        line = f.readline()
        while line:
            if line.__contains__("{"):
                attribute_name = line.split(' ')[1]
                attribute_values = line.split("{")[1].split("}")[0].split(",")
            else:
                attribute_name = line.split(' ')[1]
                attribute_values = "numeric"

            self.attributes[attribute_name] = attribute_values
            line = f.readline()

    # -- Discretization of equal width --
    def equal_width_partitioning(self, attribute_name):
        arr1 = self.train_df[attribute_name].values
        # arr2 = self.test_df[attribute_name].values
        w1 = int((max(arr1) - min(arr1)) / self.num_of_bins)
        # w2 = int((max(arr2) - min(arr2)) / self.num_of_bins)
        min1 = min(arr1)
        # min2 = min(arr2)
        arr = []
        for i in range(0, self.num_of_bins + 1):
            arr = arr + [min1 + w1 * i]
        for j in self.train_df.index:
            if self.train_df.at[j, attribute_name] <= arr[0]:
                self.train_df.at[j, attribute_name] = 1
            elif arr[0] < self.train_df.at[j, attribute_name] <= arr[1]:
                self.train_df.at[j, attribute_name] = 2
            else:
                self.train_df.at[j, attribute_name] = 3
        for k in self.test_df.index:
            if self.test_df.at[k, attribute_name] <= arr[0]:
                self.test_df.at[k, attribute_name] = 1
            elif arr[0] < self.test_df.at[k, attribute_name] <= arr[1]:
                self.test_df.at[k, attribute_name] = 2
            else:
                self.test_df.at[k, attribute_name] = 3
        pass

    # -- Encodes attribute's values --
    def simplify_labels(self, attribute_name):
        self.train_df[attribute_name] = LabelEncoder().fit_transform(self.train_df[attribute_name])
        self.test_df[attribute_name] = LabelEncoder().fit_transform(self.test_df[attribute_name])
        pass

    # -- Preparing the data --
    def data_preparation(self):
        for key, value in self.attributes.items():
            if key == "class":
                continue
            # for numeric variable fill na with mean and do equal width discretization
            if value == "numeric":
                self.train_df[key] = self.train_df[key].fillna(self.train_df[key].mean())
                self.test_df[key] = self.test_df[key].fillna(self.test_df[key].mean())
                self.equal_width_partitioning(key)
            # for categorical variable fill na with mode and encodes attribute's values
            else:
                self.train_df[key] = self.train_df[key].fillna(self.train_df[key].mode().iloc[0])
                self.test_df[key] = self.test_df[key].fillna(self.test_df[key].mode().iloc[0])
                self.simplify_labels(key)

    # -- Start preprocessing from here! --
    def preprocess(self):
        self.read_structure_file()
        self.data_preparation()
        self.attributes.pop("class")
