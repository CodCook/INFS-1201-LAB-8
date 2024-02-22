##Mahgoub Mohamed
##60304062

def randList(size):
    '''Generate a list of integers in random order.'''
    from random import shuffle
    x = list(range(1,size+1))
    shuffle(x)
    return x

