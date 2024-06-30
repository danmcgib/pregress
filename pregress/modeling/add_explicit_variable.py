# add_explicit_variable.py

from .extract_variable import extract_variable
from .apply_transformation import apply_transformation
from .environment import EvalEnvironment
import pandas as pd
from functools import reduce

def add_explicit_variable(df, X_vars, predictor, additional_globals=None):  # Line updated to include additional_globals

    env = EvalEnvironment(frame_depth=2, additional_globals=additional_globals)  # Line updated to include additional_globals
    
    trans, untransformed = extract_variable(predictor)

    if untransformed in df.columns:
        X_vars[predictor] = apply_transformation(df[untransformed], trans)
        #print(f"Applied transformation for predictor: {predictor}")
    elif trans == 'interaction':
        vars = untransformed.split(':')
        series_list = []
        missing_vars = []

        for var in vars:
            if var in df.columns:
                series_list.append(df[var])
            else:
                try:
                    print(f"Trying to evaluate {var} in global scope.")
                    series_list.append(env.eval(var))
                except NameError:
                    missing_vars.append(var)

        if missing_vars:
            raise ValueError(f"Missing variables for interaction: {', '.join(missing_vars)}")

        if len(series_list) > 1:
            X_vars[predictor] = reduce(lambda x, y: x * y, series_list)
        else:
            raise ValueError("Insufficient variables for interaction.")
    else:
        try:
            #print(f"Trying to evaluate {untransformed} in global scope.")
            X_vars[predictor] = apply_transformation(env.eval(untransformed), trans)
            #print(f"Applied transformation for global variable: {untransformed}")
        except NameError:
            #print(f"Failed to find {untransformed} in global scope.")
            raise ValueError(f"The variable '{untransformed}' is not available in the DataFrame or as a global Series.")
    
    #print(f"Exiting add_explicit_variable for predictor: {predictor}")
