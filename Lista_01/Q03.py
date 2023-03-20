def sum_to(n):
    if(n == 0):
        return 0;
    return (n + sum_to(n-1))

n = 10
print(f'The sum of all integers numbers up to and including {n} is {sum_to(n)} !')