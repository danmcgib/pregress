def plot_cor(df, title='Correlation Matrix', figsize=(10, 8), annot=True):
    """
    Generates a heatmap for the correlation matrix of a DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame for which to compute the correlation matrix.
        title (str, optional): Title of the plot.
        figsize (tuple, optional): Figure size in inches (width, height).
        annot (bool, optional): If True, write the data value in each cell.

    Returns:
        None. Displays the heatmap.
    """
    # Calculate the correlation matrix
    corr_matrix = df.corr()

    # Create a mask for the upper triangle
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Set up the matplotlib figure
    plt.figure(figsize=figsize)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr_matrix, mask=mask, annot=annot, cmap='coolwarm', vmax=1, vmin=-1,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.title(title)
    plt.show()

# Example usage:
# Assuming 'data' is your pandas DataFrame:
# plot_corr_matrix(data)


# In[80]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm as normal_dist
import inspect
