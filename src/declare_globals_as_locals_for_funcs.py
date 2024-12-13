from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M10

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
        a1, a2 = args_list
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
        do_comma_declare    0.2778   100  
        do_declare          0.2508   90   
        do_unpack_declare   0.1494   54   
        no_declare          0.1446   52   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_comma_declare    0.1935   100  
        do_declare          0.1883   97   
        do_unpack_declare   0.1151   59   
        no_declare          0.0988   51   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                Secs     %    
        do_declare          0.1889   100  
        do_comma_declare    0.1735   92   
        do_unpack_declare   0.1453   77   
        no_declare          0.1134   60   

"""