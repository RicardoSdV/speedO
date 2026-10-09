""" Containers have an empty fixed size, an average size per additional entry & a growth rate. Investigate & compare. """

from sys import getsizeof as g

print('Empty Sizes:')
print('Empty tuple size = %s bytes' % g(()))
print('Empty list  size = %s bytes' % g([]))
print('Empty dict  size = %s bytes' % g({}))
print('Empty set   size = %s bytes' % g(set()))

nums = [2**i for i in range(1, 24)]
ranges = [list(range(num)) for num in nums]
tupleSizes, listSizes, dictSizes, setSizes = [], [], [], []

for num, range in zip(nums, ranges):
    tupleSize = g(tuple([i for i in range])) / num
    listSize  = g([i       for i in range])  / num
    dictSize  = g({i: i    for i in range})  / num
    setSize   = g({i       for i in range})  / num

    tupleSizes.append(tupleSize)
    listSizes.append (listSize )
    dictSizes.append (dictSize )
    setSizes.append  (setSize  )

print('\nSize per element:')
print('Tuple size per element = %s bytes' % (round(sum(tupleSizes) / len(nums), 2)))
print('List  size per element = %s bytes' % (round(sum(listSizes)  / len(nums), 2)))
print('Dict  size per element = %s bytes' % (round(sum(dictSizes)  / len(nums), 2)))
print('Set   size per element = %s bytes' % (round(sum(setSizes)   / len(nums), 2)))


"""
Conclusion:

Python27:
    Empty Sizes:
    Empty tuple size = 48 bytes
    Empty list  size = 64 bytes
    Empty dict  size = 272 bytes
    Empty set   size = 224 bytes
    
    Size per element:
    Tuple size per element = 11.0 bytes
    List  size per element = 14.0 bytes
    Dict  size per element = 78.0 bytes
    Set   size per element = 55.0 bytes
    
Python38:
    Empty Sizes:
    Empty tuple size = 40 bytes
    Empty list  size = 56 bytes
    Empty dict  size = 64 bytes
    Empty set   size = 216 bytes
    
    Size per element:
    Tuple size per element = 11.33 bytes
    List  size per element = 14.43 bytes
    Dict  size per element = 50.53 bytes
    Set   size per element = 55.33 bytes
    
Python310:
    Empty Sizes:
    Empty tuple size = 40 bytes
    Empty list  size = 56 bytes
    Empty dict  size = 64 bytes
    Empty set   size = 216 bytes
    
    Size per element:
    Tuple size per element = 11.33 bytes
    List  size per element = 14.29 bytes
    Dict  size per element = 50.53 bytes
    Set   size per element = 55.33 bytes

Python312:
    Empty Sizes:
    Empty tuple size = 40 bytes
    Empty list  size = 56 bytes
    Empty dict  size = 64 bytes
    Empty set   size = 216 bytes
    
    Size per element:
    Tuple size per element = 11.33 bytes
    List  size per element = 14.29 bytes
    Dict  size per element = 49.86 bytes
    Set   size per element = 55.33 bytes
    
Python314:
    Empty Sizes:
    Empty tuple size = 48 bytes
    Empty list  size = 56 bytes
    Empty dict  size = 64 bytes
    Empty set   size = 216 bytes
    
    Size per element:
    Tuple size per element = 12.0 bytes
    List  size per element = 14.29 bytes
    Dict  size per element = 49.86 bytes
    Set   size per element = 55.33 bytes
"""
