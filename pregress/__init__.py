"""
PRegress Package
================

A package for regression analysis and data visualization.

Modules
-------
modeling
    Functions for model fitting and prediction.
plots
    Functions for various types of plots.

Functions
---------
Modeling functions:
- add_explicit_variable
- apply_transformation
- EvalEnvironment
- extract_variable
- fit
- format_summary
- handle_included_vars
- handle_included_vars2
- parse_formula
- predict
- print_anova_and_summary
- print_anova_table
- print_r_summary
- print_stata_summary
- significance_code
- summary

Plotting functions:
- boxplot
- hist
- hists
- plot_cor
- plotCook
- plotQQ
- plotR
- plotRH
- plots
- plotXY
"""

# Import modeling functions
from .modeling import (
    add_explicit_variable, apply_transformation, EvalEnvironment, extract_variable, fit,
    format_summary, handle_included_vars, handle_included_vars2, parse_formula, predict,
    print_anova_and_summary, print_anova_table, print_r_summary, print_stata_summary,
    significance_code, summary
)

# Import plotting functions
from .plots import (
    boxplot, hist, hists, plot_cor, plotCook, plotQQ, plotR, plotRH, plots, plotXY
)

__all__ = [
    # Modeling functions
    'add_explicit_variable', 'apply_transformation', 'EvalEnvironment', 'extract_variable', 'fit',
    'format_summary', 'handle_included_vars', 'handle_included_vars2', 'parse_formula', 'predict',
    'print_anova_and_summary', 'print_anova_table', 'print_r_summary', 'print_stata_summary',
    'significance_code', 'summary',
    
    # Plotting functions
    'boxplot', 'hist', 'hists', 'plot_cor', 'plotCook', 'plotQQ', 'plotR', 'plotRH', 'plots', 'plotXY'
]
