import joblib
import pandas as pd


class DecisionTreeClassifier:

    def __init__(self):
        self.encoders = joblib.load('ML/encoders.sav')
        self.model = joblib.load('ML/decision_tree.sav')

    def preprocessing(self, jsonInput):
        df = pd.DataFrame(jsonInput, index=[0])
        for col in ['island', 'sex']:
            encoder = self.encoders[col]
            df[col] = encoder.transform(df[col])

        return df

    def predict(self, jsonInput):
        try:
            df = self.preprocessing(jsonInput)
            predict_result = self.model.predict(df)[0]
        except Exception as e:
            return {'Error': e}

        return {'result': predict_result}
