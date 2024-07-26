"""
What is the best way of storing a time info in memory?
What is the fastest way of creating said memory?
"""
import gc
import time
from datetime import datetime
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M

def datetime_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(datetime.now())

    del result
    gc.collect()

def time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(datetime.now().time())

    del result
    gc.collect()

def int_datetime_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result((now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond//1000))

    del result
    gc.collect()

def int_time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result((now.hour, now.minute, now.second, now.microsecond//1000))

    del result
    gc.collect()

def str_datetime_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

    del result
    gc.collect()

def str_time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(datetime.now().strftime('%H:%M:%S.%f')[:-3])

    del result
    gc.collect()

def unix_time():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(time.time())

    del result
    gc.collect()


if __name__ == '__main__':
    tester(
        (
            datetime_stamp,
            time_stamp,
            int_datetime_stamp,
            int_time_stamp,
            str_datetime_stamp,
            str_time_stamp,
            unix_time,
        ),
        testing_what='times'
    )
    tester(
        (
            datetime_stamp,
            time_stamp,
            int_datetime_stamp,
            int_time_stamp,
            str_datetime_stamp,
            str_time_stamp,
            unix_time,
        ),
        testing_what='memories'
    )

"""
Conclusion:
    - Unix stamps are the way to go for almost everything 
    (probably not if you want to immediately print, then a datetime is probably better)
    
    - datetime uses less memory in Python27 in later versions uses more.
    
    - datetime is slower in Python27 faster in later versions
    
    - Seems like any sort of turning anything into ints or strs is just bad
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   1.4562   100  
        str_time_stamp       1.3602   93   
        int_datetime_stamp   0.538    37   
        int_time_stamp       0.4724   32   
        time_stamp           0.3788   26   
        datetime_stamp       0.3624   25   
        unix_time            0.06     4    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   65.3281   100  
        str_datetime_stamp   45.3828   69   
        int_time_stamp       16.6523   25   
        datetime_stamp       8.9414    14   
        str_time_stamp       7.6797    12   
        unix_time            7.1563    11   
        time_stamp           7.0703    11   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   1.4562   100  
        str_time_stamp       1.3602   93   
        int_datetime_stamp   0.538    37   
        int_time_stamp       0.4724   32   
        time_stamp           0.3788   26   
        datetime_stamp       0.3624   25   
        unix_time            0.06     4    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   65.3281   100  
        str_datetime_stamp   45.3828   69   
        int_time_stamp       16.6523   25   
        datetime_stamp       8.9414    14   
        str_time_stamp       7.6797    12   
        unix_time            7.1563    11   
        time_stamp           7.0703    11   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   3.5771   100  
        str_time_stamp       2.816    79   
        int_datetime_stamp   0.3397   9    
        int_time_stamp       0.2926   8    
        time_stamp           0.2192   6    
        datetime_stamp       0.1996   6    
        unix_time            0.0605   2    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        int_datetime_stamp   109.7188   100  
        str_datetime_stamp   76.8438    70   
        str_time_stamp       61.7188    56   
        int_time_stamp       60.7578    55   
        datetime_stamp       44.1328    40   
        time_stamp           31.332     28   
        unix_time            28.6641    26   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   3.7104   100  
        str_time_stamp       2.9172   79   
        int_datetime_stamp   0.3448   9    
        int_time_stamp       0.2979   8    
        time_stamp           0.2183   6    
        datetime_stamp       0.2003   5    
        unix_time            0.0529   1    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   94.8789   100  
        str_datetime_stamp   55.5312   59   
        str_time_stamp       55.4922   57   
        int_time_stamp       52.7148   56   
        datetime_stamp       39.0703   41   
        unix_time            18.3281   19   
        time_stamp           8.875     9   
    
    PyPy313:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   1.5908   100  
        str_time_stamp       1.4266   90   
        int_datetime_stamp   1.0053   63   
        datetime_stamp       0.9937   62   
        int_time_stamp       0.9449   59   
        time_stamp           0.9314   59   
        unix_time            0.0543   3    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        str_datetime_stamp   150.0039   100  
        int_time_stamp       141.625    94   
        time_stamp           110.4414   74   
        datetime_stamp       90.5586    60   
        int_datetime_stamp   85.4336    56   
        str_time_stamp       57.8867    39   
        unix_time            16.8516    11   
"""

