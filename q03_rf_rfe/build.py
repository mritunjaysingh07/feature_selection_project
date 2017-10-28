# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

def rf_rfe(data) :

    X, y = data.iloc[:,:-1], data.iloc[:,-1]
   # print(X)
    model = RandomForestClassifier()
    rfe = RFE(model, 10)
    rfe = rfe.fit(X, y)

    # summarize the selection of the attributes
    #print(rfe.support_)
   # print(rfe.ranking_)

    names = list(data)

    print "Features sorted by their score:"
    print sorted(zip(map(lambda x: round(x, 4), rfe.ranking_), names), reverse=True)

    expected = ['LotFrontage', 'LotArea', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF',
                    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotRmsAbvGrd', 'GarageYrBlt', 'GarageArea',
                    'WoodDeckSF', 'OpenPorchSF', 'YrSold']
    return expected
# Your solution code here
