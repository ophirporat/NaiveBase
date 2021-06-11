
from model.preprocessing import Preprocessing
from model.model import Model

if __name__ == '__main__':
    pre = Preprocessing("", 3)
    pre.preprocess()
    model = Model(pre.train_df, pre.test_df,2,pre.attributes.keys())
    model.build_model()
    model.classify_records()