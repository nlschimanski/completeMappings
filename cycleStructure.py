k = 16 # when n is 4, k is 16 - if other dimensions are in play this need to change
'''
_____________________________________________________________________________
                     Functions defined in this file
_____________________________________________________________________________
cycle(i,perm)         - takes an element of the domain of a permutation and
                        a permutation and returns the cycle of the permutation
                        containing i.
cyclic(permutation)   - takes a permutation written in standard notation and
                        returns a the permutation written in cyclic notation
cycleType(cyclic)     - takes a permutation written in cyclic notation and
                        returns a list of integers that correspond to the
                        cycle type of the permutation
definitions to come
-orderOfPermutation
'''


def cycle(i,permutation):
    acycle = [i]
    y = permutation[i]
    while y not in acycle:
        acycle.append(y)
        y = permutation[y]
    return acycle

def cyclic(permutation):
    cycles = []
    taken = []
    for i in xrange(k):
        if i not in taken:
            cycles.append(cycle(i,permutation))
            taken += cycles[-1]
    return cycles


def cycleType(cycles):
    return [len(cycles[i]) for i in xrange(len(cycles))].sort()


        
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
                                                      
