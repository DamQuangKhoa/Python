from functools import reduce
my_list = [1,2,3,4,5,6,44,23,424,24] 
def count(arr):
    return reduce((lambda x, y: x + 1), arr)
print(count(my_list))