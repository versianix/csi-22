#Create a function that given a tuple of tuples, return a 
#tuple of the average of the given tuples.

def avg_tuple(tuples):
    average = []
    for tpl in tuples:
        avg = 0
        for num in tpl:
            avg += num
        average.append(avg/len(tpl))
    return tuple(average)


my_tuple = ((2,3,4),(3,4,5,6),(2,4),(4,8,9))
new_tuple = avg_tuple(my_tuple)
print(f'The average of the touple {my_tuple} is {new_tuple}.')