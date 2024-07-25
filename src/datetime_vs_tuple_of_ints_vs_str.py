"""
What is the best way of storing a time info in memory?
What is the fastest way of creating said memory?
"""
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

def time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        append_to_result(datetime.now().time())

def int_datetime_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result((now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond//1000))

def int_time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result((now.hour, now.minute, now.second, now.microsecond//1000))

def str_datetime_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result(now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

def str_time_stamp():
    result = []
    append_to_result = result.append

    for _ in repeat(None, num):
        now = datetime.now()
        append_to_result(now.strftime('%H:%M:%S.%f')[:-3])


if __name__ == '__main__':
    tester(
        (
            datetime_stamp,
            time_stamp,
            int_datetime_stamp,
            int_time_stamp,
            str_datetime_stamp,
            str_time_stamp,
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
        ),
        testing_what='memories'
    )

"""
Conclusion:
    Seems like datetime objects are incredibly well optimized, & one of the few occasions were
    in Python27 they use less memory and as the versions increase they get faster, yet start
    using more memory.
    
    Caveat: The microseconds are //1000 because that much precision is mostly useless, but this 
    definitely mas the non str and int stamp creation slower, yet should reduce memory

    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   1.4892   100  
        str_time_stamp       1.3898   93   
        int_datetime_stamp   0.53     36   
        int_time_stamp       0.4622   31   
        time_stamp           0.3824   26   
        datetime_stamp       0.3582   24   
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   71.9648   100  
        str_datetime_stamp   67.0156   93   
        str_time_stamp       51.9961   72   
        datetime_stamp       35.9102   50   
        int_time_stamp       10.6719   15   
        time_stamp           6.1523    9    
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   3.6034   100  
        str_time_stamp       2.8248   78   
        int_datetime_stamp   0.3165   9    
        int_time_stamp       0.2748   8    
        time_stamp           0.2018   6    
        datetime_stamp       0.1809   5    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        int_datetime_stamp   114.4961   100  
        str_datetime_stamp   82.6836    72   
        int_time_stamp       80.5156    70   
        str_time_stamp       66.2578    57   
        datetime_stamp       49.5469    43   
        time_stamp           34.6367    30   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   3.6001   100  
        str_time_stamp       2.8134   78   
        int_datetime_stamp   0.339    9    
        int_time_stamp       0.2886   8    
        time_stamp           0.2146   6    
        datetime_stamp       0.1935   5    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   94.3789   100  
        str_datetime_stamp   77.0195   82   
        int_time_stamp       74.8086   79   
        str_time_stamp       63.6055   67   
        datetime_stamp       46.6602   49   
        time_stamp           15.0859   16   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   3.702    100  
        str_time_stamp       2.9782   80   
        int_datetime_stamp   0.3399   9    
        int_time_stamp       0.2936   8    
        time_stamp           0.212    6    
        datetime_stamp       0.1942   5    
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs      %    
        int_datetime_stamp   86.4648   100  
        int_time_stamp       69.2773   80   
        str_time_stamp       59.6953   69   
        str_datetime_stamp   59.5938   69   
        datetime_stamp       40.6641   47   
        time_stamp           27.1992   31   
    
    PyPy313:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        str_datetime_stamp   1.5705   100  
        str_time_stamp       1.4381   92   
        int_datetime_stamp   1.0036   64   
        int_time_stamp       0.9586   61   
        datetime_stamp       0.9561   61   
        time_stamp           0.9402   60   
        
        Testing memories mean of 5 rounds: 
        Name                 Mibs       %    
        int_time_stamp       167.5      100  
        str_datetime_stamp   129.9492   78   
        int_datetime_stamp   128.4453   77   
        time_stamp           128.3594   77   
        datetime_stamp       106.3047   63   
        str_time_stamp       47.9141    28   
"""

