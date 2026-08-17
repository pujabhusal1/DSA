"""
Write a function is_palindrome(str1) returns 
True if it is palindrome 

"abc" -> "cba" -> False
"aba" -> "aba" -> True

Return boolean value True or False.
"""
def is_palindrome(str1):
    reversed = ""
    for i in str1:
        reversed = i + reversed
        #print(reversed)
    #return reversed 
    if reversed == str1:
        return True
    else: 
        return False
    
(is_palindrome('ata'))

assert is_palindrome(' ') == True
assert is_palindrome('121') == True
assert is_palindrome('321') == False
assert is_palindrome('aaaaabbbbbaaaaa') == True
assert is_palindrome('22223333344442223') == False  
assert is_palindrome('11__22__11') == True