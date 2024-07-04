"""
Lets' say there is a list of tuples and to easily understand what the tuple represents it can contain one
of a number of flags, is there much difference between the different ways of holding such flag?
"""
from itertools import repeat

from src.z_data import data
from src.z_tester import tester



def normal_str():
    list_of_flags = ['someFlag' for _ in repeat(None, data.M10)]

def pre_declared_str():
    someFlag = 'someFlag'
    list_of_flags = [someFlag for _ in repeat(None, data.M10)]

def str_in_list():
    list_of_flags = [['someFlag'] for _ in repeat(None, data.M10)]

def pre_declared_list():
    some_list = ['someFlag']
    list_of_flags = [some_list for _ in repeat(None, data.M10)]

def pre_declared_tuple():
    some_list = ('someFlag',)
    list_of_flags = [some_list for _ in repeat(None, data.M10)]



if __name__ == '__main__':
    tester(
        (
            normal_str,
            str_in_list,
            pre_declared_str,
            pre_declared_list,
            pre_declared_tuple,
        ),
        testing_what='memories',
    )

    tester(
        (
            normal_str,
            str_in_list,
            pre_declared_str,
            pre_declared_list,
            pre_declared_tuple,
        ),
        testing_what='times',
    )


"""
Conclusion:

    All pretty much the same except creating new lists, and pypy
    in pypy tuples very cheap, and just better in general
    Python27:
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        str_in_list          828.0273   100  
        pre_declared_list    76.6367    9    
        normal_str           73.3711    9    
        pre_declared_tuple   71.207     9    
        pre_declared_str     69.8477    8    
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_in_list          1.8366   100  
        pre_declared_tuple   0.1742   9    
        pre_declared_str     0.1684   9    
        normal_str           0.1672   9    
        pre_declared_list    0.1662   9    
        
    Python38:
    
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        str_in_list          750.9102   100  
        pre_declared_tuple   87.3203    12   
        pre_declared_list    85.3906    11   
        pre_declared_str     84.8086    11   
        normal_str           76.9375    10   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_in_list          1.6837   100  
        normal_str           0.155    9    
        pre_declared_list    0.1536   9    
        pre_declared_str     0.1529   9    
        pre_declared_tuple   0.1506   9    
        
    Python312:
    
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        str_in_list          736.5312   100  
        pre_declared_list    84.5938    11   
        pre_declared_tuple   79.082     11   
        normal_str           76.3594    10   
        pre_declared_str     76.3555    10   
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_in_list          1.77     100  
        normal_str           0.1753   10   
        pre_declared_list    0.1673   9    
        pre_declared_tuple   0.1587   9    
        pre_declared_str     0.1556   9    
    
    Pypy313:
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        str_in_list          553.3867   100  
        pre_declared_str     76.3047    14   
        pre_declared_list    76.3047    14   
        normal_str           20.2852    4    
        pre_declared_tuple   6.1133     1    
        
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_in_list          0.9687   100  
        pre_declared_list    0.0778   8    
        pre_declared_str     0.0342   4    
        pre_declared_tuple   0.0326   3    
        normal_str           0.0319   3    

"""
















