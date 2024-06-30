from pregress.modeling.parse_formula import parse_formula
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm as normal_dist
import warnings

def hists(formula, data=None, xcolor="blue", ycolor="red", norm=False, layout="matrix"):
    """
    Generates and prints histograms for all numeric variables specified in the formula.

    Args:
        formula (str): Formula to define the model (dependent ~ independent).
        data (DataFrame, optional): Data frame containing the data.
        xcolor (str, optional): Color of the histograms for the independent variables.
        ycolor (str, optional): Color of the histograms for the dependent variable.
        norm (bool, optional): Whether to include a normal distribution line.
        layout (str, optional): Layout of the histograms - "column", "row", or "matrix".

    Returns:
        None. The function creates and shows histograms.
    """
    # Clear any existing plots
    plt.clf()
    plt.close()

    formula = formula + "+0"
    Y_name, X_names, Y_out, X_out = parse_formula(formula, data)

    # Combine Y and X data for histograms
    plot_data = pd.concat([pd.Series(Y_out, name=Y_name), X_out], axis=1)

    # Replace infinite values with NaN
    plot_data.replace([np.inf, -np.inf], np.nan, inplace=True)

    num_vars = len(plot_data.columns)

    # Determine the layout
    if layout == "column":
        nrows, ncols = num_vars, 1
    elif layout == "row":
        nrows, ncols = 1, num_vars
    elif layout == "matrix":
        nrows = int(np.ceil(np.sqrt(num_vars)))
        ncols = int(np.ceil(num_vars / nrows))
    else:
        raise ValueError("Invalid layout option. Choose from 'column', 'row', or 'matrix'.")

    fig, axes = plt.subplots(nrows, ncols, figsize=(5 * ncols, 5 * nrows))
    axes = np.array(axes).reshape(-1)  # Flatten the axes array for easy iteration

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)

        for i, var in enumerate(plot_data.columns):
            ax = axes[i]
            color = ycolor if var == Y_name else xcolor
            sns.histplot(plot_data[var], bins=30, kde=False, color=color, ax=ax, edgecolor='black')
            if norm:
                mean = plot_data[var].mean()
                std = plot_data[var].std()
                x = np.linspace(plot_data[var].min(), plot_data[var].max(), 100)
                p = normal_dist.pdf(x, mean, std)
                ax.plot(x, p * (len(plot_data[var]) * np.diff(np.histogram(plot_data[var], bins=30)[1])[0]), 'k', linewidth=2)
            ax.set_title(f'Histogram of {var}')
            ax.set_xlabel(var)
            ax.set_ylabel('Frequency')

        # Remove any unused subplots in the matrix layout
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])

        plt.tight_layout()
        plt.show()
