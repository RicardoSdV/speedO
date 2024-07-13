from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M100

def no_declare():

    args_list = [0, True]

    for _ in repeat(None, num):
        if args_list[0] and args_list[1]:
            continue


def do_comma_declare():

    args_list = [0, True]

    for _ in repeat(None, num):
        a1, a2 = args_list[0], args_list[1]
        if a1 and a2:
            continue

def do_unpack_declare():

    args_list = [0, True]

    for _ in repeat(None, num):
        a1, a2 = args_list, args_list
        if a1 and a2:
            continue


def do_declare():

    args_list = [0, True]

    for _ in repeat(None, num):
        a1 = args_list[0]
        a2 = args_list[1]
        if a1 and a2:
            continue


tester(
    (
        no_declare,
        do_comma_declare,
        do_declare,
        do_unpack_declare
    )
)

"""
Conclusion:
    Somehow declaring local names in got slower in python3

    Python27:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_comma_declare    2.536    100  
        do_declare          2.3236   92   
        do_unpack_declare   2.1572   85   
        no_declare          1.3516   53   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare          2.74     100  
        do_comma_declare    2.7226   99   
        do_unpack_declare   2.1679   79   
        no_declare          1.2844   47   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare          1.7861   100  
        do_comma_declare    1.6325   91   
        do_unpack_declare   1.4625   82   
        no_declare          1.0809   61  

"""