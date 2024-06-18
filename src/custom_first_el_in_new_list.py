"""
When you cant use normal list comprehension because the list needs to start with a
custom first element what is the best way?? Also, the idea is that the list needs
to be created anew, this is why this test makes sense.
"""
from src.z_data import data
from z_tester import tester_2d_loops


def using_append(list_2d):
    for inner_list in list_2d:
        new_list = [-1]
        for i in inner_list:
            new_list.append(i)


def using_concat(list_2d):
    for inner_list in list_2d:
        new_list = [-1] + [i for i in inner_list]


def using_extend(list_2d):
    for inner_list in list_2d:
        new_list = [-1].extend([i for i in inner_list])


def using_insert(list_2d):
    for inner_list in list_2d:
        new_list = [i for i in inner_list]
        new_list.insert(0, -1)


tester_2d_loops(
    (
        using_append,
        using_concat,
        using_extend,
        using_insert,
    ),
    data.slower_3d_list
)

"""
Conclusion:
    - Append is massively slow in python27 and way better in the newer versions
    - Also, just use insert.

    Python27:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name           Time     %    
        using_append   4.406    100  
        using_extend   2.9937   68   
        using_insert   2.8107   64   
        using_concat   2.7933   63   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name           Time     %    
        using_append   3.03     100  
        using_extend   2.3553   78   
        using_concat   2.3103   76   
        using_insert   1.4307   47   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name           Time     %    
        using_append   2.5733   100  
        using_concat   1.266    49   
        using_extend   1.266    49   
        using_insert   1.166    45   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name           Time     %    
        using_append   2.379    100  
        using_concat   0.9957   42   
        using_extend   0.9813   41   
        using_insert   0.873    37   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name           Time     %    
        using_append   2.3073   100  
        using_concat   1.171    51   
        using_extend   1.0023   43   
        using_insert   0.8423   37   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name           Time     %    
        using_append   3.4823   100  
        using_concat   2.3107   66   
        using_extend   2.2927   66   
        using_insert   2.004    57   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name           Time    %    
        using_append   3.528   100  
        using_concat   2.428   69   
        using_extend   2.402   68   
        using_insert   2.046   57   

    
    Python38:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name           Time     %    
        using_append   1.9813   100  
        using_concat   1.6856   85   
        using_extend   1.6743   85   
        using_insert   1.4887   75   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name           Time     %    
        using_append   1.9213   100  
        using_extend   0.9597   50   
        using_concat   0.936    49   
        using_insert   0.8543   44   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name           Time     %    
        using_append   1.7689   100  
        using_concat   0.881    50   
        using_extend   0.8762   50   
        using_insert   0.8017   45   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name           Time     %    
        using_append   1.6276   100  
        using_concat   0.7503   46   
        using_extend   0.7469   46   
        using_insert   0.6605   41   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name           Time     %    
        using_append   1.6378   100  
        using_concat   0.9998   61   
        using_extend   0.8689   53   
        using_insert   0.7036   43   

        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name           Time     %    
        using_append   2.8344   100  
        using_concat   2.2175   78   
        using_extend   2.2035   78   
        using_insert   1.8771   66   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name           Time     %    
        using_append   2.9148   100  
        using_extend   2.3386   80   
        using_concat   2.3271   80   
        using_insert   1.8988   65   

        
    Python312:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name           Time     %    
        using_append   1.6034   100  
        using_extend   1.3732   86   
        using_concat   1.3698   85   
        using_insert   1.1667   73   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name           Time     %    
        using_append   1.4578   100  
        using_concat   0.9685   66   
        using_extend   0.9159   63   
        using_insert   0.8621   59   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name           Time     %    
        using_append   1.2519   100  
        using_concat   0.9163   73   
        using_extend   0.9142   73   
        using_insert   0.8471   68   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name           Time     %    
        using_append   1.1126   100  
        using_concat   0.8287   74   
        using_extend   0.8205   74   
        using_insert   0.7275   65   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name           Time     %    
        using_append   1.0819   100  
        using_concat   0.9517   88   
        using_extend   0.8817   82   
        using_insert   0.7003   65   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name           Time     %    
        using_append   2.2711   100  
        using_concat   2.2387   99   
        using_extend   2.2317   98   
        using_insert   1.8716   82   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name           Time     %    
        using_extend   2.4386   100  
        using_concat   2.4359   100  
        using_append   2.3937   98   
        using_insert   2.0613   85   
"""