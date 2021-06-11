from sklearn.naive_bayes import MultinomialNB

from model import utils


class Model:
    def __init__(self, train, test, m_estimator, attributes, path):

        self.x_train = train[attributes]
        self.y_train = train["class"]
        self.test = test[attributes]
        self.path = path
        # self.m_estimator = m_estimator
        self.model = MultinomialNB(alpha=m_estimator)
        self.trained_model = ""

    def build_model(self):
        self.model.fit(self.x_train, self.y_train)
        pass

    def classify_records(self):
        self.y_predict = self.model.predict(self.test)
        utils.write_to_file(self.path, self.y_predict)




