import pickle
from preprocess import prepare_data

with open("PhishingDomainDetection.pkl", "rb") as file:
    classifier = pickle.load(file)


def predictor(URL):
    result = classifier.predict(prepare_data(URL))
    return result[0]