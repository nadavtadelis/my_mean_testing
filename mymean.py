"""
This is a 'module' for practice using git with travis and conda to create automatic tests
"""

def mean(num_list):
    """Compute the mean of a list of numbers"""
    first = num_list[0]
    if isinstance(first, complex):
        return NotImplemented
    return sum(num_list)/len(num_list)
