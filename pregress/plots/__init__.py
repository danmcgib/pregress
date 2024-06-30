"""
Plots
============

This subpackage provides functions for various types of plots used in regression analysis.

Functions
---------
boxplot
    Create a boxplot of the data.
hist
    Create a histogram of the data.
hists
    Create multiple histograms of the data.
plot_cor
    Plot the correlation matrix.
plotCook
    Create a Cook's distance plot.
plotQQ
    Create a QQ plot.
plotR
    Plot the residuals.
plotRH
    Plot the residuals vs. fitted values.
plots
    Create various plots.
plotXY
    Plot the X vs. Y data.
"""

from .boxplot import boxplot
from .hist import hist
from .hists import hists
from .plot_cor import plot_cor
from .plotCook import plotCook
from .plotQQ import plotQQ
from .plotR import plotR
from .plotRH import plotRH
from .plots import plots
from .plotXY import plotXY

__all__ = [
    'boxplot', 'hist', 'hists', 'plot_cor', 'plotCook', 'plotQQ', 'plotR',
    'plotRH', 'plots', 'plotXY'
]
