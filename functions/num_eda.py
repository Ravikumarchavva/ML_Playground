import pandas as pd 
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.base import BaseEstimator, TransformerMixin

class ConstantScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        # self.constant = constant
        pass

    def fit(self, X, y=None):
        # The fit method does not do anything in this case
        return self

    def transform(self, X):
        # Scale the input data by the constant value
        return X / X.max()

    def fit_transform(self, X, y=None):
        # Fit to data, then transform it
        return self.transform(X)

    def get_params(self, deep=True):
        return {}
    def get_feature_names_out(self, input_features=None):
        # Return the input features as output features
        return input_features

def num_scatter_plot(df,num_features,target_col):
    for col in num_features:
        fig, axes = plt.subplots(1, figsize=(18, 6))

        sns.regplot(data=df, x=col,y=target_col, ax=axes)
        axes.set_title(f'Bar Plot for {col}')
        axes.tick_params(axis='x', rotation=45)
        
        # Add percentage annotations on top of bars
        total = len(df[col])
        for p in axes.patches:
            height = p.get_height()
            axes.text(p.get_x() + p.get_width() / 2.,
                        height + 3,
                        '{:1.2f}%'.format((height / total) * 100),
                        ha="center")

        plt.tight_layout()
        plt.show()
def num_dodge_plot(data, num_cols, target_col):
    # Determine the number of rows needed based on the number of numerical columns
    n_cols = 2
    n_rows = (len(num_cols) + 1) // n_cols  # Round up if there is an odd number of columns
    
    fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 5 * n_rows))
    ax = ax.flatten()  # Flatten the array of axes for easy indexing
    
    for index, col in enumerate(num_cols):
        sns.histplot(data.to_pandas(), x=col, hue=target_col, multiple="dodge",fill=True, ax=ax[index])
        ax[index].set_title(f'Distribution of {col} by {target_col}')
    
    # Hide any unused subplots
    for j in range(index + 1, len(ax)):
        fig.delaxes(ax[j])
    
    plt.tight_layout()
    plt.show()