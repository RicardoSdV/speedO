from itertools import repeat
from string import Template
from sys import version

from src.z_data import data
from src.z_tester import tester


num = data.M
_a, _b, _c = '1', '2', '3'


def concat():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        _str = a + b + c

def percent_s():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        _str = '%s%s%s' % (a, b, c)

def frmt():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        _str = '{}{}{}'.format(a, b, c)

def join_and_make_tuple():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        _str = ''.join((a, b))

def join_with_existing_tuple():
    abc = (_a, _b, _c)
    for _ in repeat(None, num):
        _str = ''.join(abc)

def template():
    a, b, c = _a, _b, _c
    templ = Template('{a}{b}{c}')
    for _ in repeat(None, num):
        _str = templ.substitute(a=a, b=b, c=c)

_callables = [
    concat,
    percent_s,
    frmt,
    join_and_make_tuple,
    join_with_existing_tuple,
    template,
]

if version.startswith('3'):

    def fstrings():
        a, b, c = _a, _b, _c
        for _ in repeat(None, num):
            _str = f'{a}{b}{c}'

    _callables.append(fstrings)


tester(
    _callables
)


"""
Conclusion: 
    - In python3 fstrings
    
    - In python2 concat or .join
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                       Secs     %    
        template                   0.5968   100  
        frmt                       0.137    23   
        percent_s                  0.0696   12   
        join_and_make_tuple        0.0444   7    
        concat                     0.0382   6    
        join_with_existing_tuple   0.0362   6    
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                       Secs     %    
        template                   0.2377   100  
        frmt                       0.0944   40   
        percent_s                  0.0757   32   
        join_and_make_tuple        0.0382   16   
        concat                     0.0351   15   
        join_with_existing_tuple   0.0334   14   
        fstrings                   0.0328   14   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                       Secs     %    
        template                   0.2836   100  
        frmt                       0.094    33   
        percent_s                  0.075    26   
        join_and_make_tuple        0.0418   15   
        concat                     0.0387   14   
        fstrings                   0.0354   12   
        join_with_existing_tuple   0.0338   12   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                       Secs     %    
        template                   0.2368   100  
        frmt                       0.1023   43   
        percent_s                  0.0435   18   
        concat                     0.0378   16   
        join_and_make_tuple        0.0351   15   
        fstrings                   0.0317   13   
        join_with_existing_tuple   0.0308   13   

"""


