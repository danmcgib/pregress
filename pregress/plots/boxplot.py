from pregress.modeling.parse_formula import parse_formula
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def boxplot(formula=None, data=None, xcolor="blue", ycolor="red", main="Boxplots of Variables", xlab="Variable", ylab="Value"):
    """
    Generates and prints boxplots for all numeric variables specified in the formula or all numeric variables in the data if no formula is provided.

    Args:
        formula (str, optional): Formula to define the model (dependent ~ independent).
        data (DataFrame, optional): Data frame containing the data.
        xcolor (str, optional): Color of the boxplots for the independent variables.
        ycolor (str, optional): Color of the boxplots for the dependent variable.

    Returns:
        None. The function creates and shows boxplots.
    """
    # Clear any existing plots
    #plt.clf()
    #plt.close()

    if formula is not None:
        formula = formula + "+0"
        Y_name, X_names, Y_out, X_out = parse_formula(formula, data)

        # Combine Y and X data for boxplots
        plot_data = pd.concat([pd.Series(Y_out, name=Y_name), X_out], axis=1)

        # Melt the DataFrame for easier plotting with seaborn
        plot_data_melted = plot_data.melt(var_name='Variable', value_name='Value')

        # Create a color palette
        palette = {Y_name: ycolor, **{var: xcolor for var in X_names}}
    else:
        # If no formula is provided, use all numeric variables in the data
        plot_data = data.select_dtypes(include=[np.number])
        plot_data_melted = plot_data.melt(var_name='Variable', value_name='Value')

        # Create a single color for all variables
        palette = {var: xcolor for var in plot_data.columns}

    # Create the boxplot
    plt.figure(figsize=(10, 6))
    boxplot = sns.boxplot(x='Variable', y='Value', data=plot_data_melted, hue='Variable', palette=palette, dodge=False)
    boxplot.set_title(main)
    boxplot.set_xlabel(xlab)
    boxplot.set_ylabel(ylab)

    plt.show()






