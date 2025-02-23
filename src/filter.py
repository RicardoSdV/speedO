from itertools import repeat
# from itertools import ifilter

from src.z_data import data
from src.z_tester import auto_tester


reps = data.k100

def _is_one(n): return n == 1

def filter_k_small(filterFunc=_is_one, nums=data.hun_ints, f=filter):
    for _ in repeat(None, reps//10):
        list(f(filterFunc, nums))  # take out the list if 27

# def ifilter_k_small(filterFunc=_is_one, nums=data.hun_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps//10):
#         l(iF(filterFunc, nums))

def comprehend_with_func_k_small(filterFunc=_is_one, nums=data.hun_ints):
    for _ in repeat(None, reps//10):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_k_small(filterFunc=_is_one, nums=data.hun_ints):
    for _ in repeat(None, reps//10):
        [num for num in nums if num == 1]


def filter_hun_small(filterFunc=_is_one, nums=data.hun_ints, f=filter):
    for _ in repeat(None, reps):
        list(f(filterFunc, nums))  # take out the list if 27

# def ifilter_hun_small(filterFunc=_is_one, nums=data.hun_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps):
#         l(iF(filterFunc, nums))

def comprehend_with_func_hun_small(filterFunc=_is_one, nums=data.hun_ints):
    for _ in repeat(None, reps):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_hun_small(filterFunc=_is_one, nums=data.hun_ints):
    for _ in repeat(None, reps):
        [num for num in nums if num == 1]


def filter_ten_small(filterFunc=_is_one, nums=data.ten_ints, f=filter):
    for _ in repeat(None, reps*10):
        list(f(filterFunc, nums))  # take out the list if 27

# def ifilter_ten_small(filterFunc=_is_one, nums=data.ten_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps*10):
#         l(iF(filterFunc, nums))

def comprehend_with_func_ten_small(filterFunc=_is_one, nums=data.ten_ints):
    for _ in repeat(None, reps*10):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_ten_small(filterFunc=_is_one, nums=data.ten_ints):
    for _ in repeat(None, reps*10):
        [num for num in nums if num == 1]


def _not_one(n): return n != 1

def filter_k_big(filterFunc=_not_one, nums=data.k_ints, f=filter):
    for _ in repeat(None, reps//10):
        list(f(filterFunc, nums))  # take out the list if 27

# def ifilter_k_big(filterFunc=_not_one, nums=data.k_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps//10):
#         l(iF(filterFunc, nums))

def comprehend_with_func_k_big(filterFunc=_not_one, nums=data.k_ints):
    for _ in repeat(None, reps//10):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_k_big(filterFunc=_not_one, nums=data.k_ints):
    for _ in repeat(None, reps//10):
        [num for num in nums if num != 1]


def filter_hun_big(filterFunc=_not_one, nums=data.hun_ints, f=filter):
    for _ in repeat(None, reps):
        list(f(filterFunc, nums))  # take out the list if 27

# def ifilter_hun_big(filterFunc=_not_one, nums=data.hun_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps):
#         l(iF(filterFunc, nums))

def comprehend_with_func_hun_big(filterFunc=_not_one, nums=data.hun_ints):
    for _ in repeat(None, reps):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_hun_big(filterFunc=_not_one, nums=data.hun_ints):
    for _ in repeat(None, reps):
        [num for num in nums if num != 1]


def filter_ten_big(filterFunc=_not_one, nums=data.ten_ints, f=filter):
    for _ in repeat(None, reps*10):
        list(f(filterFunc, nums))  # take out the list if 27

# Only 27
# def ifilter_ten_big(filterFunc=_not_one, nums=data.ten_ints, iF=ifilter, l=list):
#     for _ in repeat(None, reps*10):
#         l(iF(filterFunc, nums))

def comprehend_with_func_ten_big(filterFunc=_not_one, nums=data.ten_ints):
    for _ in repeat(None, reps*10):
        [num for num in nums if filterFunc(num)]

def comprehend_direct_ten_big(filterFunc=_not_one, nums=data.ten_ints):
    for _ in repeat(None, reps*10):
        [num for num in nums if num != 1]


auto_tester(segregator='end', seg_parts=2)

"""
Conclusion:
    Python27:
        Name                           Secs     %    
        ifilter_hun_big                0.4716   100  
        comprehend_with_func_hun_big   0.4258   90   
        filter_hun_big                 0.3126   66   
        comprehend_direct_hun_big      0.182    39   
        
        Name                             Secs     %    
        ifilter_hun_small                0.3732   100  
        filter_hun_small                 0.3154   85   
        comprehend_with_func_hun_small   0.3122   84   
        comprehend_direct_hun_small      0.0908   24   
        
        Name                         Secs     %    
        ifilter_k_big                0.403    100  
        comprehend_with_func_k_big   0.3816   95   
        filter_k_big                 0.2936   73   
        comprehend_direct_k_big      0.1494   37   
        
        Name                           Secs     %    
        ifilter_k_small                0.0378   100  
        comprehend_with_func_k_small   0.031    82   
        filter_k_small                 0.0308   81   
        comprehend_direct_k_small      0.0092   24   
        
        Name                           Secs     %    
        ifilter_ten_big                0.6958   100  
        comprehend_with_func_ten_big   0.5466   79   
        filter_ten_big                 0.4298   62   
        comprehend_direct_ten_big      0.2492   36   
        
        Name                             Secs     %    
        ifilter_ten_small                0.7128   100  
        filter_ten_small                 0.5002   70   
        comprehend_with_func_ten_small   0.4036   56   
        comprehend_direct_ten_small      0.1388   19   
        
    Python38:
        Name                           Secs     %    
        comprehend_with_func_hun_big   0.3522   100  
        filter_hun_big                 0.2948   84   
        comprehend_direct_hun_big      0.157    45   
        
        Name                             Secs     %    
        comprehend_with_func_hun_small   0.2843   100  
        filter_hun_small                 0.2404   85   
        comprehend_direct_hun_small      0.0936   33   
        
        Name                         Secs     %    
        comprehend_with_func_k_big   0.3317   100  
        filter_k_big                 0.2642   80   
        comprehend_direct_k_big      0.1435   43   
        
        Name                           Secs     %    
        comprehend_with_func_k_small   0.0286   100  
        filter_k_small                 0.0242   85   
        comprehend_direct_k_small      0.0091   32   
        
        Name                           Secs     %    
        comprehend_with_func_ten_big   0.4074   100  
        filter_ten_big                 0.3534   87   
        comprehend_direct_ten_big      0.1988   49   
        
        Name                             Secs     %    
        comprehend_with_func_ten_small   0.3694   100  
        filter_ten_small                 0.3488   94   
        comprehend_direct_ten_small      0.1593   43   
        
    Python310:
    
        

"""

