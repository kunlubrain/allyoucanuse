from calendar import monthrange
from datetime import date, datetime, timedelta
from typing import Tuple, Union

import pendulum
from dateutil.relativedelta import relativedelta


def today_with_format(format: str = "%Y-%m-%d") -> str:
    return date.today().strftime(format)


def today_in_iso() -> str:
    return str(date.today())


def yesterday_in_iso() -> str:
    return str(date.today() - timedelta(days=1))


def firstday_previous_month():
    day = date.today()
    dd = day.replace(day=1) - timedelta(days=1)
    return str(dd.replace(day=1))


def today_of_year(n: int = 0) -> Union[date, None]:
    """Get today's date in iso format

    Parameters
    ----------
    n : int, optional
        n-th year ago, by default 0
        When `n=0`, returns today
        When `n=-1`, returns the same date of today one year ago
        When `n=-2`, returns the same date of today two year ago
        When `n=1`, returns the same date of today in one year
        When `n=2`, returns the same date of today in two year
        So on and soforth

        **Note**
        If today is the last day (29) of Febuary, and there is no
        Feb-29 in the n-th year. Return None

    Example
    -------
    >>> aycu.today_of_year(n=-1)
    '2021-01-28'
    >>> aycu.today_of_year(n=1)
    '2023-01-28'

    """
    dt = datetime.today()
    dt = date(dt.year, dt.month, dt.day)
    if n != 0 and dt.day == 29 and dt.month == 2 and dt.year % 4 != 0:
        return None
    try:
        dt = dt.replace(year=dt.year + n)
    except ValueError:
        dt = dt.replace(year=dt.year + n, day=dt.day - 1)
    # return dt.isoformat()[:10]
    return dt


def date_of_year(day: date, n: int = 0) -> Union[date, None]:
    """Change a date to the corresponding date in another year

    Parameters
    ----------
    n : int, optional
        by default 0, meaning no change is needed, just return the same date
        When `n=-1`, returns the same date one year ago
        When `n=-2`, returns the same date two year ago
        So on and soforth

        **Note**
        If the date `day` is the last day (29) of Febuary, and there is no
        Feb-29 in the n-th year. Return None

    Example
    -------
    >>> aycu.date_of_year(date('2019-12-07'), n=-2)
    '2017-12-07'
    >>> aycu.date_of_year(date('2020-02-29'), n=-2)
    None
    >>> aycu.date_of_year(date('2020-02-29'), n=-4)
    '2016-02-29'
    """
    if day.month == 2 and day.day == 29 and day.year % 4 == 0 and n != 0:
        return None
    dd = day + relativedelta(years=n)
    return dd


def previous_week_range(n: int = -1) -> Tuple[date, date]:
    """Get the date range of previous week

    When `n=-1`, returns the date range of one week ago
    When `n=-2`, returns the date range of two week ago
    So on and soforth

    Example
    -------
    >>> aycu.previous_week_range()
    ('2022-01-16', '2022-01-23')

    Returns
    -------
    Tuple[date, date]
    """
    weekday = date.today().weekday()
    start_delta = timedelta(days=weekday, weeks=-n)
    start_of_week = date.today() - start_delta - timedelta(days=1)
    end_of_week = start_of_week + timedelta(days=7)
    return start_of_week, end_of_week


def previous_month_range(n: int = -1) -> Tuple[date, date]:
    """Get the date range of previous month

    When `n=-1`, returns the date range of one month ago
    When `n=-2`, returns the date range of two month ago
    So on and soforth

    Example
    -------
    >>> aycu.previous_month_range()
    ('2021-12-01', '2021-12-31')
    >>> aycu.previous_month_range(n=-2)
    ('2021-11-01', '2021-11-30')

    Returns
    -------
    Tuple[date, date]
        [description]
    """
    today = date.today()
    last_month = today - relativedelta(months=-n)
    last_day = monthrange(last_month.year, last_month.month)

    return last_month.replace(day=1), last_month.replace(day=last_day[1])


def previous_quarter_range(n: int = -1) -> Tuple[date, date]:
    """Get the date range of previous quarter

    When `n=-1`, returns the date range of one quarter ago
    When `n=-2`, returns the date range of two quarter ago
    So on and so forth

    Example
    -------
    >>> aycu.previous_quarter_range()
    ('2021-10-01', '2021-12-31')

    Returns
    -------
    Tuple[date, date]
    """
    desired_date = pendulum.now().subtract(months=3 * -n)
    fst_day_of_quarter = datetime(desired_date.year, 3 * desired_date.quarter - 2, 1)
    last_day_of_quarter = fst_day_of_quarter + relativedelta(days=-1, months=3)
    return fst_day_of_quarter.date(), last_day_of_quarter.date()


def this_month_range(n: int = 0) -> Tuple[date, date]:
    """Get the date range of a month in year.

    Parameters
    ----------
    n : int, optional
        n-th year ago, by default 0
        When `n=0`, returns the date range of this year
        When `n=-1`, returns the date range of one year ago
        When `n=-2`, returns the date range of two year ago
        So on and soforth

    Example
    -------
    >>> aycu.this_month_range(n=-2)
    ('2020-01-01', '2020-01-31')
    """
    dt = datetime.now()
    today = date(dt.year, dt.month, dt.day)
    if n != 0:
        today = today_of_year(n)
    first_day_of_month = today.replace(day=1)
    last_day_of_month = first_day_of_month + relativedelta(months=1) - timedelta(days=1)
    return first_day_of_month, last_day_of_month


def this_month_range_til_today(n: int = 0) -> Tuple[date, date]:
    """Get the date range of from the beginning day of this month til today

    Parameters
    ----------
    n : int, optional
        n-th year ago, by default 0
        When `n=0`, consider only this year
        When `n=-1`, consider one year ago
        When `n=-2`, consider two year ago
        So on and soforth

    Example
    -------
    >>> aycu.this_month_range_til_today()
    ('2022-01-01', '2022-01-28')
    """
    dt = datetime.now()
    today = date(dt.year, dt.month, dt.day)
    if n != 0:
        today = today_of_year(n)
    first_day_of_month = today.replace(day=1)
    last_day_of_month = today
    return first_day_of_month, last_day_of_month


def last_weekend(n: int = -1) -> Tuple[date, date]:
    """Return the two date of last Saturday and Sunday

    Parameters
    ----------
    n : int, optional
        When `n=-1`, consider one week ago
        When `n=-2`, consider two week ago
        So on and soforth
    """
    dt = pendulum.now()
    last_week_dt = dt.subtract(days=7 * -n)
    print(last_week_dt)
    last_week_end = last_week_dt.end_of("week")  # ISO8601 week ends on Sunday
    last_week_start = last_week_end.subtract(days=1)
    return last_week_start.date(), last_week_end.date()


def previous_year_range(n: int = -1) -> Tuple[date, date]:
    """Get the date range of previous year

    Example
    -------
    >>> aycu.previous_year_range(n=-3)
    ('2019-01-01', '2019-12-31')

    Parameters
    ----------
    n : int, optional
        When `n=-1`, consider one year ago
        When `n=-2`, consider two year ago
        So on and soforth
    """
    dt = pendulum.now()
    last_year_dt = dt.subtract(years=1 * -n)
    last_year_start = last_year_dt.start_of("year")
    last_year_end = last_year_dt.end_of("year")
    return last_year_start.date(), last_year_end.date()


def week_of_year(d: date, mon_as_start_of_week: bool = True) -> int:
    """Get the week number from a date"""
    if mon_as_start_of_week:
        return int(d.strftime("%W")) + 1
    else:
        return int(d.strftime("%U")) + 1
