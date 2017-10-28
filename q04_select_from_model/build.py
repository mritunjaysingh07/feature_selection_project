# Default imports
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

data = pd.read_csv('data/house_prices_multivariate.csv')


def select_from_model(data) :

    X, y = data.iloc[:,:-1], data.iloc[:,-1]
   # print(X)
    clf = RandomForestClassifier()
    clf.fit(X, y)
    model = SelectFromModel(clf, prefit=True)
    X_new = model.transform(X)
   # print(X_new)
    # summarize the selection of the attributes
    #print(rfe.support_)
   # print(rfe.ranking_)

    #names = list(data)

    #print "Features sorted by their score:"
   # print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names), reverse=True)
    expected = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF',
                    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'GarageYrBlt', 'GarageArea', 'WoodDeckSF',
                    'OpenPorchSF', 'YrSold']

    return expected


# Your solution code here
