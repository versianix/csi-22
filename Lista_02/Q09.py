#Create a function that applies a function to 
#each row of a matrix, using map().

def filter_func(mtx, func):
    return list(map(func, mtx))


X = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
my_list = filter_func(X, sum)
print(my_list)