from preprocessing import Preprocessing
from model import Model

if __name__ == '__main__':
    path = "C:\\Users\\morzw\\PycharmProjects\\NaiveBase"
    pre = Preprocessing(path, 3)
    pre.preprocess()
    model = Model(pre.train_df, pre.test_df, 2, pre.attributes.keys(), path)
    model.build_model()
    model.classify_records()
