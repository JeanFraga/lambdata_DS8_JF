"""
lambdata - a collection of data science helper functions
"""

import pandas as pd
import numpy as np

# Sample code

ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

def increment(x):
	return(x+1)

def null_count(dataframe):
	"""
	returns a series that equals the sum of null values for each feature
	"""
	print("This here is the sum total for null values")
	return dataframe.isnull().sum()

def datetime_converter(dataframe, column):
	"""
	returns the dataframe you imported along with the column you want to separate by year/month/day
	"""
	df = dataframe.copy()
	df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
	df['year'] = df[column].dt.year
	df['month'] = df[column].dt.month
	df['day'] = df[column].dt.day
	df = df.drop(columns=column)
	return df
