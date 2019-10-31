# lambdata_JeanFraga_DS8: powerful Python data analysis methods for convinience

<table>
<tr>
  <td>Latest Release</td>
  <td>
    <a href="https://test.pypi.org/project/lambdata-JeanFraga-DS8/">
    <img src="https://img.shields.io/pypi/status/pandas.svg" alt="status" />
    </a>
  </td>
</tr>
<tr>
  <td>License</td>
  <td>
    <a href="https://github.com/JeanFraga/lambdata_DS8_JF/blob/master/LICENSE">
    <img src="https://img.shields.io/pypi/l/pandas.svg" alt="license" />
    </a>
</td>
</tr>
</table>

## What is it?

**lambdata_JeanFraga_DS8** is a work in progress to fascilitate the use of a number of functions for data science.

## Main Features
Here are just a few of the things that pandas does well:

  - date: columns can be [**datetime_converter**][datetime_converter] to turn the date column into 3 different columns(year/month/day)
  - Easy print sum of [**null_values**][null_values] (represented as
    `NaN`) in a series.

   [null_values]: https://github.com/JeanFraga/lambdata_DS8_JF/blob/master/lambdata_JeanFraga_DS8/__init__.py
   [datetime_converter]: https://github.com/JeanFraga/lambdata_DS8_JF/blob/master/lambdata_JeanFraga_DS8/__init__.py

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/JeanFraga/lambdata_DS8_JF

```sh
# or PyPI
pip install pandas
```

## Dependencies
- [NumPy](https://www.numpy.org): 1.13.3 or higher
- [python-dateutil](https://labix.org/python-dateutil): 2.5.0 or higher
- [pytz](https://pythonhosted.org/pytz): 2015.4 or higher

See the [full installation instructions](https://pandas.pydata.org/pandas-docs/stable/install.html#dependencies)
for recommended and optional dependencies.

## License
[BSD 3](LICENSE)

## Background
Work on ``pandas`` started at AQR (a quantitative hedge fund) in 2008 and
has been under active development since then.

