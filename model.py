from sklearn.naive_bayes import CategoricalNB


import utils


class Model:
    def __init__(self, train, test, m, attributes, path):
        self.x_train = train[attributes]
        self.y_train = train["class"]
        self.test = test[attributes]
        self.path = path
        self.model = CategoricalNB(alpha=m)
        self.trained_model = ""

    # -- Training the model --
    def build_model(self):
        self.model.fit(self.x_train, self.y_train)

    # -- Classify the test records --
    def classify_records(self):
        self.y_predict = self.model.predict(self.test)
        utils.write_to_file(self.path, self.y_predict)




