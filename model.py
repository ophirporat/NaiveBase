from sklearn.naive_bayes import MultinomialNB

import utils


class Model:
    def __init__(self, train, test, m_estimator, attributes, path):

        self.x_train = train[attributes]
        self.y_train = train["class"]
        self.test = test[attributes]
        self.path = path
        # self.m_estimator = m_estimator
        self.model = MultinomialNB()
        self.trained_model = ""

    def build_model(self):
        # print("self.x_train", self.x_train)
        # print("self.y_train", self.y_train)
        self.model.fit(self.x_train, self.y_train)
        pass

    def classify_records(self):
        print(self.test)
        self.y_predict = self.model.predict(self.test)
        utils.write_to_file(self.path, self.y_predict)




