from itertools import repeat
from string import Template
from sys import version

from src.z_data import data
from src.z_tester import tester


num = data.M

def concat():
    a = 2
    _str1 = '1_'
    for _ in repeat(None, num):
        _str2 = _str1 + str(a)

def percent_d():
    a = 2
    _str1 = '1_%d'
    for _ in repeat(None, num):
        _str = _str1 % a

def percent_s():
    a = 2
    _str1 = '1_%s'
    for _ in repeat(None, num):
        _str = _str1 % a

def frmt():
    a = 2
    _str1 = '1_{}'
    for _ in repeat(None, num):
        _str = _str1.format(a)

def join():
    a = 2
    _str1 = '1_'
    for _ in repeat(None, num):
        _str = ''.join((_str1, str(a)))

def template():
    a = 2
    templ = Template('1_{a}')
    for _ in repeat(None, num):
        _str = templ.substitute(a=str(a))

_callables = [
    concat,
    percent_s,
    percent_d,
    frmt,
    join,
    template,
]

if version.startswith('3'):

    def fstrings():
        a = 2
        _str1 = '1_'
        for _ in repeat(None, num):
            _str = f'{_str1}{a}'

    _callables.append(fstrings)


tester(
    _callables
)


"""
Conclusion:
    - In python27 %s fastest, by far
    
    - In python3 fstrings fastest but normally very
    close to %s, so %s is a good version bridge
    
    Python27: 
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.5742   100  
        percent_d   0.1618   28   
        join        0.0924   16   
        frmt        0.0834   15   
        concat      0.0642   11   
        percent_s   0.0454   8    
    
    Python38:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.2951   100  
        join        0.0894   30   
        frmt        0.0756   26   
        concat      0.0716   24   
        percent_d   0.0558   19   
        percent_s   0.0539   18   
        fstrings    0.051    17   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.3152   100  
        join        0.0812   26   
        frmt        0.0722   23   
        concat      0.064    20   
        percent_d   0.0513   16   
        percent_s   0.0499   16   
        fstrings    0.0485   15   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.3141   100  
        frmt        0.1136   36   
        percent_d   0.1006   32   
        join        0.099    32   
        concat      0.0954   30   
        percent_s   0.0792   25   
        fstrings    0.0781   25   
"""
