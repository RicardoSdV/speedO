"""
When you "need" to append what is the fastest way?
The fastest way is list comprehension but some people don't find this readable
and sometimes its a mess to have to define a bunch of generators and so on to
be able to have complex loops happen in list comprehension
"""
from collections import deque

from src.z_data import data
from src.z_tester import tester_2d

class CircularBuffer(object):
    def __init__(self, size=2000):
        self.__list = [None] * size
        self.__cnt = 0
        self.__size = size

    def append_try_except(self, el):
        try:
            self.__cnt += 1
            self.__list[self.__cnt] = el
        except IndexError:
            self.__cnt = 0
            self.__list[self.__cnt] = el

    def check_and_append(self, el):
        self.__cnt += 1
        if self.__cnt == self.__size:
            self.__cnt = 0

        self.__list[self.__cnt] = el

circular_buffer = CircularBuffer()
deque_circ_buff = deque(maxlen=2000)
_deque = deque()
app_to_circ_buff = deque_circ_buff.append
app_deque = _deque.append

def normal_append(list_2d):
    for inner_list in list_2d:
        result = []
        for i in inner_list:
            result.append(i)

def predef_append(list_2d):
    for inner_list in list_2d:
        result = []
        res_app = result.append
        for i in inner_list:
            res_app(i)

def prealloc(list_2d):
    """ Enumerate makes sense because normally you wouldn't assign the index """
    for inner_list in list_2d:
        result = [None] * len(inner_list)
        for i, j in enumerate(inner_list):
            result[i] = j

def circular_buffer_check_and_append(list_2d):
    app = circular_buffer.check_and_append
    for inner_list in list_2d:
        for el in inner_list:
            app(el)

def circular_buffer_append_try_except(list_2d):
    app = circular_buffer.append_try_except
    for inner_list in list_2d:
        for el in inner_list:
            app(el)

def deque_circ_buff(outer):
    app = app_to_circ_buff
    for inner in outer:
        for el in inner:
            app(el)

def deque_circ_buff_no_max(outer):
    for inner in outer:
        app = app_deque
        for el in inner:
            app(el)

tester_2d(
    (
        normal_append,
        predef_append,
        prealloc,
        circular_buffer_check_and_append,
        circular_buffer_append_try_except,
        deque_circ_buff,
        deque_circ_buff_no_max,
    ),
)


"""
Conclusion:
    - Writing your own circular buffer is a terrible idea, deque is surprisingly fast, specially for smaller sizes,
    which seems wierd. Also maxlen vs no maxlen seems kinda strange, because it makes sense for small inner lists 
    having maxlen is faster since you dont have to create a new deque, but why is it faster when the list is like 
    1M elements? maybe because the deque doesnt have to grow.
    
    Python 27:
        - Predefining the append is always way faster, however, if you have a list > 10M elements
        it might make sense to preallocate the elements and assign them        
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                                Secs     %    
        circular_buffer_check_and_append    1.3533   100  
        circular_buffer_append_try_except   1.183    87   
        prealloc                            0.4773   35   
        normal_append                       0.4127   30   
        predef_append                       0.298    22   
        deque_circ_buff_no_max              0.2067   15   
        deque_circ_buff                     0.1807   13   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                                Secs     %    
        circular_buffer_check_and_append    1.8803   100  
        circular_buffer_append_try_except   1.529    81   
        normal_append                       0.3897   21   
        prealloc                            0.359    19   
        predef_append                       0.2833   15   
        deque_circ_buff_no_max              0.259    14   
        deque_circ_buff                     0.2353   13   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    2.1807   100  
        circular_buffer_append_try_except   1.725    79   
        normal_append                       0.521    24   
        prealloc                            0.3997   18   
        predef_append                       0.3547   16   
        deque_circ_buff_no_max              0.2943   13   
        deque_circ_buff                     0.2663   12   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    2.177    100  
        circular_buffer_append_try_except   1.7317   80   
        normal_append                       0.486    22   
        prealloc                            0.4047   19   
        predef_append                       0.31     14   
        deque_circ_buff_no_max              0.2997   14   
        deque_circ_buff                     0.275    13   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    2.192    100  
        circular_buffer_append_try_except   1.72     78   
        normal_append                       0.497    23   
        prealloc                            0.419    19   
        predef_append                       0.3167   14   
        deque_circ_buff_no_max              0.2903   13   
        deque_circ_buff                     0.267    12   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    2.2      100  
        circular_buffer_append_try_except   1.7373   79   
        normal_append                       0.693    31   
        predef_append                       0.514    23   
        prealloc                            0.4483   20   
        deque_circ_buff_no_max              0.3033   14   
        deque_circ_buff                     0.275    13   

    Python38:
        - As we know normal append becomes better in python3, but predefining it still 
        faster. Prealloc the list increases its range to > 1M
    
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9938   100  
        circular_buffer_append_try_except   0.8161   82   
        prealloc                            0.2679   27   
        normal_append                       0.2025   20   
        predef_append                       0.1704   17   
        deque_circ_buff                     0.153    15   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9741   100  
        circular_buffer_append_try_except   0.8066   83   
        normal_append                       0.1975   20   
        prealloc                            0.1854   19   
        predef_append                       0.1588   16   
        deque_circ_buff                     0.1378   14   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9827   100  
        circular_buffer_append_try_except   0.8183   83   
        prealloc                            0.2054   21   
        normal_append                       0.1886   19   
        predef_append                       0.1424   14   
        deque_circ_buff                     0.1344   14   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9832   100  
        circular_buffer_append_try_except   0.8092   82   
        prealloc                            0.2143   22   
        normal_append                       0.1785   18   
        predef_append                       0.1358   14   
        deque_circ_buff                     0.1292   13   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9802   100  
        circular_buffer_append_try_except   0.8141   83   
        prealloc                            0.2283   23   
        normal_append                       0.179    18   
        deque_circ_buff                     0.1358   14   
        predef_append                       0.1341   14   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                                Secs     %    
        circular_buffer_check_and_append    0.9881   100  
        circular_buffer_append_try_except   0.8088   82   
        normal_append                       0.2832   28   
        predef_append                       0.2401   24   
        prealloc                            0.2358   24   
        deque_circ_buff                     0.1322   13   

        
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