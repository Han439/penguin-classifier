import json
import numpy as np
import pandas as pd
import sys
import joblib
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# load data
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/part3/penguins_cleaned.csv')

# prepare features and target
X = df.drop(['species'], axis=1, inplace=False)
y = df['species']

# encoder categories features
category_cols = ['island', 'sex']
encoders = {}
for col in category_cols:
    converter = LabelEncoder()
    X[col] = converter.fit_transform(X[col])
    encoders[col] = converter

# prepare test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123)

# train model
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
dt.score(X_test, y_test)

# save to the disk
joblib.dump(dt, './decision_tree.joblib', compress=True)
joblib.dump(encoders, './encoders.joblib', compress=True)
joblib.dump(category_cols, './categories.joblib', compress=True)

