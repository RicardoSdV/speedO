"""
How much slower is it to use functions for conditions when there is a nested loop?
where the state of the outer loop dictates a condition in the inner loop.
"""

from z_tester import tester_2d_loops


def if_for_condition(outer_list):
    for j, inner_list in enumerate(outer_list):
        for i in inner_list:
            if i == j:
                continue


def lambda_for_condition(outer_list):
    for j, inner_list in enumerate(outer_list):
        condition = lambda x: x == j
        for i in inner_list:
            if condition(i):
                continue


def function_for_condition(outer_list):
    for j, inner_list in enumerate(outer_list):
        def condition(x): return x == j
        for i in inner_list:
            if condition(i):
                continue


tester_2d_loops(
    (
        if_for_condition,
        lambda_for_condition,
        function_for_condition,
    )
)


""" 
Conclusion:
    - Surprisingly python27 ifs almost as good if not better than python312

    Python312:
        - Ifs more than twice as good

        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                     Time     %    
        function_for_condition   3.1837   100  
        lambda_for_condition     3.1808   100  
        if_for_condition         1.294    41   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                     Time     %    
        function_for_condition   2.4699   100  
        lambda_for_condition     2.4601   100  
        if_for_condition         0.9641   39   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                     Time     %    
        function_for_condition   2.3925   100  
        lambda_for_condition     2.3903   100  
        if_for_condition         0.9314   39   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                     Time     %    
        function_for_condition   2.3986   100  
        lambda_for_condition     2.3847   99   
        if_for_condition         0.9396   39   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                     Time     %    
        function_for_condition   2.409    100  
        lambda_for_condition     2.4049   100  
        if_for_condition         0.9553   40   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                     Time     %    
        function_for_condition   2.4193   100  
        lambda_for_condition     2.4126   100  
        if_for_condition         1.0006   41   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                     Time     %    
        function_for_condition   2.4208   100  
        lambda_for_condition     2.4158   100  
        if_for_condition         0.9963   41   
        
        
    Python38:
        - Ifs more than three times as good
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                     Time     %    
        lambda_for_condition     3.6975   100  
        function_for_condition   3.6834   100  
        if_for_condition         1.0516   28   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                     Time     %    
        function_for_condition   3.0359   100  
        lambda_for_condition     3.0315   100  
        if_for_condition         0.8516   28   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                     Time     %    
        lambda_for_condition     3.0006   100  
        function_for_condition   2.9951   100  
        if_for_condition         0.8196   27   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                     Time     %    
        lambda_for_condition     2.9994   100  
        function_for_condition   2.9864   100  
        if_for_condition         0.8174   27   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                     Time     %    
        function_for_condition   2.9955   100  
        lambda_for_condition     2.9955   100  
        if_for_condition         0.826    28   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                     Time     %    
        lambda_for_condition     3.038    100  
        function_for_condition   3.0329   100  
        if_for_condition         0.8423   28   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                     Time     %    
        function_for_condition   3.0069   100  
        lambda_for_condition     3.0015   100  
        if_for_condition         0.8343   28   
        
        
    Python27:
        - Ifs four times faster
    
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                     Time     %    
        lambda_for_condition     4.542    100  
        function_for_condition   4.5207   100  
        if_for_condition         1.157    25   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                     Time     %    
        function_for_condition   3.668    100  
        lambda_for_condition     3.6583   100  
        if_for_condition         0.8347   23   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                     Time     %    
        function_for_condition   3.5873   100  
        lambda_for_condition     3.5627   99   
        if_for_condition         0.765    21   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                     Time     %    
        lambda_for_condition     3.53     100  
        function_for_condition   3.5237   100  
        if_for_condition         0.762    22   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                     Time     %    
        lambda_for_condition     3.468    100  
        function_for_condition   3.4583   100  
        if_for_condition         0.7617   22   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                     Time     %    
        lambda_for_condition     3.5137   100  
        function_for_condition   3.5113   100  
        if_for_condition         0.7757   22   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                     Time     %    
        lambda_for_condition     3.5213   100  
        function_for_condition   3.501    99   
        if_for_condition         0.782    22   
    
"""
