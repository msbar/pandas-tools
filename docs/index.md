# Pandas Tools

PandasTools is a Python package that extends the functionality of Pandas DataFrames by introducing the `PtDataFrame` class. `PtDataFrame` provides additional features and enhancements to work with DataFrames in a more convenient and flexible way.

## Features

- Asynchronous iteration support: `PtDataFrame` implements both synchronous and asynchronous iterators, allowing for efficient and convenient data processing in asynchronous contexts.
- Context manager support: `PtDataFrame` can be used as a context manager to easily access the encapsulated Pandas DataFrame.
- Concatenation and reduction: `PtDataFrame` supports concatenation of multiple instances and reduction of a list of `PtDataFrame` objects into a single instance.
- Column extraction: Easily extract a column as a list from a `PtDataFrame`.

## Installation

You can install PandasTools using pip:
```
pip install pandas-tools
```