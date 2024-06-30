def plotR(model):
    """
    Plots the residuals of a fitted statsmodels regression model.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.

    Returns:
        None. Displays a residual plot.
    """
    # Calculate residuals
    residuals = model.resid

    # Calculate fitted values
    fitted = model.predict()

    # Create the residual plot
    plt.scatter(fitted, residuals, color='blue')
    plt.axhline(0, color='red', linestyle='--')  # Adds a horizontal line at zero
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.show()

# Example usage:
# Assuming 'model' is your fitted statsmodels object, you would call it like this:
# plotR(model)


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
