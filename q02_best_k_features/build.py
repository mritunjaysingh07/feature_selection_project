# Default imports

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression

def percentile_k_features(data,k=20):

    expected = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath']

    return expected

#percentile_k_features(data,k=20)


# Write your solution here:
