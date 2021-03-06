__version__ = 'v1.0.0'

import os
from contextlib import contextmanager

@contextmanager
def workdir(path):
    """
    Takes a path and provides a context with that path as working directory.
    
    Args:
        path (str): Path the working directory should be changed to.
    
    Yields:
        None
        
    Raises:
        TypeError: If path is not string.
    """
    
    if not isinstance(path, str):
        raise TypeError('Path should be a string.')
    
    try:
        prev_wd = os.getcwd()
        os.chdir(path)
        yield
    finally:
        os.chdir(prev_wd)
