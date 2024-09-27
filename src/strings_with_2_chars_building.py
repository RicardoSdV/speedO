from itertools import repeat
from string import Template
from sys import version

from src.z_data import data
from src.z_tester import tester


num = data.M

def concat():
    a, b = 1, 2
    for _ in repeat(None, num):
        _str = str(a) + '_' + str(b)


def percent_d():
    a, b = 1, 2
    for _ in repeat(None, num):
        _str = '%d_%d' % (a, b)

def percent_s():
    a, b = 1, 2
    for _ in repeat(None, num):
        _str = '%s_%s' % (a, b)

def frmt():
    a, b = 1, 2
    for _ in repeat(None, num):
        _str = '{}_{}'.format(a, b)

def join():
    a, b = 1, 2
    for _ in repeat(None, num):
        _str = '_'.join((str(a), str(b)))

def template():
    a, b = 1, 2
    templ = Template('{a}_{b}')
    for _ in repeat(None, num):
        _str = templ.substitute(a=str(a), b=str(b))

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
        a, b = 1, 2
        for _ in repeat(None, num):
            _str = f'{a}_{b}'

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
        template    0.6956   100  
        percent_d   0.3202   46   
        join        0.1452   21   
        concat      0.1418   20   
        frmt        0.1244   18   
        percent_s   0.0734   11   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.3973   100  
        join        0.1488   37   
        concat      0.1352   34   
        frmt        0.1003   25   
        percent_d   0.0944   24   
        percent_s   0.0853   21   
        fstrings    0.08     20   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.412    100  
        join        0.1285   31   
        concat      0.1266   31   
        frmt        0.1007   24   
        percent_d   0.0833   20   
        percent_s   0.0794   19   
        fstrings    0.0793   19   
        
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


