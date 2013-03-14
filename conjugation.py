'''
** Issues to fix: make all permutations tuples
_____________________________________________________________________________
                     Functions defined in this file
_____________________________________________________________________________
bases()             - generates a list of linearly independent elements of \Z
automorphism(basis) - generates an automorphism in standard notation given
                      the image of e_1,...,e_4
allAutomorphisms()  - generates all automorphisms of \Z in standard notation
generateH()         - returns the subspace of Aut(\Z) whose elements fix e_1,
                      e_2,e_3
conjugate(pi,g)     - returns the permutation g pi g^{-1}
stabCheck(pi,H)     - returns the non-identity elements in the stabilizer of
                      pi under the action of conjugation by the group H
stabCheckAll(ol,H)  - returns a list of pairs with the first element a complete
                      map and the second non-identity elements of the stabilizer
G_orbit(pi,H)       - returns the orbit of the element pi under the action of
                      conjugation by elements in the group H
fix(g,ol)           - returns a list of complete maps that are fixed by the
                      automorphism g
'''


# generates four linearly independent elements of the vector space Z_2^n
def bases():
    bases = []
    for i in range(1,16):
        for j in range(1,16):
            if j==i:
                continue
            for k in range(1,16):
                if k==i or k==j or k==i^j:
                    continue
                for l in range(1,16):
                    if l==i or l==j or l==k or l==i^j or l==i^k or l==j^k or l==i^j^k:
                        continue
                    bases.append([i,j,k,l])
    return bases


# Takes the image of basis elements of an automorphism of \Z and returns
# the entire automorphism in standard notation, that is,
# automorphisms(basis) returns a list, l, such that the image of k is l[k].
def automorphisms(basis):
    autom = [0,basis[0],basis[1],basis[0]^basis[1],basis[2],basis[2]^basis[0],basis[2]^basis[1],basis[2]^basis[1]^basis[0]]
    orphism = [basis[3]^autom[i] for i in range(8)]
    return tuple(autom + orphism)

# Generates all automorphisms
def allAutomorphisms():
    return [automorphisms(item) for item in bases()]

# Generates the subspace of Aut(Z_2^n) that fixes e_1,e_2,e_3.
def generateH(): 
    autos = []
    for k in xrange(8,16):
        auto = range(8)+[k]+[k^i for i in range(1,8)]
        autos.append(auto)
    return tuple(autos)


# Conjugates a complete map by an automorphism.
# Inputs are complete map pi and automorphism g.
def conjugate(pi,g):
    return [g[pi[g.index(i)]] for i in range(16)]


# Given a subgroup of Aut(\Z), H, stabCheck returns all the nonidentity
# elements in the stabilizer of the complete map pi (with group action
# of conjugation).
def stabCheck(pi,H):
    stab = []
    for g in H[1:]:
        if conjugate(pi,g) == pi:
            stab.append(g)
    return stab

def stabilizer(pi,H):
    stab = []
    for g in H:
        if tuple(conjugate(pi,g)) == tuple(pi):
            stab.append(g)
    return stab


# Returns a list of pairs: (complete map, stabilizer elements) so long
# as non-identity stabilizer elements exist.
def stabCheckAll(orthos,H):
    pairs = []
    for item in orthos:
        stab = stabCheck(item,H)
        if len(stab) != 0:
            pairs.append([item,stab])
    return pairs


# Returns the orbit of a complete map pi
def G_orbit(pi,H):
    return list(set([tuple(conjugate(pi,g)) for g in H]))


# Returns a list of complete maps fixed by an autormophism G
def fix(g,orthos):
    return [item for item in orthos if tuple(conjugate(item,g))==tuple(item)]

# Given a complete map pi, this function returns the complete map pi+id
def addxtransformation(pi):
    return tuple([pi[i]^i for i in range(len(pi))])

# Given a complete map pi and an element, l, of \Z, this function returns
# the complete map pi+l
def addktransformation(pi,l):
    return tuple([pi[i]^l for i in range(len(pi))])
