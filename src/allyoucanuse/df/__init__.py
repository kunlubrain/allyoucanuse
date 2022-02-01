from typing import Dict, List, Optional, Union

import numpy as np
from pandas import DataFrame


def df_row_contains(
    df: DataFrame, s: Union[str, int], col: Optional[str] = None
) -> DataFrame:
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
    if s is None:
        return df
    if col is None:
        # filter all rows across all columns, if any field in the row contains `s`
        mask = np.column_stack([df[col].str.contains(s) for col in df])
        return df.loc[mask.any(axis=1)]  # type: ignore
        # return df[(df.iloc[:, :] == s).any(axis=1)]  # type: ignore, exact match
    return df[df[col].str.contains(s)]  # type: ignore


def df_column_stats(df: DataFrame, col: Optional[str]) -> Union[Dict, List[Dict]]:  # type: ignore
    """Show the statistics of one column in a df

    The stats include:
    count
    mean
    std
    min
    25%
    50%
    75%
    max

    Parameters
    ----------
    col: str|None
        If None, we consider all columns.

    Return
    ------
        Example:
        {
           "count":3.0,
           "mean":2.0,
           "std":1.0,
           "mid":1.0,
           "25d":1.5,
           "50d":2.0,
           "75d":2.5,
           "mad":3.0
        }
    """
    if col is None:
        return [df_column_stats(df, col) for col in df.columns]
    value_counts = df[col].value_counts()
    stats = df[col].describe().to_dict()
    stats["value_counts"] = value_counts.to_dict()
    return stats  # type: ignore
