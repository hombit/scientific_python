"""This documentation example"""


def swap_optional(x, y=None):
    """Change order of arguments
    
    Full multiline ... . .. . . .
    description of the function .. 
    
    Parameters:
    -----------
    x : float
        Positive number in cm
    y : float, optional
        Positive number in kg, default is None
    
    Returns:
    -------
    float or None : 
        Second parameter
    float : 
        First parameter
        
    Examples:
    ---------
    
    >>> x = 1
    >>> if x == 0:
    ...     print('x is 0')
    ... else:
    ...     print('x is not zero')
    x is not zero
    
    """
    return (y, x)
