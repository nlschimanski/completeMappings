"""
Orthomorphisms(p,n)  - Given an integer n greater than 1 and a nonempty
                       list of equal length partial orthomorphisms as lists,
                       p, this function returns a complete set of
                       orthomorphisms on Z_2^n. To generate all orthomorphisms
                       for a given n, set p equal to
                       [[i] for i in range(pow(2,n))].

"""

def Orthomorphisms(partials,n):
    while len(partials[0]) != pow(2,n):
        newpartials = []
        for item in partials:
            itemxor = [item[i]^i for i in range(len(item))]
            valid = list()
            for i in range(pow(2,n)):
                if i not in item and i^len(item) not in itemxor:
                    valid.append(i)
            for i in valid:
                newpartials.append(item+[i])
        partials = newpartials
    return partials
