def get(St = "Input?: ", func):
    try:
        Va = func(input(St))
        return Va
    except ValueError:
        return get(St,func) 

