from pregress.modeling.parse_formula import parse_formula
import matplotlib.pyplot as plt
import seaborn as sns

def plotXY(formula, data=None, pcolor="blue", lcolor="red", xlab=None, ylab=None, main=None, line=True, psize = 50):
    """
    Generates and prints a plot of the regression model fit using a specified formula and data.
    It only supports plotting for models with one predictor variable. The function utilizes Seaborn
    for plotting the regression line and scatter plot.

    Args:
        formula (str): Formula to define the model (dependent ~ independent).
        data (DataFrame, optional): Data frame containing the data.
        pcolor (str, optional): Color of the points in the scatter plot.
        lcolor (str, optional): Color of the regression line.
        xlab (str, optional): Label for the x-axis.
        ylab (str, optional): Label for the y-axis.
        main (str, optional): Title for the plot.
        line (bool, optional): Whether to display the regression line. Default is True.

    Returns:
        None. The function creates and shows a plot.
    """

    # Clear any existing plots
    plt.clf()
    plt.close()

    formula = formula + "+0"
    Y_name, X_names, Y_out, X_out = parse_formula(formula, data)

    # Check the number of predictor variables in the model
    if X_out.shape[1] > 1:
        print("Only one predictor variable can be plotted.")
    else:
        # Plot the regression line and scatter plot using seaborn
        if line:
            sns.regplot(x=X_out, y=Y_out, scatter_kws={"color": pcolor, "s": psize}, line_kws={"color": lcolor}, ci=None)
        else:
            sns.scatterplot(x=X_out.values.flatten(), y=Y_out, color=pcolor, s=psize)

        # Set labels for the x and y axes
        plt.xlabel(xlab if xlab is not None else X_names[0])
        plt.ylabel(ylab if ylab is not None else Y_name)

        if main is not None:
            plt.title(main)

        # Display the plot
        plt.show()


