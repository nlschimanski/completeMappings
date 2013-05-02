"""
Orthomorphisms(n,p)  - Given an integer n greater than 1 and a nonempty
                       list of equal length partial orthomorphisms as lists,
                       p, this function returns a complete set of
                       orthomorphisms on \Z[n]. To generate all orthomorphisms
                       for a given n, set p equal to
                       [[i] for i in range(pow(2,n))].
                       
ExtendByOne(n,p)     - The parameter n must be an integer greater than 1
                       and p must be a nonempty list of equal length partial
                       orthomorphisms. The function returns a list of all
                       partial orthomorphisms with lengths one more than
                       the input.

"""

def Orthomorphisms(n,partials):
    if len(partials[0])==pow(2,n):
        return partials
    else:
        return Orthomorphisms(n,ExtendByOne(n,partials))


def ExtendByOne(n,partials):
    newpartials = list()
    for item in partials:
        itemxor = [item[i]^i for i in range(len(item))]
        valid = list()
        for i in range(pow(2,n)):
            if i not in item and i^len(item) not in itemxor:
                valid.append(i)
        for i in valid:
            newpartials.append(item+[i])
    return newpartials
