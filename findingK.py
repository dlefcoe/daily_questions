'''

Given an array of numbers and a number k, 
determine if there are three entries in the array which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

'''

import itertools


def findK(a, k):
    '''
    given an array of numbers and a value k, find 3 numbers that add to k

    input:
        a: array of numbers
        k: value to be found

    return:
        true: numbers are found
        false: nothing found
        numbers that add to k
    '''
    valsToK = False
    
    aCombs = itertools.combinations(a, 3)
    for i in aCombs:
        if sum(i) == k:
            # k is found
            valsToK = True
            print(i)

    return valsToK
    




# input params
arrayToTest = [20, 303, 3, 4, 25]
specifiedNumber = 49

# call the function
result = findK(arrayToTest, specifiedNumber)
print(result)


'''

Given an array of numbers and a number k, 
determine if there are three entries in the array which add up to the specified number k. 
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.

'''

import itertools


def findK(a, k):
    '''
    given an array of numbers and a value k, find 3 numbers that add to k

    input:
        a: array of numbers
        k: value to be found

    return:
        true: numbers are found
        false: nothing found
        numbers that add to k
    '''
    valsToK = False
    
    aCombs = itertools.combinations(a, 3)
    for i in aCombs:
        if sum(i) == k:
            # k is found
            valsToK = True
            print(i)

    return valsToK
    




# input params
arrayToTest = [20, 303, 3, 4, 25]
specifiedNumber = 49

# call the function
result = findK(arrayToTest, specifiedNumber)
print(result)



'''
the end
'''
