from .format_summary import format_summary
from .print_r_summary import print_r_summary
from .print_anova_table import print_anova_table
from .print_stata_summary import print_stata_summary
from .significance_code import significance_code
import numpy as np
import pandas as pd
import statsmodels.api as sm
import warnings

def summary(model, type='statsmodels'):
    """
    Generates and prints a summary of the regression model fit. The default summary is from statsmodels,
    but it can also mimic summaries from R, STATA, or show only specific parts like the
    coefficient table or the ANOVA table. The summary is also returned for further use.

    Args:
        type (str): Type of summary output. Options include 'statsmodels', 'R', 'STATA',
                    'coefficients', and 'ANOVA'.

    Returns:
        Various types of summaries depending on the input type, both printed and returned.
    """
    if type == 'statsmodels':
        print(model.summary())
        return

    warnings.filterwarnings("ignore", category=sm.tools.sm_exceptions.ValueWarning)
    results_summary = model.summary()
    results_as_html = results_summary.tables[1].as_html()
    summary_df = pd.read_html(results_as_html, header=0, index_col=0)[0]
    summary_df = format_summary(summary_df)

    p_values = model.pvalues
    conf_intervals = model.conf_int()
    r_squared = model.rsquared
    adj_r_squared = model.rsquared_adj
    f_statistic = model.fvalue
    f_p_value = model.f_pvalue
    log_likelihood = model.llf
    aic = model.aic
    bic = model.bic
    RSS = np.sum(model.resid**2)
    df = model.df_resid
    RSE = np.sqrt(RSS / df)
    n_obs = int(model.nobs)
    df_model = model.df_model
    df_resid = model.df_resid
    mse_model = model.mse_model
    mse_resid = model.mse_resid

    if type == 'R':
        print_r_summary(model, summary_df, RSE, r_squared, adj_r_squared, f_statistic, f_p_value)
    elif type == 'simple':
        print("Coefficients:")
        print("---")
        print(summary_df)
        print("\n---")
        print(f"R-squared: {r_squared:.4f}")
        print(f"F-statistic: {f_statistic:.2f} on {int(model.df_model)} and {int(model.df_resid)} DF, p-value: {f_p_value:.6f}")
    elif type in ['coefficients', 'coef']:
        print(model.summary().tables[1])
    elif type == 'ANOVA':
        anova_table = print_anova_table(model)
        print(anova_table)
    elif type == 'STATA':
        print_stata_summary(model, summary_df, conf_intervals)
    else:
        raise ValueError("Unsupported summary type specified.")


