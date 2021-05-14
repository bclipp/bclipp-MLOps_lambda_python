import sys
import sklearn
import pickle5 as pickle


def handler(event, context):
    loaded_model = pickle.load(open("model.pkl", 'rb'))
    prediction = loaded_model.predict(event["body"])
    return {
        'statusCode': 200,
        'body': prediction
    }
