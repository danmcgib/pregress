# parse_formula.py

from .extract_variable import extract_variable
from .apply_transformation import apply_transformation
from .handle_included_vars import handle_included_vars
from .environment import EvalEnvironment
import pandas as pd

def parse_formula(formula, df=None):
    """
    Parses a statistical formula and applies specified transformations to DataFrame columns.

    Args:
        formula (str): A string formula, e.g., 'Y ~ X1 + X2 - X3' or 'Y ~ . - X1'
        df (pd.DataFrame): DataFrame containing the data for variables mentioned in the formula.

    Returns:
        tuple: A tuple containing a dictionary of transformed predictors, list of predictor names,
               the transformed response series, and a DataFrame of transformed predictors.
    """

    formula = formula.replace(' ', '')
    response, predictors = formula.split('~')

    # Extract and transform the response variable.
    response_trans, untransformed_Y = extract_variable(response)

    # Attempt to resolve variables from df, if not present try to get from globals.
    if df is None:
        df = pd.DataFrame()

    if untransformed_Y not in df.columns:
        globals_dict = globals()
        if untransformed_Y in globals_dict:
            df[untransformed_Y] = globals_dict[untransformed_Y]
        else:
            raise KeyError(f"Variable '{untransformed_Y}' not found in DataFrame or global scope.")

    Y = apply_transformation(df[untransformed_Y], response_trans)

    if predictors == '1':
        X = pd.DataFrame(index=df.index)
        include_intercept = True
    else:
        # Check for intercept exclusion
        if '+0' in predictors or '-1' in predictors:
            include_intercept = False
            predictors = predictors.replace('+0', '').replace('-1', '').strip()
        else:
            include_intercept = True

        # Initialize lists to manage included and excluded variables.
        included_vars = []
        excluded_vars = []

        # Split the predictors on '+' and handle each segment separately.
        predictor_parts = predictors.split('+')
        for part in predictor_parts:
            if '-' in part:
                # If a '-' is present, split on '-' and manage exclusions.
                subparts = part.split('-')
                included_vars.append(subparts[0].strip())
                excluded_vars.extend([sub.strip() for sub in subparts[1:]])
            else:
                included_vars.append(part.strip())

        X_vars = handle_included_vars(df, included_vars, excluded_vars, untransformed_Y)

        X = pd.DataFrame(X_vars)

    if include_intercept:
        X['Intercept'] = 1
        cols = ['Intercept'] + [col for col in X.columns if col != 'Intercept']
        X = X[cols]

    return response, X.columns.tolist(), Y, X
