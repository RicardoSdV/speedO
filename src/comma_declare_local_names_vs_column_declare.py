from itertools import repeat

from src.z_data import data
from src.z_tester import tester

num = data.M10

def overhead():
    for _ in repeat(None, num):
        continue

def declare_1():
    for _ in repeat(None, num):
        a = 1

def comma_declare_2():
    for _ in repeat(None, num):
        a, b = 1, 2

def column_declare_2():
    for _ in repeat(None, num):
        a = 1
        b = 2

def comma_declare_4():
    for _ in repeat(None, num):
        a, b, c, d = 1, 2, 3, 4

def column_declare_4():
    for _ in repeat(None, num):
        a = 1
        b = 2
        c = 3
        d = 4

def comma_declare_8():
    for _ in repeat(None, num):
        a, b, c, d, e, f, g, h = 1, 2, 3, 4, 5, 6, 7, 8

def column_declare_8():
    for _ in repeat(None, num):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8


tester(
    (
        overhead,
        declare_1,
        comma_declare_2,
        column_declare_2,
        comma_declare_4,
        column_declare_4,
        comma_declare_8,
        column_declare_8,
    )
)

"""
Conclusion:
    - The point at which comma declaring is faster shifts with the python version
    but in general it starts being worth it at about 3-4 names.

    Python27:
        Name               Secs     %    
        column_declare_8   0.3084   100  
        comma_declare_8    0.1914   62   
        column_declare_4   0.1438   47   
        comma_declare_4    0.1328   43   
        comma_declare_2    0.1004   33   
        column_declare_2   0.0924   30   
        declare_1          0.0676   22   
        overhead           0.0424   14   
    
    Python38:
        Name               Secs     %    
        column_declare_8   0.2554   100  
        comma_declare_8    0.1729   68   
        column_declare_4   0.1324   52   
        comma_declare_4    0.1182   46   
        comma_declare_2    0.0905   35   
        column_declare_2   0.0846   33   
        declare_1          0.0623   24   
        overhead           0.0362   14   
        
    Python310
        Testing times mean of 5 rounds: 
        Name               Secs     %    
        column_declare_8   0.2692   100  
        comma_declare_8    0.2121   79   
        comma_declare_4    0.1447   54   
        column_declare_4   0.141    52   
        comma_declare_2    0.1078   40   
        column_declare_2   0.0904   34   
        declare_1          0.0657   24   
        overhead           0.0371   14   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name               Secs     %    
        column_declare_8   0.3143   100  
        comma_declare_8    0.211    67   
        column_declare_4   0.1684   54   
        comma_declare_4    0.1381   44   
        column_declare_2   0.1073   34   
        comma_declare_2    0.1026   33   
        declare_1          0.0756   24   
        overhead           0.0384   12   

"""
