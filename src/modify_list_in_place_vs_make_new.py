"""
What is the fastest way of modifying a list in place?

"""

from src.z_data import data
from z_tester import tester_2d
from zz_import import vrange


# The idea here is you need the element because you're
# going to do something more complicated than += 1
def mod_list_in_place_with_range_len(outer, _vrange=vrange, _len=len):
    for inner in outer:
        for i in _vrange(_len(inner)):
            el = inner[i]
            inner[i] = el + 1

def mod_list_in_place_with_enumerate(outer, _enum=enumerate):
    for inner in outer:
        for i, el in _enum(inner):
            inner[i] = el + 1

# By the way slicing creates a new list, even though its
# immediately destroyed after the slicing is done. So, if
# the elements of the list are more complicated than a number
# and the point is to transform them without there being two
# copies in memory (one of the pre-transform objects and one of
# the post-transform objects) this method is pointless.
def mod_list_in_place_with_colon_enumerate(outer, _enum=enumerate):
    for inner in outer:
        inner[:] = [el + 1 for i, el in _enum(inner)]

def mod_list_in_place_with_with_colon_range_len(outer, _vrange=vrange, _len=len):
    for inner in outer:
        inner[:] = [inner[i] + 1 for i in _vrange(_len(inner))]

def make_new_comprehension(outer):
    for inner in outer:
        [el + 1 for el in inner]

def make_new_append(outer):
    for inner in outer:
        res = []
        for el in inner:
            res.append(el + 1)

def make_new_append_predef(outer):
    for inner in outer:
        res = []; app = res.append
        for el in inner:
            app(el + 1)


tester_2d(
    (
        mod_list_in_place_with_range_len,
        mod_list_in_place_with_enumerate,
        mod_list_in_place_with_colon_enumerate,
        mod_list_in_place_with_with_colon_range_len,
        make_new_append,
        make_new_append_predef,
        make_new_comprehension,
    ),
)


"""
Conclusion:
    Yeah, making a new list is always faster, the only reason to mod it
    in place would be if you're running out of memory.

    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.5137   100  
        make_new_append                               0.4977   97   
        mod_list_in_place_with_with_colon_range_len   0.4693   91   
        mod_list_in_place_with_enumerate              0.4067   79   
        mod_list_in_place_with_range_len              0.397    77   
        make_new_append_predef                        0.3833   75   
        make_new_comprehension                        0.2593   50   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                                          Secs     %    
        make_new_append                               0.3573   100  
        mod_list_in_place_with_range_len              0.314    88   
        mod_list_in_place_with_enumerate              0.3063   86   
        mod_list_in_place_with_colon_enumerate        0.293    82   
        mod_list_in_place_with_with_colon_range_len   0.2723   76   
        make_new_append_predef                        0.2657   74   
        make_new_comprehension                        0.184    51   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                                          Secs     %    
        make_new_append                               0.329    100  
        mod_list_in_place_with_range_len              0.3177   97   
        mod_list_in_place_with_enumerate              0.3067   93   
        mod_list_in_place_with_colon_enumerate        0.261    79   
        mod_list_in_place_with_with_colon_range_len   0.2457   75   
        make_new_append_predef                        0.2327   71   
        make_new_comprehension                        0.1593   48   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                                          Secs     %    
        make_new_append                               0.3207   100  
        mod_list_in_place_with_range_len              0.3163   99   
        mod_list_in_place_with_enumerate              0.3057   95   
        mod_list_in_place_with_colon_enumerate        0.2487   78   
        mod_list_in_place_with_with_colon_range_len   0.2383   74   
        make_new_append_predef                        0.221    69   
        make_new_comprehension                        0.151    47   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                                          Secs     %    
        mod_list_in_place_with_range_len              0.314    100  
        make_new_append                               0.312    99   
        mod_list_in_place_with_enumerate              0.3003   96   
        mod_list_in_place_with_colon_enumerate        0.26     83   
        mod_list_in_place_with_with_colon_range_len   0.2517   80   
        make_new_append_predef                        0.2127   68   
        make_new_comprehension                        0.1383   44   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                                          Secs     %    
        make_new_append                               0.4253   100  
        mod_list_in_place_with_colon_enumerate        0.403    95   
        mod_list_in_place_with_with_colon_range_len   0.3887   91   
        make_new_append_predef                        0.336    79   
        mod_list_in_place_with_range_len              0.314    74   
        mod_list_in_place_with_enumerate              0.302    71   
        make_new_comprehension                        0.2697   63   

    Python38:
        -Seems crazy but it seems that for short lists and long lists a for loop with either enumerate or range len
        is best but for 10k elements colon and list comprehension works better, wtf?
    
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                                          Secs     %    
        mod_list_in_place_with_with_colon_range_len   0.385    100  
        mod_list_in_place_with_colon_enumerate        0.3274   85   
        mod_list_in_place_with_range_len              0.3234   84   
        mod_list_in_place_with_enumerate              0.2752   71   
        make_new_append                               0.2496   65   
        make_new_append_predef                        0.2205   56   
        make_new_comprehension                        0.1883   49   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                                          Secs     %    
        make_new_append                               0.2472   100  
        mod_list_in_place_with_range_len              0.2437   99   
        mod_list_in_place_with_colon_enumerate        0.2312   94   
        mod_list_in_place_with_with_colon_range_len   0.2269   92   
        mod_list_in_place_with_enumerate              0.2154   87   
        make_new_append_predef                        0.2067   84   
        make_new_comprehension                        0.1481   60   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_range_len              0.2838   100  
        mod_list_in_place_with_enumerate              0.2757   97   
        mod_list_in_place_with_colon_enumerate        0.269    95   
        make_new_append                               0.2661   94   
        mod_list_in_place_with_with_colon_range_len   0.2505   88   
        make_new_append_predef                        0.2226   78   
        make_new_comprehension                        0.1602   56   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_range_len              0.2941   100  
        mod_list_in_place_with_enumerate              0.2916   99   
        mod_list_in_place_with_colon_enumerate        0.2791   95   
        make_new_append                               0.2642   90   
        mod_list_in_place_with_with_colon_range_len   0.2519   86   
        make_new_append_predef                        0.2185   74   
        make_new_comprehension                        0.157    53   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.3322   100  
        mod_list_in_place_with_with_colon_range_len   0.3115   94   
        make_new_append                               0.3004   90   
        mod_list_in_place_with_range_len              0.294    89   
        mod_list_in_place_with_enumerate              0.2931   88   
        make_new_append_predef                        0.2586   78   
        make_new_comprehension                        0.1902   56   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.4663   100  
        mod_list_in_place_with_with_colon_range_len   0.452    97   
        make_new_append                               0.4163   89   
        make_new_append_predef                        0.3762   81   
        make_new_comprehension                        0.3159   68   
        mod_list_in_place_with_enumerate              0.2956   63   
        mod_list_in_place_with_range_len              0.2944   63   

    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.2848   100  
        mod_list_in_place_with_with_colon_range_len   0.2555   90   
        mod_list_in_place_with_enumerate              0.2375   83   
        make_new_append_predef                        0.2355   83   
        mod_list_in_place_with_range_len              0.2281   80   
        make_new_append                               0.198    70   
        make_new_comprehension                        0.1433   50   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.2218   100  
        make_new_append_predef                        0.2122   96   
        mod_list_in_place_with_with_colon_range_len   0.1959   88   
        mod_list_in_place_with_enumerate              0.1893   85   
        make_new_append                               0.1881   85   
        mod_list_in_place_with_range_len              0.185    83   
        make_new_comprehension                        0.1348   61   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.2732   100  
        mod_list_in_place_with_enumerate              0.2535   93   
        mod_list_in_place_with_range_len              0.2473   91   
        mod_list_in_place_with_with_colon_range_len   0.2442   89   
        make_new_append_predef                        0.2208   81   
        make_new_append                               0.1919   70   
        make_new_comprehension                        0.1597   57   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.2892   100  
        mod_list_in_place_with_enumerate              0.2717   94   
        mod_list_in_place_with_range_len              0.2665   92   
        mod_list_in_place_with_with_colon_range_len   0.2641   91   
        make_new_append_predef                        0.2231   77   
        make_new_append                               0.2027   70   
        make_new_comprehension                        0.1645   56   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.3013   100  
        mod_list_in_place_with_enumerate              0.2751   91   
        mod_list_in_place_with_with_colon_range_len   0.2734   91   
        mod_list_in_place_with_range_len              0.2674   89   
        make_new_append_predef                        0.2144   71   
        make_new_append                               0.1868   62   
        make_new_comprehension                        0.1583   53   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                                          Secs     %    
        mod_list_in_place_with_colon_enumerate        0.4533   100  
        mod_list_in_place_with_with_colon_range_len   0.4282   94   
        make_new_append_predef                        0.3532   78   
        make_new_append                               0.3264   72   
        make_new_comprehension                        0.2953   65   
        mod_list_in_place_with_enumerate              0.2757   61   
        mod_list_in_place_with_range_len              0.2722   60   

"""


