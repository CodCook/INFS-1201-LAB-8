##Mahgoub Mohamed
##60304062

def matrixAdd(first, second):
    '''Add two matrices element by element.'''
    
    assert len(first) == len(second), "Matrices must have the same number of rows"
    
    for i in range(len(first)):
        assert len(first[i]) == len(second[i]), f"Row {i+1} has different number of elements"
    
    final = []
    for i in range(len(first)):
        raw = []
        for j in range(len(first[i])):
            raw.append(first[i][j]+second[i][j])
        final.append(raw)
    return final

