my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70 ] 
my_list2 = ["geeks", "geeg", "keek", "practice", "aa"]
def devideBy(data,number):
    return list(
        filter(
            lambda x: (x % number == 0),data
        )
    )
def findPalindromes(listData):
    return list(
        filter(
            lambda data: isPalindromes(data),listData
        )
    )
def isPalindromes(data):
    result = (data == "".join(reversed(data)))
    return result      

# def findPalindromes(listData):
#     return list(
#         filter(
#             lambda x: (x == "".join(reversed(x)),listData
#         )
#     )
#     )

result = findPalindromes(my_list2)

print(result)



