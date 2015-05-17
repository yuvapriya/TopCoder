# Problem Statement http://community.topcoder.com/stat?c=problem_statement&pm=10240
def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf
def SuperSum(k , n):
    if (k == 0):
        return n 
    s = 0   
    for i in range(1, n+1):
        s += SuperSum(k-1, i)
    return s

SuperSum = memoize(SuperSum)
print SuperSum(14,14)