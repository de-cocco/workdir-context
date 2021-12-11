import os
from contextlib import contextmanager

@contextmanager
def workdir(path):
    """
    Takes a path and provides a context with that path as working directory
    
    Args:
        path (str): path the working directory should be changed to
    
    Yields:
        None
        
    Raises:
        TypeError: If path is not string
    """
    
    try:
        if not isinstance(path, str):
            raise TypeError('Path should be a string')
        
        prev_wd = os.getcwd()
        os.chdir(path)
        yield
        
    finally:
        os.chdir(prev_wd)
