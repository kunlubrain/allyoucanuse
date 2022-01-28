from typing import Union, Iterable
import hashlib

def hash_id(seeds:Union[str, Iterable], n:int=32)->str:
    """For the moment, use the default simple python hash func
    """
    h = hashlib.sha256(''.join(seeds)).hexdigest()[:n]
    return h