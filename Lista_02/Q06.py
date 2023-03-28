#Using a generator, create a function that 
#traverses a list in reverse order.

def reverse_list(lst):
    for item in reversed(lst):
        yield item

my_list = [0, 1, 2, 3, 4, 5, 6, 7]
rl = reverse_list(my_list)
next(rl)
