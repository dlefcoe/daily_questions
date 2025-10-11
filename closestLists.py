'''

This question is asked by Darren

given a set of lists that contain integer numbers
find the closest elements within the lists
one number must be selected from each list

for example a = [3, 5, 10], b = [1, 9, 15],  c = [4, 8]

the closest would be [8, 9, 10]


'''


import itertools as it


def closestElements(*lsts:list[list])->list:
    '''
    take a set of lists and return the closest element from each of the sets
    
    input: list of lists
    output: list of closest elements
    '''



    # list of possibilities
    allPossible = list(it.product(a, b, c))
    
    # initalise before loop
    rMin = max(a + b + c) - min(a + b + c) # r to largest possible
    result = None
    
    for i in allPossible:
        r = max(i) - min(i)
        if r < rMin:
            result = list(reversed(i))
            rMin = r

       


    return result


a = [3, 5, 10]
b = [1, 9, 15]
c = [4, 8]


done = closestElements(a, b, c)
print(done)

