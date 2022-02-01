import re

import pendulum
from MailChecker import MailChecker
from pendulum.exceptions import ParserError


def cleanup(s: str, remove_non_alphabet: bool = True) -> str:
    """Remove all *bad* characters in text"""
    if remove_non_alphabet:
        s = re.sub("\W", "", s)
    s = re.sub("[\n\t]+", " ", s)
    s = re.sub("\s+", " ", s)
    return s


def is_email(s: str) -> bool:
    """Return True if the text is a valid email"""
    return MailChecker.is_valid(s)


def is_date(s: str) -> bool:
    """Return True if the text is an ISO-date"""
    try:
        dt = pendulum.parse(s)
        # print(dt)
    except ParserError:
        return False
    return True


def is_integer(s: str) -> bool:
    """Return True if the text is an integer"""
    return s.isdigit()


def is_float(s: str) -> bool:
    """Return True if the text is a floating number"""
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number(s: str) -> bool:
    """Return True if the text is either integer or floating number"""
    return is_integer(s) or is_float(s)
