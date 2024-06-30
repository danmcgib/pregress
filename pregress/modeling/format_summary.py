from .significance_code import significance_code


def format_summary(summary_df):
    """Formats the summary DataFrame."""
    # Remove the columns for the 95% confidence interval
    summary_df.drop(['[0.025', '0.975]'], axis=1, inplace=True)
    summary_df['P>|t|'] = summary_df['P>|t|'].astype(float).map(lambda x: f'{x:.6f}')
    summary_df[' '] = summary_df['P>|t|'].apply(significance_code)
    return summary_df
