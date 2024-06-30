from .parse_formula import parse_formula
import statsmodels.api as sm

def fit(formula, data=None, method = "statsmodels"):

    Y_name, X_names, Y_out, X_out = parse_formula(formula, data)
    if X_out.empty:
        raise ValueError("The input data is empty or the specified variables are not found in the data.")

    model = sm.OLS(Y_out, X_out).fit()
    return model
