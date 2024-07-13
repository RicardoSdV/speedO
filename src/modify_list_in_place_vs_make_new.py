"""
What is the fastest way of modifying a list in place?

"""

from src.z_data import data
from z_tester import tester_2d


def mod_list_in_place_with_range_len(outer):
    for inner in outer:
        for i in range(len(inner)):
            inner[i] += 1


def mod_list_in_place_with_enumerate(outer):
    for inner in outer:
        for i, el in enumerate(inner):
            inner[i] = el - 1


def mod_list_in_place_with_colon_enumerate(outer):
    for inner in outer:
        inner[:] = [el + 1 for i, el in enumerate(inner)]


def mod_list_in_place_with_with_colon_range_len(outer):
    for inner in outer:
        inner[:] = [inner[i] - 1 for i in range(len(inner))]


tester_2d(
    (
        mod_list_in_place_with_range_len,
        mod_list_in_place_with_enumerate,
        mod_list_in_place_with_colon_enumerate,
        mod_list_in_place_with_with_colon_range_len,
    ),
    list_3d=data.faster_3d_list
)


"""
Conclusion:
    Python27:
        - For some reason the window were colon enumerate is better is larger in python27 between 100 and 100k
        but for lists of 10 or 1 million a for loop is better, lol
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                                          Time     %    
        mod_list_in_place_with_with_colon_range_len   0.7597   100  
        mod_list_in_place_with_colon_enumerate        0.75     99   
        mod_list_in_place_with_range_len              0.417    55   
        mod_list_in_place_with_enumerate              0.4053   53   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                                          Time     %    
        mod_list_in_place_with_enumerate              0.3097   100  
        mod_list_in_place_with_range_len              0.306    99   
        mod_list_in_place_with_with_colon_range_len   0.2943   95   
        mod_list_in_place_with_colon_enumerate        0.2897   94   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                                          Time     %    
        mod_list_in_place_with_enumerate              0.307    100  
        mod_list_in_place_with_range_len              0.3057   100  
        mod_list_in_place_with_with_colon_range_len   0.2633   86   
        mod_list_in_place_with_colon_enumerate        0.252    82   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                                          Time     %    
        mod_list_in_place_with_range_len              0.3087   100  
        mod_list_in_place_with_enumerate              0.3003   97   
        mod_list_in_place_with_with_colon_range_len   0.2427   79   
        mod_list_in_place_with_colon_enumerate        0.233    75   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                                          Time     %    
        mod_list_in_place_with_range_len              0.3347   100  
        mod_list_in_place_with_enumerate              0.2873   86   
        mod_list_in_place_with_with_colon_range_len   0.2457   73   
        mod_list_in_place_with_colon_enumerate        0.23     69   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                                          Time     %    
        mod_list_in_place_with_with_colon_range_len   0.4387   100  
        mod_list_in_place_with_colon_enumerate        0.4013   91   
        mod_list_in_place_with_range_len              0.3377   77   
        mod_list_in_place_with_enumerate              0.2907   66   


    Python38:
        -Seems crazy but it seems that for short lists and long lists a for loop with either enumerate or range len
        is best but for 10k elements colon and list comprehension works better, wtf?
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                                          Time     %    
        mod_list_in_place_with_with_colon_range_len   0.4221   100  
        mod_list_in_place_with_colon_enumerate        0.3666   87   
        mod_list_in_place_with_range_len              0.3098   73   
        mod_list_in_place_with_enumerate              0.2921   69   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.2577   100  
        mod_list_in_place_with_with_colon_range_len   0.2562   99   
        mod_list_in_place_with_enumerate              0.2396   93   
        mod_list_in_place_with_range_len              0.2376   92   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                                          Time     %    
        mod_list_in_place_with_enumerate              0.2659   100  
        mod_list_in_place_with_colon_enumerate        0.2597   98   
        mod_list_in_place_with_range_len              0.2572   97   
        mod_list_in_place_with_with_colon_range_len   0.2474   93   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                                          Time     %    
        mod_list_in_place_with_enumerate              0.2758   100  
        mod_list_in_place_with_range_len              0.2656   96   
        mod_list_in_place_with_colon_enumerate        0.2543   92   
        mod_list_in_place_with_with_colon_range_len   0.237    86   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.2933   100  
        mod_list_in_place_with_enumerate              0.2785   95   
        mod_list_in_place_with_with_colon_range_len   0.2741   93   
        mod_list_in_place_with_range_len              0.2684   92   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.437    100  
        mod_list_in_place_with_with_colon_range_len   0.424    97   
        mod_list_in_place_with_enumerate              0.2785   64   
        mod_list_in_place_with_range_len              0.274    63   
    

    Python312:
        - Mainly using a for loop with enumerate is winning, but for some reason when the inner list is 10k
        mod_list_in_place_with_with_colon_range_len wins, which is wierd
    
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.3234   100  
        mod_list_in_place_with_with_colon_range_len   0.2897   90   
        mod_list_in_place_with_range_len              0.2752   85   
        mod_list_in_place_with_enumerate              0.2597   80   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.2505   100  
        mod_list_in_place_with_range_len              0.2312   92   
        mod_list_in_place_with_with_colon_range_len   0.2299   92   
        mod_list_in_place_with_enumerate              0.2073   83   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.2743   100  
        mod_list_in_place_with_range_len              0.2681   98   
        mod_list_in_place_with_with_colon_range_len   0.2477   90   
        mod_list_in_place_with_enumerate              0.2471   90   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
        Name                                          Time     %    
        mod_list_in_place_with_range_len              0.2814   100  
        mod_list_in_place_with_colon_enumerate        0.2656   94   
        mod_list_in_place_with_enumerate              0.2622   93   
        mod_list_in_place_with_with_colon_range_len   0.2382   85   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.2996   100  
        mod_list_in_place_with_range_len              0.2839   95   
        mod_list_in_place_with_with_colon_range_len   0.2787   93   
        mod_list_in_place_with_enumerate              0.2671   89   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
        Name                                          Time     %    
        mod_list_in_place_with_colon_enumerate        0.4314   100  
        mod_list_in_place_with_with_colon_range_len   0.398    92   
        mod_list_in_place_with_range_len              0.284    66   
        mod_list_in_place_with_enumerate              0.2631   61   

    

"""


