def plotCook(model):
    """
    Plots Cook's Distance for each observation in a fitted statsmodels regression model to identify influential points.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.

    Returns:
        None. Displays a plot of Cook's Distance for each observation.
    """
    # Calculate Cook's Distance
    influence = model.get_influence()
    cooks_d = influence.cooks_distance[0]

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.stem(np.arange(len(cooks_d)), cooks_d, markerfmt=",", use_line_collection=True)
    ax.set_xlabel('Observation Index')
    ax.set_ylabel("Cook's Distance")
    ax.set_title("Cook's Distance Plot")

    # Adding a reference line for common cutoff
    ax.axhline(y=0.5, linestyle='--', color='red', label='Influence threshold (0.5)')
    ax.legend()

    # Show the plot
    plt.show()

# Example usage:
# Assuming 'model' is your fitted statsmodels object, you would call it like this:
# plotCooksDistance(model)


# In[ ]:


import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
from statsmodels.graphics.gofplots import ProbPlot
