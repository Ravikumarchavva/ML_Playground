import pandas as pd
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns
def cat_fill_mode(df,features):
    for col in features:
        df[col].fillna(df[col].mode().iloc[0],inplace=True)
        
def cramers_v(x, y):
    """Calculate Cramér's V statistic for categorial-categorial association."""
    confusion_matrix = pd.crosstab(x,y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))
    
def cramers_v_matrix(df, cat_cols):
    """Build Cramér's V matrix for categorical columns."""
    matrix = np.zeros((len(cat_cols), len(cat_cols)))
    for i, col1 in enumerate(cat_cols):
        for j, col2 in enumerate(cat_cols):
            matrix[i, j] = cramers_v(df[col1], df[col2])
    return matrix
    
def plot_heatmap(matrix, columns):
    """Plot heatmap for Cramér's V matrix."""
    plt.figure(figsize=(18, 5))
    sns.heatmap(matrix, annot=True, cmap='coolwarm', fmt=".2f", xticklabels=columns, yticklabels=columns)
    plt.title("Cramér's V Association Matrix")
    plt.show()

def plot_roc_curve(fpr, tpr):
    """
    Plots a ROC curve given the false positve rate (fpr) and 
    true postive rate (tpr) of a classifier.
    """
    # Plot ROC curve
    plt.plot(fpr, tpr, color='green', label='ROC')
    
    # Plot line with no predictive power (baseline)
    plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='Guess')
    
    # Customize the plot
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve', fontsize=15)
    plt.legend()
    plt.show()

def calculate_proportions(df, group_by, target):
    prop_df = df.groupby([group_by, target]).size().unstack().apply(lambda x: x / x.sum(), axis=1)
    return prop_df

def cat_proportion_plot(data, cat_cols, target_col):
    if (type(data)==pl.dataframe.frame.DataFrame):
        data=data.to_pandas()
    # Determine the number of rows needed based on the number of categorical columns
    n_cols = 2
    n_rows = (len(cat_cols) + 1) // n_cols  # Round up if there is an odd number of columns
    
    fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(20, 5 * n_rows))
    ax = ax.flatten()  # Flatten the array of axes for easy indexing
    
    for index, col in enumerate(cat_cols):
        prop_df = calculate_proportions(data, col, target_col)
        prop_df.plot(kind='bar', stacked=True, ax=ax[index])
        ax[index].set_title(f'Proportion of {target_col} by {col}')
        ax[index].set_ylabel('Proportion')
        ax[index].set_xlabel(col)
        ax[index].legend(['No', 'Yes'], loc='upper right')

    # Hide any unused subplots
    for j in range(index + 1, len(ax)):
        fig.delaxes(ax[j])
    
    plt.tight_layout()
    plt.show()