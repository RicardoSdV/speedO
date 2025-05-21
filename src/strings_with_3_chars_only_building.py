from itertools import repeat
from sys import version

from src.z_data import data
from src.z_tester import tester


num = data.M10
_a, _b, _c = '1', '2', '3'


def concat():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        a + b + c

def percent_s():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        '%s%s%s' % (a, b, c)

def frmt():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        '{}{}{}'.format(a, b, c)

def join_and_make_tuple():
    a, b, c = _a, _b, _c
    for _ in repeat(None, num):
        ''.join((a, b))

def join_with_existing_tuple():
    abc = (_a, _b, _c)
    for _ in repeat(None, num):
        ''.join(abc)

def predef_join_make_tuple():
    a, b, c = _a, _b, _c
    join = ''.join
    for _ in repeat(None, num):
        join((a, b))

# Templates are so slow it slows down the test so much its not even worth having.
# they are 10x slower than the next slowest way.
# from string import Template
# def template():
#     a, b, c = _a, _b, _c
#     subs = Template('$a$b$c').substitute
#     for _ in repeat(None, num):
#         subs(a=a, b=b, c=c)

_callables = [
    concat,
    percent_s,
    frmt,
    join_and_make_tuple,
    join_with_existing_tuple,
    predef_join_make_tuple,
]

if version.startswith('3'):
    pass
    # def fstrings():
    #     a, b, c = _a, _b, _c
    #     for _ in repeat(None, num):
    #         f'{a}{b}{c}'
    #
    # _callables.append(fstrings)


tester(
    _callables
)


"""
Conclusion: 
    - In python3 fstrings
    
    - In python2 concat or .join
    
    Python27:
        Name                       Secs     %    
        frmt                       1.3864   100  
        percent_s                  0.6976   50   
        join_and_make_tuple        0.4476   32   
        join_with_existing_tuple   0.3808   27   
        concat                     0.3594   26   
        predef_join_make_tuple     0.35     25   
        
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


