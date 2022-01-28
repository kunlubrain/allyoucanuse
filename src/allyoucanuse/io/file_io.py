from typing import Iterable, Dict, Any
import jsonlines
import json

def read_jsonline_file(filename:str)->Iterable:
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


def write_jsonline_file(filename:str, lines:Iterable):
    """Write the content of `lines` into a jsonline file"""
    raise NotImplementedError

def read_yml_file(filename:str)->Dict:
    """Return the content of a yml file as a dict"""
    raise NotImplementedError

def read_json_file(filename:str)->Any:
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
    raise NotImplementedError


def write_json_file(filename:str, data:Any):
    """Write the data into a jsonline file"""
    raise NotImplementedError