""" this is a very specific test for when you need to iterate over a slice of a
list where you may need to advance more than one iteration per loop.
"""

from src.z_data import data
from itertools import islice

from src.z_tester import auto_tester

num = data.k10
ints = range(num)

def islice_and_next(islice=islice, next=next, ints=ints):
    for i in ints:
        iterInts = islice(ints, i)
        try:
            while True:
                next(iterInts)
        except StopIteration:
            continue

def slice_and_next(next=next, ints=ints, iter=iter):
    for i in ints:
        iterInts = iter(ints[i:])
        try:
            while True:
                next(iterInts)
        except StopIteration:
            continue

def while_index(ints=ints):
    _len = len(ints)
    for i in ints:
        while i < _len:
            ints[i]
            i += 1

def while_true_and_except(ints=ints):
    for i in ints:
        try:
            while True:
                ints[i]
                i += 1
        except IndexError:
            continue

auto_tester()


"""
Conclusion:
- In python2 indexing is better, but not by much, in python3 adding integers is so expensive, copying an entire list is cheaper, lol.

Python27:
Name              Secs    %    
islice_and_next   1.522   100  
slice_and_next    1.497   98   
while_index       1.224   80  

Python38:
Name              Secs     %    
while_index       2.4887   100  
islice_and_next   0.7179   28   
slice_and_next    0.675    27 

Python310:
Name              Secs     %    
while_index       2.1789   100  
islice_and_next   0.7673   35   
slice_and_next    0.7191   33 

Python312:
Name              Secs     %    
while_index       2.4989   100  
islice_and_next   0.8929   36   
slice_and_next    0.8363   33  

Python314:
Name                    Secs     %    
while_index             2.3369   100  
while_true_and_except   2.0902   89   
islice_and_next         0.9114   39   
slice_and_next          0.8722   37   

"""


