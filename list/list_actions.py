"""
Input : string of length <=20 all english alphabets only 
Output : Return a list

Action : transform string instructions to a list
a -> add 1 to the list
b -> add 2 to the list
c -> add 3 to the list
d -> add 4 to the list
e -> add 5 to the list
f -> If exists , pick the number from 0th index and append it. 
g -> If exists, pick the number from 1st index and append it. 
p -> pop from the list only if the list is non-empty ( len(...) > 0)
l -> append length of the list (len(....)) to the list
other characters : do nothing

"abc" -> [1, 2, 3]
"abcp" -> [1,2,3] -> p-> [1, 2]

"abcdpf" -> [1,2,3]
"abcdefghpl" -> [1, 2, 3, 4, 5, 1, 6]

[] -> 0th index -> Index out of bound error
"""

def transform_string(myString):
    ans = []
    alphabets = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,}

    for char in myString: 
      if char in alphabets:
        #print(alphabets[char])
        ans.append(alphabets[char])
      if char not in alphabets:
        if char == 'f':
           if len(ans) > 0:
              ans.append(ans[0])
        elif char == 'g':
           if len(ans) > 1:
              ans.append(ans[1])
        elif char == 'p':
                if len(ans) > 0:
                    ans.pop()
        elif char == 'l':
           if len(ans) > 0:
            ans.append(len(ans))
        
    return ans
         
      
#print (transform_string('pujaflu'))
assert transform_string('') == []
assert transform_string('xyz') == []
assert transform_string('a1a') == [1,1]
assert transform_string('qwertypujajnlg') == [1, 1, 1]
assert transform_string('pujaqqqweertttttt123456789900') == [1, 5, 5,]

        