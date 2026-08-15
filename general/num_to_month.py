def get_month_name (num):
    if num == 1:
        return "january"
    elif num == 2:
        return "feburay"
    elif num == 3:
        return "march"
    elif num == 4:
        return "april"
    elif num == 5:
        return "may"
    elif num == 6:
        return "june"
    elif num == 7:
        return "july"
    elif num == 8:
        return "august"
    elif num == 9:
        return "september"
    elif num == 10:
        return "october"
    elif num == 11:
        return "november"
    elif num == 12:
        return "december"

assert(get_month_name(1) == "january")
assert(get_month_name(4)) == "april"
assert(get_month_name(8)) == "august"
assert(get_month_name(12)) == "december"

    
