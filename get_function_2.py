def get(string, func, bounds):
    try:
        value = func(input(string))
        if value in bounds:
            return value
        else:
            return get(string, func, bounds)
    except ValueError:
        return get(string, func, bounds)
