"""
Number of unique characters in a string : Assume string size <= 20.
"abc" -> 3
"aaa" -> 1
"" -> 0
"abcdefgh" -> 8

Hint : Use set.
"""
def unique_chars(string):
    my_set = set()
    if len(string) > 20:
        return 0
    for char in string:
        my_set.add(char) 
    return len(my_set)
#print(unique_chars("pujaaaaaaa"))

assert(unique_chars('44444') == 1)
assert(unique_chars('a') ==1)
assert(unique_chars('sangansangan') == 4)
assert(unique_chars('as11as11sss') == 3)
assert(unique_chars('nasjdmjdjjdjjdjdjdjjdjdjd') == 0)

