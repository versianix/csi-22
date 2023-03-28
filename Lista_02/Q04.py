#Create a function that verifies if all characters of a 
#string occurs in another string.

def is_in(str1, str2):
    count = 0
    for char in str1:
        if str2.count(char) > 0: 
            count += 1
    if count == len(str1): return True
    else: return False


print(f'Is the string "no" characters in "vision"? {is_in("no", "vision")}.\n')
print(f'Is the string "dog" characters in "computer"? {is_in("dog", "computer")}.')
