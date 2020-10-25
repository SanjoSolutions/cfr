def iterate(fn, number_of_iterations, args=None):
    value = args
    for iteration_number in range(number_of_iterations):
        value = fn() if value is None else fn(value)
    return value
