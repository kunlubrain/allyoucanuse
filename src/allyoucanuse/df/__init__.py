from pandas import DataFrame
from typing import Dict, List, Union


def df_row_contains(
        df: DataFrame,
        s: str,
        col: str = None)->DataFrame:
    """Filter the rows if any field in the row contains `s`

    Parameters
    ----------
    s: str
        A query text that we search in the df
        If `s` is empty, return df as is.
    col: str|None
        If not None, we consider only that field in a row.
        If None, we consider all fields (columns).

    Return
    ------
        The part of the dataframe that is filtered
    """

    raise NotImplementedError


def df_column_stats(
        df: DataFrame,
        col: str = None) -> Union[Dict, List[Dict]]:
    """Show the statistics of one column in a df

    The stats include:
    * max
    * min
    * avg
    * value count

    Parameters
    ----------
    col: str|None
        If None, we consider all columns.

    Return
    ------
        Example:
        {
            "max": 10,
            "min": 2,
            "avg": 5,
            "value_count": {"2": 1, "10":1, "3":1, "5":2},
        }
    """
    raise NotImplementedError
