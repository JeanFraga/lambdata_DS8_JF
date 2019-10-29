"""
lambdata - a collection of data science helper functions
by:Jean P Fraga
"""

import pandas as pd
import numpy as np


class Dataframe_manipulators:
    """
    In version 0.1.4 I added support for classes.
    At this moment Dataframe_manipulators only supports 2 methods.
    Built in a dataframe that can be called with "ONES", "ZEROS" for testing.

    Methods include "datetime_converter" and "null_count"
    """

    ONES = pd.DataFrame(np.ones(10))

    ZEROS = pd.DataFrame(np.zeros(50))

    def __init__(self):
        pass

    def datetime_converter(self, column):
        """
        returns the dataframe with the column separated by year/month/day
        """
        df = self.copy()
        df[column] = pd.to_datetime(df[column], infer_datetime_format=True)
        df['year'] = df[column].dt.year
        df['month'] = df[column].dt.month
        df['day'] = df[column].dt.day
        df = df.drop(columns=column)
        return df

    def null_count(self):
        """
        returns a series that equals the sum of null values for each feature
        """
        print("This here is the sum total for null values")
        return self.isnull().sum()
