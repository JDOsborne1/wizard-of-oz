def taxbasic(income,baseratecut,baserate):
    takehome = baseratecut+((1 - baserate)*(income - baseratecut))
    return takehome
def inversetaxbasic(takehome,baseratecut,baserate):
    income = baseratecut+ ((1/(1-baserate))*(takehome-baseratecut))
    return income
