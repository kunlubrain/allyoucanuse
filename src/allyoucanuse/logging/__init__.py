"""
ref
* [1] https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal

This is collection of logging functions to print *colorful* logging message in terminal
"""
import inspect
import logging
from typing import Any, Iterable

# from icecream import ic

_logging_banner = "=" * 60


class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    green = "\33[32m"
    reset = "\x1b[0m"

    format = (
        # "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
        "%(message)s"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: green + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logging_config(
    level: int,
    logging_file: str,
    logging_format: str = "%(asctime)s %(levelname)s %(message)s",
):
    _validlevel = level in (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR)
    assert _validlevel, f"{level} is not supported. Expected debug|info|warning|error"
    logging.basicConfig(filename=logging_file, format=logging_format, level=level)


def get_logger(loggername: str) -> ...:
    """Get a standard logger with a given name"""
    # init_logging_config(level=logging.DEBUG, logging_file="logging.log")
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger


logger = get_logger(__name__)


def log_start_step(msg: str) -> None:
    """Print a `start` message before starting a task

    Example
    -------
    >>> log_start_step('XYZ')
    >>> for i in range(1000):
    >>>     ...
    >>> log_finish_step('XYZ')
    """
    # logger.info(f"{_logging_banner}")
    logger.debug(_logging_banner)
    logger.info(f"🚗 START: {msg}")

    # Pick one unicode icon e.g.
    # https://unicode-table.com/en/1F680/
    # or
    # https://unicode-table.com/en/search/?q=beer

    # Color of text in this message = blue
    # return 1
    # raise NotImplementedError(
    #     "Show a nice logging message with *color text* as in [1]. E.g. an icon + 'green' START + the msg"
    # )


def log_one_step(msg: str, fa_icon: str = "arrow-right") -> None:
    """Print a log message for one `step` of task

    Parameters
    ----------
    msg : str
        A message passed by the caller

    Example
    >>> log_step(msg="Do sth")
    ⇨ Do sth
    """
    logger.warning(f"➤ {msg}")

    # We may need our own Logger - inherit from the standard logger
    # in order to implement our specific logging syntax/message
    #
    # icon: pick one from
    # https://unicode-table.com/en/search/?q=arrow
    # ⇨ Do sth
    # ➤
    #
    # Color of text in this message = yellow
    # raise NotImplementedError


def log_finish_step(msg: str) -> None:
    # Color of text in this message = green
    logger.info(f"🍺 FINISH: {msg}")


def flog(msg: str, nth_last_caller: int = 2):
    """Show log of the caller function

    Parameters
    ----------
    msg : str
        A message passed by the caller
    nth_last_caller: int
        Backtrace to the n-th caller

    Example
    >>> def foo():
    >>>     flog('some debug message')

    """
    _caller = inspect.stack()[nth_last_caller].function
    print(f"{_caller}: {msg}")


def logthefunc(fn: Any):
    """A decrator used for debugging.

    It prints out the value of args of the callee.

    Ref:
    * https://stackoverflow.com/questions/25936746/create-a-function-decorator-that-logs-arguments/25937594#25937594
    * https://www.vitoshacademy.com/python-writing-a-logger-in-python-with-a-decorator/
    * https://pypi.org/project/logwrap/ This might be too complex to use

    Example
    -------
    >>> @aycu.logthefunc
    >>> def foo():
    >>>   pass
    print the params of foo()
    """

    def func(*a: Any, **kw: Any) -> Any:
        # log_one_step(f"{fn}({a}, {kw})")
        logger.info(f"{fn} with args: {a}, kws: {kw}")
        return fn(*a, **kw)

    return func


_default_item_sep = "\n" + "-" * 60


def log_iters(
    sequence: Iterable[Any], item_msg: str = "", item_sep: str = _default_item_sep
) -> None:
    """Log each *item* in the sequence.

    Parameters
    ----------
    sequence : Iterable
        It can be an iterable (e.g. list) of anything.
        If the item is a dict, then just print the dict
    item_msg: str
        Prefix message for each item

    Example
    >>> a [1, 2, 3]
    >>> aycu.log_iter(a, item_msg='score')
    score: 1
    ------------------------------------------------------------
    score: 2
    ------------------------------------------------------------
    score: 3
    """
    for item in sequence:
        if isinstance(item, dict):
            logger.info(item_msg + ": " + str(item))
        else:
            logger.info(item_msg + ": " + str(item))
        logger.info(item_sep)


def log_bump_indent() -> None:
    """When called, the default indent of the log message is increased

    Example
    >>> aycu.log_one_step(msg='hello')
    hello
    >>> aycu.log_bump_indent()
    >>> aycu.log_one_step(msg='world')
        world
    >>> aycu.log_bump_indent()
    >>> aycu.log_one_step(msg='foo')
            foo
    >>> aycu.log_one_step(msg='bar')
            bar
    >>> aycu.log_reset_indent()
    >>> aycu.log_one_step(msg='bar')
    bar
    >>> aycu.log_bump_indent()
    >>> for i in [1,2]:
    >>>     aycu.log_one_step(msg=i)
    >>>     aycu.log_bump_indent()
    >>>     for j in [4, 5]:
    >>>         aycu.log_one_step(msg=j)
    >>>     aycu.log_reduce_indent()
        1
            4
            5
        2
            4
            5
    """
    raise NotImplementedError


def log_reset_indent() -> None:
    """Rest the indent level of the logging messages - i.e. no indent

    Example
    >>> help(aycu.log_bump_indent)
    """
    raise NotImplementedError


def log_reduce_indent() -> None:
    """Decrease the indent level

    Example
    >>> help(aycu.log_bump_indent)
    """
    raise NotImplementedError
