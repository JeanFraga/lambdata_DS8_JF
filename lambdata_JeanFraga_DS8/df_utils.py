"""
checks for any nulls then displays a sum of the nulls for every feature.

splits dates ("MM/DD/YYYY", etc.) into multiple columns
"""

import pandas

def null_count(dataframe):
	print("This here is the sum total for null values")
	return dataframe.isnull().sum()

def datetime_converter(dataframe, column):
	df = dataframe.copy()
	df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
    df['year'] = df[column].dt.year
    df['month'] = df[column].dt.month
    df['day'] = df[column].dt.day
    df = df.drop(columns=column)
    return df

