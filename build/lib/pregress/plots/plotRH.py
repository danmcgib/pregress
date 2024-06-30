from .hist import hist
from pregress.modeling.fit import fit
import numpy as np
import matplotlib.pyplot as plt

def plotRH(model):
    """
    Plots a histogram of the residuals of a fitted statsmodels regression model and overlays a normal distribution curve.

    Args:
        model (statsmodels.regression.linear_model.RegressionResultsWrapper): A fitted statsmodels regression model.

    Returns:
        None. Displays a histogram of residuals with a normal distribution curve.
    """
    # Calculate residuals
    residuals = model.resid

    # Plot histogram of the residuals
    plt.hist(residuals, bins=30, color='blue', alpha=0.7, density=True, label='Residuals Histogram')

    # Fit a normal distribution to the residuals
    mu, std = stats.norm.fit(residuals)

    # Create a range of values from the residuals' min to max for plotting the curve
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)

    # Plot the normal distribution curve
    plt.plot(x, p, 'k', linewidth=2, label=f'Normal Dist. Mean={mu:.2f}, Std={std:.2f}')
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)

    # Add labels and legend
    plt.xlabel('Residuals')
    plt.ylabel('Density')
    plt.legend()

    # Display the plot
    plt.show()

