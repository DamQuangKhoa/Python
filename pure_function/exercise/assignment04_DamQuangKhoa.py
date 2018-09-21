from functools import reduce
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70] 
my_list3= [1, 2, 3, 1, 2, 4, 2, 3]
# my_list = [1,2,3,4,5,6,44,23,424,24]
my_dic =  {'a': [1, 2], 'b': [3, 4], 'c': [5, 6]} 
def sumElement(listData):
   return reduce(
     (lambda x, y: x + y), listData
     )    

def countElement(listData):
    count = reduce(
        (lambda x,y: x+1) 
        ,listData,0
        )
    return count

def findMin(listData):
    return reduce(
        (lambda x,y: x if x<y else y)
        ,listData
    )
#  x la phan tu dau tien , y la phan tu ke tiep , y chay trong danh sach
def findMax(listData):
     return reduce(
        (lambda x,y: x if x>y else y)
        ,listData
    ) 
def removeNumberBy3(listData):
    return list(
        filter(
            (lambda x: x%3 != 0),listData
        )
    )
def flattenObject(listObject):
    return reduce(
        (lambda x,y: x+ y)
        ,listObject.values()
    )
# def groupByN(listData,number):
#     return reduce(
#         (lambda parameter_list: expression)
#     )      
def countNumberOfOccurrences(arr):
    return dict(map(lambda x  : (x , list(arr).count(x)) , arr))   
def splitIntoOddAndEven(arr):
    return list(
        filter(
            (lambda x: x%2==0)
            ,arr
        ) + list(
            filter(
                (lambda x: x%2 != 0)
                ,arr
            )
        )
    )    
    
print('number item is : ' + str(countElement(my_list)))
print('min number is : ' + str(findMin(my_list)))
print('max number is : ' + str(findMax(my_list)))
print(' number not devide to 3 is : ' + str(removeNumberBy3(my_list)))
print(' flatten dictionary: ' + str(flattenObject(my_dic)))
print('Count the number of occurrences of each items ' + str(countNumberOfOccurrences(my_list3)))
print('Split an array into 2 arrays of odd and even numbers ' + str(splitIntoOddAndEven(my_list)))


