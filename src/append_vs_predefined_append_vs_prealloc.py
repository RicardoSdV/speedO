"""
When you "need" to append what is the fastest way?
The fastest way is list comprehension but some people don't find this readable
and sometimes its a mess to have to define a bunch of generators and so on to
be able to have complex loops happen in list comprehension
"""
from src.z_data import data
from src.z_tester import tester_2d

def normal_append(list_2d):
    for inner_list in list_2d:
        result = []
        for i in inner_list:
            result.append(i+1)

def predef_append(list_2d):
    for inner_list in list_2d:
        result = []
        res_app = result.append
        for i in inner_list:
            res_app(i+1)

def prealloc_with_enumerate(list_2d):
    """ Enumerate makes sense because normally you wouldn't assign the index """
    for inner_list in list_2d:
        result = [None] * len(inner_list)
        for i, j in enumerate(inner_list):
            result[i] = j+1


# tester_2d_loops(
#     (
#         normal_append,
#         predef_append,
#         prealloc_with_enumerate,
#     ),
#     data.slower_3d_list,
#     testing_what='times'
# )

if __name__ == '__main__':
    tester_2d(
        (
            normal_append,
            predef_append,
            prealloc_with_enumerate,
        ),
        list_3d=data.slower_3d_list,
        testing_what='memories'
    )

"""
Times:
    Python 27:
        - Predefining the append is always way faster, however, if you have a list > 10M elements
        it might make sense to preallocate the elements and assign them        
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                      Secs     %    
        prealloc_with_enumerate   4.6177   100  
        normal_append             4.1143   89   
        predef_append             2.98     65   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                      Secs     %    
        normal_append             3.0057   100  
        prealloc_with_enumerate   2.5993   86   
        predef_append             1.9843   66   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                      Secs     %    
        normal_append             2.6103   100  
        prealloc_with_enumerate   2.5157   96   
        predef_append             1.641    63   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.5917   100  
        normal_append             2.4953   96   
        predef_append             1.5497   60   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.788    100  
        normal_append             2.5923   93   
        predef_append             1.6493   59   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                      Secs     %    
        normal_append             3.7063   100  
        prealloc_with_enumerate   2.84     77   
        predef_append             2.7027   73   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                      Secs     %    
        normal_append             3.8933   100  
        predef_append             2.8463   73   
        prealloc_with_enumerate   2.77     71  
        
        
    Python38:
        - As we know normal append becomes better in python3, but predefining it still 
        faster. Prealloc the list increases its range to > 1M
    
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.7171   100  
        normal_append             1.9343   71   
        predef_append             1.6108   59   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                      Secs     %    
        normal_append             1.9565   100  
        prealloc_with_enumerate   1.8598   95   
        predef_append             1.5211   78   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.0406   100  
        normal_append             1.8396   90   
        predef_append             1.4014   69   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.0926   100  
        normal_append             1.7548   84   
        predef_append             1.3306   64   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.2209   100  
        normal_append             1.7733   80   
        predef_append             1.3431   60   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                      Secs     %    
        normal_append             2.8619   100  
        predef_append             2.4246   85   
        prealloc_with_enumerate   2.3216   81   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                      Secs     %    
        normal_append             3.0191   100  
        predef_append             2.6024   86   
        prealloc_with_enumerate   2.3242   77   
        
    Python312:
        - Normal append wins now, prealloc still has it for > 1M
    
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.6595   100  
        predef_append             1.7736   67   
        normal_append             1.5955   60   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                      Secs     %    
        prealloc_with_enumerate   1.668    100  
        predef_append             1.6544   99   
        normal_append             1.5335   92   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   1.8971   100  
        predef_append             1.4731   78   
        normal_append             1.3825   73   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   1.9775   100  
        predef_append             1.4178   72   
        normal_append             1.2934   65   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   2.0442   100  
        predef_append             1.437    70   
        normal_append             1.3211   65   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                      Secs     %    
        predef_append             2.4071   100  
        normal_append             2.3037   96   
        prealloc_with_enumerate   2.1633   90   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                      Secs     %    
        predef_append             2.767    100  
        normal_append             2.6447   96   
        prealloc_with_enumerate   2.1653   78   
        
    PyPy313:
        - Normal append mostly wins too, prealloc > 10M
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name                      Secs     %    
        prealloc_with_enumerate   0.5777   100  
        normal_append             0.5513   95   
        predef_append             0.4516   78   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name                      Secs     %    
        prealloc_with_enumerate   0.4971   100  
        predef_append             0.3943   79   
        normal_append             0.3789   76   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   0.483    100  
        predef_append             0.4076   84   
        normal_append             0.3948   82   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name                      Secs     %    
        predef_append             1.0287   100  
        prealloc_with_enumerate   0.5998   57   
        normal_append             0.5172   50   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name                      Secs     %    
        prealloc_with_enumerate   1.7285   100  
        predef_append             0.857    50   
        normal_append             0.8525   49   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name                      Secs     %    
        predef_append             2.3437   100  
        prealloc_with_enumerate   1.5183   65   
        normal_append             1.3232   56   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name                      Secs     %    
        normal_append             1.9131   100  
        predef_append             1.7462   91   
        prealloc_with_enumerate   1.5259   80   
        
        
Memories:

"""