import pandas as pd
class Model:
    def __init__(self,train, test, m_estimator, attributes,path):
        self.attributes = attributes
        self.m_estimator = m_estimator
        temp = [k for k in attributes.keys() if k != "class"]
        self.x_train = train[temp]
        self.y_train = train["class"]
        self.test = test[temp]
        self.path = path
        self.prob_dict ={}
        pass

    def calc_m_estimator(self):
        for attribute in self.attributes:
            probabilities = {}
            M = len(self.attributes[attribute])  # num of possible values
            p = float(1 / M)  # uniform prior
            classes = self.attributes["class"]
            predict_value = self.y_train
            curr_value = self.x_train
            for i in range(len(classes)):
                probabilities[classes[i]] = {}
                split_attribute_value = self.attributes[attribute]
                n = float(len(self.x_train.loc[classes[i] == predict_value]))  # all values
                for j in range(len(split_attribute_value)):
                    # n_c is the number of times the value appears
                    n_c = int(
                        len(self.x_train.loc[(classes[i] == predict_value) & (split_attribute_value[j] == curr_value)]))
                    m_estimator = (n_c + (p * self.m_estimator)) / (n + self.m_estimator)
                    probabilities[classes[i]][
                        split_attribute_value[j]] = m_estimator  # probabilities[male][yes] = 0.3
            self.m_estimator_dict[attribute] = probabilities

    def build_model(self, path, attributes, train, bins_dict):
        test = "self.x_train +self.y_train"
        num_of_options = attributes["class"]
        for i in range(len(self.attributes["class"])):
            sum_of_option = len(num_of_options)
            option_probability = sum_of_option / len(self.y_train)
            self.prob_dict[num_of_options[i]] = option_probability
        self.m_estimator()
        self.test(path+'/output.txt', test)

    def test(self,test):
        output = open(self.path, "w")
        probabilities = {}
        test = test.reset_index()
        test_len = len(test) + 1
        test["index"] = range(1, test_len)
        splited_class = self.attributes["class"].split(",")
        classes_len = len(splited_class)
        classes = []
        # create classes
        for i in range(classes_len):
            classes.append(splited_class[i])
        # save index
        for line in test.iterrows():
            index = line[1]["index"]
            # save options of each attribute
            for j in range(classes_len):
                option = classes[j]
                p = 1
                # skip attribute index or class
                for k in range(len(test.columns)):
                    attribute = test.columns[k]
                    if attribute == "index":
                        pass
                    elif attribute == "class":
                        pass
                    else:
                        # multiply p
                        try:
                            p *= self.m_estimator_dict[attribute][option][line[1][attribute]]
                        except KeyError:
                            continue
                # save probabilities
                probabilities[option] = self.prob_dict[option] * p
            # find max values
            max_key = max(probabilities, key=probabilities.get)
            output.write(str(index) + " " + max_key + "\n")
        output.flush()
        output.close()