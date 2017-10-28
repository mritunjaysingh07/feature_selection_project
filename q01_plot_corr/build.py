# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('data/house_prices_multivariate.csv')
def plot_corr(data,size = 11):
    plt.figure(figsize=(10,6))
    sns.heatmap(data.corr())


# Write your solution here:
