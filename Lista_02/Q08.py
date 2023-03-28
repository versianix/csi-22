#Create a function that filters the even numbers of a list.

def filter_even(lst):
    return [num for num in filter(lambda x: x % 2 == 0, lst)]

my_list = [0, 2, 5, 8, 9, 11, 13, 14, 17, 20, 21]
print(f'''The filtered list {my_list} 
of even numbers only is {filter_even(my_list)}.''')