'''


Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.


solution taken from c++ code and converted to python
relies on fact that TF = FT

'''



import random

def biased_cointoss():
    ''' Return result of a 83% biased cointoss.'''
    bias = 83  # 50 here would be unbiased
    return bias / 100 - 0.5 + random.random() > 0.5
    

def unbiased_toss():
    ''' Return result of an unbiased cointoss using biased_cointoss().'''
    toss1 = biased_cointoss()
    toss2 = biased_cointoss()

    # True, False must have the same probaility as False, True.
    if (toss1, toss2) == (False, True):
         return True
    elif (toss1, toss2) == (True, False):
        return False

    else:
        # Reject result if both tosses are the same
        return unbiased_toss()


def main():
    ''' the main function '''
    # Do one thousand tosses to test 83% bias
    x = [biased_cointoss() for x in range(1000)]
    print(x.count(True), "<-- should be around 830", f'the diff is {x.count(True)-830}')

    # Do one thousand tosses to test unbiasededness 
    x = [unbiased_toss() for x in range(1000)]
    print(x.count(True), "<-- should be around 500", f'the diff is {x.count(True)-500}')



# main guard idiom
if __name__=='__main__':
    main()