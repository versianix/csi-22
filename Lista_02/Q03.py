#Given a list of strings, create a function that process that list
#and returns a new list with alphanumeric strings only.

def filter_alpha(lst):
    return [word for word in filter(lambda x: x.isalnum(), lst)]


my_list = ['Carro', 'Vas$oura', 'Compensação', '23 Reais', 'marcel@gmail', 'Tudo bem!']
new_list = filter_alpha(my_list)
print(f'''When I filter the list {my_list}
to a new one that only has alphabetic and number characters, I get: {new_list}.''')