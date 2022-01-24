dollar_euro  = 0.88
euro_pound = 0.84


def dollar_to_euro(amount):
    amount *= dollar_euro
    return amount


def  euro_to_dollar(amount):
    amount /= dollar_euro
    return amount


def euro_to_pound(amount):
    amount *= euro_pound
    return amount


def pound_to_euro(amount):
    amount /= euro_pound
    return amount
 