import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
import pickle

if __name__ =="__main__":
    df = pd.read_csv("COVID-19dataset.csv")
    y = df['Corona result']
    df.drop('Corona result',axis=1,inplace = True)
    X_train, X_valid, y_train, y_valid = train_test_split(df, y, test_size=0.3, shuffle=True)
    model = RandomForestRegressor(n_estimators=100, max_features=0.7, bootstrap=True, max_depth=10, min_samples_leaf=5, random_state=42)
    model.fit(X_train, y_train)

    # open a file, where you ant to store the data
    file = open('model.pkl', 'wb')

    # dump information to that file
    pickle.dump(model, file)
    file.close()

    predictions = model.predict(X_valid)
    prob = int(model.predict([[20,1,98.6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]))
    prob