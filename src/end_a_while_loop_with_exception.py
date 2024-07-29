""" At some point it becomes worth it to end a while loop with an exception, when?
Or, maybe like everything in Python, it's better with iterators?

PROBLEM: There's a problem with this test which is that the exception in the blocks in
never raised, also, the len never changes, must be rewritten with varying numbers of
elements deleted from the list

"""
from src.z_data import data
from src.z_tester import tester_2d

# Somtimes you need a dynamic len bc the size of whatever you're
# iterating over is changing in length, the main reason to use
# a while loop rather than a for loop. Of course if the changes in
# size don't happen often its probably still worth it to precompute
# the len and -= from it on change, but yeah ...
def end_with_condition_dynamic_len(outer):
    for inner in outer:
        i = 0
        while i < len(inner):
            el = inner[i]
            i += 1

def end_with_condition_pre_comp_len(outer):
    for inner in outer:
        len_inner, i = len(inner), 0
        while i < len_inner:
            el = inner[i]
            i += 1

def end_with_try_except(outer):
    for inner in outer:
        try:
            i = 0
            while True:
                el = inner[i]
                i += 1
        except:
            pass

# maybe not all exceptions inside a while loop should be handled
# as an end of iteration event, so should be more specifically handled
def end_with_specific_try_except(outer):
    for inner in outer:
        try:
            i = 0
            while True:
                el = inner[i]
                i += 1
        except IndexError:
            pass

# You should probably declare your own generator for using filter()
# involves passing it a function and calling that function repeatedly
# probably mitigates the performance gains of the generator
def generator(_list):
    for el in _list:
        yield el

def use_generator(outer):
    for inner in outer:
        inner[:] = generator(inner)



tester_2d(
    (
        end_with_condition_dynamic_len,
        end_with_condition_pre_comp_len,
        end_with_try_except,
        end_with_specific_try_except,
        use_generator,
    ),
    list_3d=data.slower_3d_list,
)

"""
Conclusion:
    - The only general conclusion is that specific exceptions are as expensive to catch as
    generic ones so might as well catch specific

    Python27:
        - When len changes a small minority of times:
            - For lists < 100 elements, precomputed length is the way to go
            - For 100 < lists < 1 000 000 elements, a generator is better
            - For lists >= 1 000 000 elements pre computed length
            
        - When len changes often
            - For lists < 10 dynamic length
            - For 100 < lists < 100 000 generator
            - For lists > 100 000 try except block
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                              Secs     %    
        end_with_specific_try_except      5.31     100  
        end_with_try_except               4.8327   91   
        use_generator                     4.8083   91   
        end_with_condition_dynamic_len    3.882    73   
        end_with_condition_pre_comp_len   2.7303   51   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.5463   100  
        end_with_specific_try_except      2.9913   84   
        end_with_try_except               2.9543   83   
        use_generator                     2.5893   73   
        end_with_condition_pre_comp_len   2.319    65   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.8453   100  
        end_with_specific_try_except      2.8093   73   
        end_with_try_except               2.7607   72   
        end_with_condition_pre_comp_len   2.4273   63   
        use_generator                     1.9713   51   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.9713   100  
        end_with_specific_try_except      2.7417   69   
        end_with_try_except               2.7223   69   
        end_with_condition_pre_comp_len   2.4703   62   
        use_generator                     1.8227   46   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.8897   100  
        end_with_specific_try_except      2.629    68   
        end_with_try_except               2.6177   67   
        end_with_condition_pre_comp_len   2.453    63   
        use_generator                     1.8873   49   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.884    100  
        use_generator                     3.164    81   
        end_with_specific_try_except      2.6117   67   
        end_with_try_except               2.6003   67   
        end_with_condition_pre_comp_len   2.453    63   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                              Secs     %    
        use_generator                     4.0337   100  
        end_with_condition_dynamic_len    3.9013   97   
        end_with_specific_try_except      3.21     80   
        end_with_try_except               3.2083   80   
        end_with_condition_pre_comp_len   2.532    63   
    
    Python3x:
        try except block 
    
    Python38:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.2515   100  
        use_generator                     2.8401   87   
        end_with_condition_pre_comp_len   2.4759   76   
        end_with_specific_try_except      2.3808   73   
        end_with_try_except               2.2261   68   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    2.9557   100  
        end_with_condition_pre_comp_len   2.1156   72   
        use_generator                     2.0712   70   
        end_with_specific_try_except      1.5499   52   
        end_with_try_except               1.5426   52   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.6053   100  
        end_with_condition_pre_comp_len   2.3005   64   
        use_generator                     1.8051   50   
        end_with_specific_try_except      1.7026   47   
        end_with_try_except               1.7011   47   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.6669   100  
        end_with_condition_pre_comp_len   2.3549   64   
        use_generator                     1.7811   49   
        end_with_specific_try_except      1.7779   48   
        end_with_try_except               1.7635   48   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.6036   100  
        end_with_condition_pre_comp_len   2.3228   64   
        use_generator                     1.8676   52   
        end_with_try_except               1.7339   48   
        end_with_specific_try_except      1.732    48   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.5955   100  
        use_generator                     3.148    88   
        end_with_condition_pre_comp_len   2.3229   65   
        end_with_try_except               1.7379   48   
        end_with_specific_try_except      1.7347   48   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.6008   100  
        use_generator                     3.5792   99   
        end_with_condition_pre_comp_len   2.3305   65   
        end_with_specific_try_except      1.733    48   
        end_with_try_except               1.7206   48   
        
    Python310:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    4.2645   100  
        use_generator                     3.1453   74   
        end_with_condition_pre_comp_len   3.071    72   
        end_with_specific_try_except      2.7998   66   
        end_with_try_except               2.6129   61   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    3.9401   100  
        use_generator                     3.0228   77   
        end_with_condition_pre_comp_len   2.6053   66   
        end_with_try_except               1.9179   49   
        end_with_specific_try_except      1.9143   49   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    4.6497   100  
        end_with_condition_pre_comp_len   2.8271   61   
        use_generator                     2.2343   48   
        end_with_try_except               2.1218   46   
        end_with_specific_try_except      2.1131   45   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    4.7939   100  
        end_with_condition_pre_comp_len   2.9631   62   
        end_with_specific_try_except      2.2018   46   
        end_with_try_except               2.1994   46   
        use_generator                     1.9841   41   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    4.7672   100  
        end_with_condition_pre_comp_len   2.9648   62   
        end_with_try_except               2.1665   45   
        end_with_specific_try_except      2.1665   45   
        use_generator                     2.0659   43   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    7.2888   100  
        use_generator                     5.335    73   
        end_with_condition_pre_comp_len   4.4976   62   
        end_with_try_except               3.3155   45   
        end_with_specific_try_except      2.8256   39   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    5.0669   100  
        use_generator                     4.0415   80   
        end_with_condition_pre_comp_len   3.1433   62   
        end_with_try_except               2.2706   45   
        end_with_specific_try_except      2.2687   45   
        
    Python312:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                              Secs     %    
        use_generator                     3.7939   100  
        end_with_specific_try_except      2.6482   70   
        end_with_condition_dynamic_len    2.5793   68   
        end_with_try_except               2.5673   68   
        end_with_condition_pre_comp_len   2.4851   66   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                              Secs     %    
        use_generator                     4.6914   100  
        end_with_condition_dynamic_len    4.1257   88   
        end_with_condition_pre_comp_len   3.082    66   
        end_with_specific_try_except      2.1914   47   
        end_with_try_except               2.1739   46   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    5.8038   100  
        use_generator                     3.7889   65   
        end_with_condition_pre_comp_len   3.6874   64   
        end_with_specific_try_except      2.7661   48   
        end_with_try_except               2.7615   48   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    6.0168   100  
        end_with_condition_pre_comp_len   3.8832   65   
        use_generator                     3.5128   57   
        end_with_specific_try_except      2.9794   50   
        end_with_try_except               2.9762   49   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                              Secs     %    
        end_with_condition_dynamic_len    6.0589   100  
        end_with_condition_pre_comp_len   3.9187   65   
        use_generator                     3.5412   57   
        end_with_specific_try_except      3.003    50   
        end_with_try_except               3.0019   50   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                              Secs     %    
        use_generator                     6.274    100  
        end_with_condition_dynamic_len    6.0528   96   
        end_with_condition_pre_comp_len   3.9092   62   
        end_with_specific_try_except      2.9933   48   
        end_with_try_except               2.9921   48   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                              Secs     %    
        use_generator                     6.9361   100  
        end_with_condition_dynamic_len    6.0664   87   
        end_with_condition_pre_comp_len   3.9159   56   
        end_with_specific_try_except      2.9954   43   
        end_with_try_except               2.9924   43   
    
    PyPy313:
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                              Secs     %    
        use_generator                     2.03     100  
        end_with_condition_pre_comp_len   0.3001   15   
        end_with_condition_dynamic_len    0.2939   14   
        end_with_try_except               0.2679   13   
        end_with_specific_try_except      0.2592   13   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                              Secs     %    
        use_generator                     1.5605   100  
        end_with_try_except               0.54     35   
        end_with_specific_try_except      0.5362   34   
        end_with_condition_dynamic_len    0.4803   31   
        end_with_condition_pre_comp_len   0.4781   31   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                              Secs     %    
        use_generator                     1.5507   100  
        end_with_condition_dynamic_len    0.5243   34   
        end_with_condition_pre_comp_len   0.5102   33   
        end_with_try_except               0.4698   30   
        end_with_specific_try_except      0.4685   30   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                              Secs     %    
        use_generator                     2.9485   100  
        end_with_condition_dynamic_len    0.516    18   
        end_with_condition_pre_comp_len   0.5003   17   
        end_with_try_except               0.4607   16   
        end_with_specific_try_except      0.4586   16   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                              Secs     %    
        use_generator                     8.074    100  
        end_with_condition_dynamic_len    0.516    6    
        end_with_condition_pre_comp_len   0.5036   6    
        end_with_specific_try_except      0.4611   6    
        end_with_try_except               0.4594   6    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                              Secs     %    
        use_generator                     8.2351   100  
        end_with_condition_dynamic_len    0.5297   6    
        end_with_condition_pre_comp_len   0.505    6    
        end_with_try_except               0.4637   6    
        end_with_specific_try_except      0.4613   6    
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                              Secs     %    
        use_generator                     8.3672   100  
        end_with_condition_dynamic_len    1.045    12   
        end_with_condition_pre_comp_len   0.511    6    
        end_with_try_except               0.4603   6    
        end_with_specific_try_except      0.459    5    

"""


