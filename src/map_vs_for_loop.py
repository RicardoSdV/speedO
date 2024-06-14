"""
What is faster, map? or list comprehension?

map() makes list in python27, in python3 makes map object which is like gen
"""
from sys import version

from src.z_data import data
from z_tester import tester_2d_loops

if version.startswith('2'):
    def map_with_lambda(outer_list):
        for inner_list in outer_list:
            res = map(lambda n: n + 1, inner_list)

    def pre_defined_func(n): return n + 1

    def map_with_pre_defined_func(outer_list):
        for inner_list in outer_list:
            res = map(pre_defined_func, inner_list)

    def list_comprehension(outer_list):
        for inner_list in outer_list:
            res = [n + 1 for n in inner_list]

    def list_comprehension_with_func(outer_list):
        for inner_list in outer_list:
            res = [pre_defined_func(n) for n in inner_list]


    tester_2d_loops(
        (
            map_with_lambda,
            map_with_pre_defined_func,
            list_comprehension,
            list_comprehension_with_func,
        ),
        list_3d=data.faster_3d_list
    )

else:

    def map_with_lambda(outer_list):
        for inner_list in outer_list:
            res = map(lambda n: n + 1, inner_list)
            for el in res:
                continue

    def pre_defined_func(n):
        return n + 1


    def map_with_pre_defined_func(outer_list):
        for inner_list in outer_list:
            res = map(pre_defined_func, inner_list)
            for el in res:
                continue


    def generator_comprehension(outer_list):
        for inner_list in outer_list:
            res = (n + 1 for n in inner_list)
            for el in res:
                continue

    def generator_comprehension_with_func(outer_list):
        for inner_list in outer_list:
            res = (pre_defined_func(n) for n in inner_list)
            for el in res:
                continue


    tester_2d_loops(
        (
            map_with_lambda,
            map_with_pre_defined_func,
            generator_comprehension,
            generator_comprehension_with_func,
        ),
        list_3d=data.faster_3d_list
    )


"""
Conclusion: 

    Python27:
        - List comprehension is normally faster unless you need to do the manipulation of the elements in a func
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                           Time     %    
        list_comprehension_with_func   0.8003   100  
        map_with_lambda                0.5433   68   
        map_with_pre_defined_func      0.52     65   
        list_comprehension             0.5057   63   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                           Time     %    
        list_comprehension_with_func   0.5157   100  
        map_with_pre_defined_func      0.3813   74   
        map_with_lambda                0.3803   74   
        list_comprehension             0.263    51   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                           Time     %    
        list_comprehension_with_func   0.4057   100  
        map_with_lambda                0.364    90   
        map_with_pre_defined_func      0.3637   90   
        list_comprehension             0.167    41   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                           Time     %    
        list_comprehension_with_func   0.365    100  
        map_with_lambda                0.359    98   
        map_with_pre_defined_func      0.358    98   
        list_comprehension             0.1387   38   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                           Time     %    
        map_with_pre_defined_func      0.395    100  
        map_with_lambda                0.3947   100  
        list_comprehension_with_func   0.3533   89   
        list_comprehension             0.1323   34   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                           Time     %    
        list_comprehension_with_func   0.472    100  
        map_with_lambda                0.3883   82   
        map_with_pre_defined_func      0.3843   81   
        list_comprehension             0.247    52   
    
    
    Python38:
        - Same, use generator, when need to manipulate with func use map
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4909   100  
        map_with_lambda                     0.3783   77   
        map_with_pre_defined_func           0.3273   67   
        generator_comprehension             0.3069   63   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4083   100  
        map_with_lambda                     0.2881   71   
        map_with_pre_defined_func           0.2586   63   
        generator_comprehension             0.2197   54   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4245   100  
        map_with_lambda                     0.3029   71   
        map_with_pre_defined_func           0.2747   65   
        generator_comprehension             0.2324   55   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4274   100  
        map_with_lambda                     0.3067   72   
        map_with_pre_defined_func           0.2798   65   
        generator_comprehension             0.2376   56   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.431    100  
        map_with_lambda                     0.3096   72   
        map_with_pre_defined_func           0.2802   65   
        generator_comprehension             0.2366   55   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4277   100  
        map_with_lambda                     0.3131   73   
        map_with_pre_defined_func           0.2837   66   
        generator_comprehension             0.2387   56   
        
        
    Python312:
        - Same as before
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                                Time     %    
        generator_comprehension_with_func   0.4051   100  
        map_with_lambda                     0.3554   88   
        map_with_pre_defined_func           0.3347   83   
        generator_comprehension             0.2801   69   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                                Time     %    
        generator_comprehension_with_func   0.2996   100  
        map_with_lambda                     0.2769   92   
        map_with_pre_defined_func           0.2742   92   
        generator_comprehension             0.175    57   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.3196   100  
        map_with_lambda                     0.3059   96   
        map_with_pre_defined_func           0.3044   95   
        generator_comprehension             0.191    60   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.3291   100  
        map_with_lambda                     0.3178   97   
        map_with_pre_defined_func           0.3162   96   
        generator_comprehension             0.1986   60   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.33     100  
        map_with_pre_defined_func           0.3158   96   
        map_with_lambda                     0.3157   96   
        generator_comprehension             0.1989   60   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                                Time     %    
        generator_comprehension_with_func   0.3364   100  
        map_with_pre_defined_func           0.3227   96   
        map_with_lambda                     0.3226   96   
        generator_comprehension             0.201    60   
"""
