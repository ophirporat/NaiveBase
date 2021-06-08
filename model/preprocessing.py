import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer


class Preprocessing:
    def __init__(self, path):
        self.attributes = {}
        self.path = path
        self.train_df = pd.read_csv(path + "../train.csv")

    def read_structure_file(self):
        f = open("path +/Structure.txt", "r")
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

    def equal_width_partitioning(self, attribute_name):
        arr1 = self.train_df[attribute_name].values
        m = 3
        w = int((max(arr1) - min(arr1)) / m)
        min1 = min(arr1)
        arr = []
        for i in range(0, m + 1):
            arr = arr + [min1 + w * i]
        for j in self.train_df.index:
            if self.train_df.at[j, attribute_name] <= arr[0]:
                self.train_df.at[j, attribute_name] = 1
            elif arr[0] < self.train_df.at[j, attribute_name] <= arr[1]:
                self.train_df.at[j, attribute_name] = 2
            else:
                self.train_df.at[j, attribute_name] = 3
        pass

    def simplifiy_labels(self, attribute_name):
        pass

    def data_preparation(self):
        for key, value in self.attributes.items():
            if key == "class":
                continue
            if value == "numeric":
                self.train_df[key] = self.train_df[key].fillna(self.train_df[key].mean())
                self.equal_width_partitioning(key)

            else:
                self.train_df[key] = self.train_df[key].fillna(self.train_df[key].mode().iloc[0])
                self.simplifiy_labels(key)


m = Preprocessing("..")
m.read_structure_file()
m.data_preparation()
