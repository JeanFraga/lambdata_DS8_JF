"""
This is our testing file for lambdata_JeanFraga_DS8
"""

import unittest
from lambdata_JeanFraga_DS8 import Dataframe_manipulators as df_man


class Sampledftest(unittest.TestCase):
    """
    These are the tests for sample dataframes
    """

    def test_ONES(self):
        """
        ensures the resulting shape of the method "df_man.ONES" is equal to
        the expected shape.
        """
        ones = df_man.ONES
        self.assertTupleEqual(ones.shape, (10, 1))

    def test_ZEROS(self):
        """
        ensures the resulting shape of the method "df_man.ZEROS" is equal to
        the expected shape.
        """
        zeros = df_man.ZEROS
        self.assertTupleEqual(zeros.shape, (50, 1))


class test_manipulators(unittest.TestCase):
    """
    These are the tests for dataframe manipulators
    """

    def test_datetime_converter(self):
        """
        ensures the resulting shape of the method "df_man.datetime_converter"
        is equal to the expected shape.
        """
        zeros = df_man.ZEROS
        datetime = df_man.datetime_converter(zeros, 0)
        self.assertTupleEqual(datetime.shape, (50, 3))

    def test_null_counter(self):
        pass


if __name__ == '__main__':
    unittest.main()
