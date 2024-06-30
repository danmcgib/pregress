import numpy as np

def plotQQ(model):
    """
    Generates a QQ plot for the residuals of a fitted statsmodels regression model to assess normality,
    including a 95% confidence band.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.

    Returns:
        None. Displays a QQ plot of the residuals with a 95% confidence band.
    """
    # Extract residuals
    residuals = model.resid

    # Create a Probability Plot
    pp = ProbPlot(residuals, fit=True)

    # Generate the QQ plot figure
    fig, ax = plt.subplots(figsize=(6, 4))

    # Generate the plot
    qq = pp.qqplot(line='45', alpha=0.5, color='blue', lw=1, ax=ax)

    # Add 95% confidence interval
    quantiles = np.linspace(0.02, 0.98, 100)  # Adjust range to avoid extreme ends
    endog_quantiles = pp.theoretical_quantiles
    sample_quantiles = pp.sample_quantiles

    # Interpolating quantile values
    crit = statsmodels.stats.stattools.qsturng(quantiles, len(residuals))
    ci_low = np.interp(crit, endog_quantiles, sample_quantiles)
    ci_upp = np.interp(2 - crit, endog_quantiles, sample_quantiles)

    ax.fill_betweenx(np.sort(pp.sample_quantiles), ci_low, ci_upp, color='gray', alpha=0.3)

    # Setting the plot title and labels
    ax.set_title('QQ Plot of Residuals with 95% Confidence Band')
    ax.set_xlabel('Theoretical Quantiles')
    ax.set_ylabel('Sample Quantiles')

    # Display the plot
    plt.show()

# Example usage:
# Assuming 'model' is your fitted statsmodels object, you would call it like this:
# plotQQ(model)


# In[ ]:


import matplotlib.pyplot as plt
