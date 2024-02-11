try:
    import numpy as np

    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False


def add_arr(list1, list2):
    """
    Summation of two lists. Uses NumPy if available, otherwise falls back to manual summation.

    Parameters:
    - list1: First list of numbers.
    - list2: Second list of numbers.

    Returns:
    - The sum of list1 and list2.
    """
    if NUMPY_AVAILABLE:
        arr1 = np.array(list1)
        arr2 = np.array(list2)
        return (arr1 + arr2).tolist()
    else:
        return [x + y for x, y in zip(list1, list2)]
