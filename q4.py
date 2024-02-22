##Mahgoub Mohamed
##60304062

def kMin(lst, k):
    '''Find and return the k smallest elements from a given list in ascending order.'''
    if k > len(lst):
        return sorted(lst)
    
    x = []
    lste = lst.copy()
    
    for i in range(k):
        h = min(lste)
        x.append(h)
        lste.remove(h)
        
    x.sort() 
    return x
