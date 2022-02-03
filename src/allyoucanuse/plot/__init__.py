from pandas import DataFrame

def plot_1d(
    y:list,
    x:list,
    variant:str='bar',
    save2file:str=None)->None:
    """Plot a bar

    We can use the plotting function of pandas, by creating
    a DataFrame from x, y first, then plot them.

    We can also use other plotting package of python, if easier
    than dataframe.

    Parameters
    ----------
    y : list
        Data on the y-axis
    x : list
        Data on the x-axis

        `x` is allowed to be *empty*. If so, then we use a
        DataFrame which contains just one column from `y`
        and use the row number (indices) as the x-axis.

    variant : str
        Allowed values:
        
        * bar
        * line
        * donut 

    save2file : str
        When not empty, save the plot to a file.
    """
    raise NotImplementedError


def plot_2d(
    x1:list,
    x2:list,
    y:list,
    variant:str='stacked',
    save2file:str=None
)->None:
    """Plat a Stacked|Groupped bar chart

    Parameters
    ----------
    y : list
        Data of the y-axis
    x1 : list
        Data of the first x-axis
    x2 : list
        Data of the second x-axis
    variant : str
        Allowed values:
        
        * stacked: `y` values are stacked by `x2` and shown on each tick of `x1`
        * groupped: the `x2` is considered to be the groups 
        * heatmap: `x1` is the horizontal x-axis
            `x2` is the vertical x-axis
            `y` are the values of the heatmap cell

    save2file : str, optional
        When not empty, save the plot to a file.
    """
    raise NotImplementedError
