def mean(num_list):
    "Compute the mean of a list of numbers"
    first = num_list[0]
    if isinstance(first, complex):
        return NotImplemented
    return sum(num_list)/len(num_list)