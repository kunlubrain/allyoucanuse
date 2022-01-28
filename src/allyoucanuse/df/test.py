import pandas as pd
from pandas import DataFrame

from __init__ import *

df = DataFrame(
    [
        ["1", "2", "3", "4", "5"],
        ["1", "2", "3", "6", "5"],
        ["1", "2", "6", "3", "1"],
    ],
    columns=["a", "b", "c", "d", "e"],
)


def test_df_row_contains():
    print(df)
    print(df_row_contains(df, "6", "d"))
    print(df_row_contains(df, "6", None))


# test_df_row_contains()


def test_df_column_stats():
    df = DataFrame(
        {
            "categorical": pd.Categorical(["d", "e", "f"]),
            "numeric": [1, 2, 3],
            "numeric2": [3, 200, 500],
            "object": ["a", "b", "c"],
        }
    )
    print(df_column_stats(df, None))
    print(df_column_stats(df, "numeric2"))


# test_df_column_stats()
