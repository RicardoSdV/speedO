from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M10

def min_and_mult():
    for _ in repeat(None, num):
        min(0.3, 0.1*0.5)

const = 0.1*0.5
def min_and_const():
    for _ in repeat(None, num):
        min(0.3, const)

def min_and_default(_const=const):
    for _ in repeat(None, num):
        min(0.3, _const)

def if_and_default(_const=const):
    for _ in repeat(None, num):
        0.3 if 0.3 < _const else _const

auto_tester()

"""
Python 27:
Name              Secs     %    
min_and_const     0.5358   100  
min_and_mult      0.5158   96   
min_and_default   0.515    96   
if_and_default    0.1668   31   

Python 312:
Name              Secs     %    
min_and_const     0.511    100  
min_and_mult      0.5024   98   
min_and_default   0.4933   97   
if_and_default    0.1093   21   
"""
