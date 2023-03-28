#Given a list of tuples, create a function that removes all empty tuples.

def rmv_empty_tuple(lst):
    return [tp for tp in filter(lambda x: x != (), lst)]

my_list = [(1,0), (2,0), (3,0), (0,0), (), ()]
new_list = rmv_empty_tuple(my_list)
print(f'''Given the list {my_list}, when I remove
all empty tuples I get {new_list}.''')