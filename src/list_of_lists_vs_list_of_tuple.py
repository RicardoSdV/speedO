"""
How much slower is it to create a list of tuples than a list of lists?
How much memory do I save by creating a list of tuples?
The point is to use in STAK this is why all the appending
"""

from itertools import repeat

from src.z_data import data
from src.z_tester import tester

k100 = data.k100
k = data.k
hun_chars = data.hun_chars_str


def list_of_lists():
    outer_res = []
    for _ in repeat(None, k100):
        inner_res = []
        for _ in repeat(None, k):
            inner_res.append(hun_chars)
        outer_res.append(inner_res)
    return outer_res


def comprehend_list_of_lists():
    return [[hun_chars for _ in repeat(None, k)] for _ in repeat(None, k100)]


def list_of_tuples():
    outer_res = []
    for _ in repeat(None, k100):
        inner_res = []
        for _ in repeat(None, k):
            inner_res.append(hun_chars)
        outer_res.append(tuple(inner_res))
    return outer_res


def comprehend_list_of_tuples():
    return [tuple(hun_chars for _ in repeat(None, k)) for _ in repeat(None, k100)]

def comprehend_list_of_tuples2():
    return [tuple([hun_chars for _ in repeat(None, k)]) for _ in repeat(None, k100)]

def comprehend_list_of_tuples3():
    return [tuple((hun_chars for _ in repeat(None, k))) for _ in repeat(None, k100)]


if __name__ == '__main__':

    tester(
        (
            list_of_lists,
            list_of_tuples,
            comprehend_list_of_lists,
            comprehend_list_of_tuples,
            comprehend_list_of_tuples2,
            comprehend_list_of_tuples3,
        ),
        testing_what='memories'
    )

    tester(
        (
            list_of_lists,
            list_of_tuples,
            comprehend_list_of_lists,
            comprehend_list_of_tuples,
            comprehend_list_of_tuples3,
        ),
        testing_what='times'
    )


"""
Conclusion:
    - In interpreted python, the memory saved by using tuples is not great but not bad, but surprisingly, the speed loss
    is even less significant, so, tuples is worth it.
    
    - Pypy is wierd, or maybe interpreted python is wierd, but they dont correlate too well
    
    - List comprehension is great and should be used, and generally the best way to get a tuple is to make a 
    list and turn to tuple rather than tuple comprehension


    Python27:
        - Max speed probably list comprehension then turn to tuple
        - Min memory probably straight up tuple comprehension
    
        Testing memories average of 5 rounds: 
        Name                         Mibs       %    
        list_of_lists                674.3359   100  
        comprehend_list_of_lists     643.3555   95   
        list_of_tuples               549.3477   81   
        comprehend_list_of_tuples    523.1758   78   
        comprehend_list_of_tuples2   505.418    75   
        comprehend_list_of_tuples3   490.2852   73   
        
        Testing times average of 5 rounds: 
        Name                         Secs     %    
        list_of_lists                3.7578   100  
        list_of_tuples               3.4926   93   
        comprehend_list_of_tuples    2.4676   66   
        comprehend_list_of_lists     2.0092   53   
        comprehend_list_of_tuples2   1.8052   48  
        
    Python38:
        - Min memory tuple comprehension & list comprehension then turn to tuple tied
        - Max speed list comprehension then turn to tuple
    
        Testing memories average of 5 rounds: 
        Name                         Mibs       %    
        list_of_lists                868.3984   100  
        comprehend_list_of_lists     856.8352   99   
        list_of_tuples               761.1195   88   
        comprehend_list_of_tuples2   757.5781   87   
        comprehend_list_of_tuples    757.3797   87   
        
        Testing times average of 5 rounds: 
        Name                         Secs     %    
        list_of_lists                3.4827   100  
        list_of_tuples               3.1305   90   
        comprehend_list_of_tuples    2.2946   66   
        comprehend_list_of_lists     1.6124   46   
        comprehend_list_of_tuples2   1.5644   45   
        
    Python312:
        - Min memory tuple comprehension
        - Max speed list comprehension tied with list comprehension then turn to tuple
    
        Testing memories average of 5 rounds: 
        Name                         Mibs       %    
        list_of_lists                899.2914   100  
        comprehend_list_of_lists     863.025    96   
        list_of_tuples               761.8375   85   
        comprehend_list_of_tuples2   755.457    84   
        comprehend_list_of_tuples    727.6047   81   

        Testing times average of 5 rounds: 
        Name                         Secs     %    
        comprehend_list_of_tuples    2.3952   100  
        list_of_tuples               1.771    74   
        list_of_lists                1.7704   74   
        comprehend_list_of_lists     1.4453   60   
        comprehend_list_of_tuples2   1.4438   60   
        
    Pypy313:
        - Min memory list comprehension then turn to tuple
        - Max speed list comprehension
        
        Testing memories average of 5 rounds: 
        Name                         Mibs       %    
        list_of_tuples               753.1391   100  
        list_of_lists                703.3703   93   
        comprehend_list_of_tuples    682.1398   91   
        comprehend_list_of_lists     614.2352   82   
        comprehend_list_of_tuples2   584.1164   78   
        
        Testing times average of 5 rounds: 
        Name                         Secs     %    
        comprehend_list_of_tuples    1.2476   100  
        list_of_lists                1.1518   92   
        comprehend_list_of_tuples2   1.1258   90   
        list_of_tuples               1.1239   90   
        comprehend_list_of_lists     0.8855   71   
"""
