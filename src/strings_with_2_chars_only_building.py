from itertools import repeat
from string import Template
from sys import version

from src.z_data import data
from src.z_tester import tester


num = data.M

def concat():
    a, b = '1', '2'
    for _ in repeat(None, num):
        _str = a + b

def percent_s():
    a, b = '1', '2'
    for _ in repeat(None, num):
        _str = '%s%s' % (a, b)

def frmt():
    a, b = '1', '2'
    for _ in repeat(None, num):
        _str = '{}{}'.format(a, b)

def join_and_make_tuple():
    a, b = '1', '2'
    for _ in repeat(None, num):
        _str = ''.join((a, b))

def join_from_existing_tuple():
    ab = ('1', '2')
    for _ in repeat(None, num):
        _str = ''.join(ab)

def template():
    a, b = '1', '2'
    templ = Template('{a}{b}')
    for _ in repeat(None, num):
        _str = templ.substitute(a=a, b=b)

_callables = [
    concat,
    percent_s,
    frmt,
    join_and_make_tuple,
    join_from_existing_tuple,
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
        template    0.6632   100  
        join        0.1302   20   
        frmt        0.1098   17   
        percent_s   0.0576   9    
        concat      0.0208   3    
        
    Python38:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.3261   100  
        join        0.0976   30   
        fstrings    0.08     25   
        frmt        0.0773   24   
        percent_s   0.0625   19   
        concat      0.0225   7    
        
    Python310:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.3412   100  
        join        0.0886   26   
        frmt        0.0764   22   
        fstrings    0.0759   22   
        percent_s   0.0624   18   
        concat      0.0245   7    
        
    Python312:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        template    0.2469   100  
        frmt        0.0823   33   
        fstrings    0.0754   31   
        join        0.0506   20   
        percent_s   0.0333   13   
        concat      0.021    9    

"""


