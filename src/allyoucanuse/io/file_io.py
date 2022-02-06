import json
from typing import Any, Dict, Iterable

import jsonlines
from benedict import benedict


def read_jsonline_file(filename: str) -> Iterable:
    """Read a jsonline file

    Parameters
    ----------
    filename : str
        The jsonline file

    Returns
    -------
    Iterable
        [description]

    Example
    -------
    >>> import allyoucanuse as aycu
    >>> content = aycu.read_jsonline_file("tickets.jsonl")
    """
    with jsonlines.open(filename) as f:
        for record in f:
            yield record


def write_jsonline_file(filename: str, lines: Iterable[object]):
    """Write the content of `lines` into a jsonline file"""
    with open(filename, "w") as f:
        for line in lines:
            f.write(json.dumps(line) + "\n")


def read_yml_file(filename: str) -> Dict:
    """Return the content of a yml file as a dict"""
    d = benedict.from_yaml(filename)
    return d


def read_json_file(filename: str) -> Any:
    """Read a json file

    Parameters
    ----------
    filename : str
        The json file

    Returns
    -------
        A json object

    Example
    -------
    >>> import allyoucanuse as aycu
    >>> content = aycu.read_json_file("tickets.json")
    """
    with open(filename) as f:
        return json.load(f)


def write_json_file(filename: str, data: Any):
    """Write the data into a jsonline file"""
    with open(filename, "w") as f:
        json.dump(data, f)


import pickle


def write_pickle(filename: str, data: Any):
    """Write data into a pickle file"""
    with open(filename, "wb") as f:
        pickle.dump(data, f)


def read_pickle(filename: str) -> Any:
    """Load data from a pickle file"""
    with open(filename, "rb") as f:
        return pickle.load(f)
