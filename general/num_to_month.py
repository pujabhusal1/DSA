'''def get_month_name (num):
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

if there is any invalid number, then return "invalid" 
Hint : use dictionariy's "not in" feature and also update 
unit test
''' 
'''def get_month_name (num):
    num = {1: "january", 2: "februry", 3: "march", 4: "april", 5: "may", 6: "june", 7: "july", 8: "august"}
    return num
assert(get_month_name(4) == "april")'''





'''Dictonary'''

def get_month_name(num):

    months = {
        1: "january",
        2: "february",
        3: "march",
        4: "april",
        5: "may",
        6: "june",
        7: "july",
        8: "august",
        9: "september",
        10: "october",
        11: "november",
        12: "December",
    }

    if num not in months:
        print("invalid")
        return "invalid"
    else: 
        print(months[num])
        return months[num]

assert get_month_name(1) == "january"
assert get_month_name(4) == "april"
assert get_month_name(9) == "september"
assert get_month_name(13) == "invalid"


    
