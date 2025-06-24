from src.z_data import data
from src.z_tester import tester_2d


def use_max(outer):
    for inner in outer:
        _max = max(inner)

# When you need to iter for other reasons still worth it?
def use_max_and_iter(outer):
    for inner in outer:
        _max = max(el for el in inner)

def use_max_and_iter_gen(outer):
    for inner in outer:
        _max = max((el for el in inner))

def use_max_and_iter_list(outer):
    for inner in outer:
        _max = max([el for el in inner])

def use_for_loop(outer):
    for inner in outer:
        _max = 0
        for el in inner:
            if el > _max:
                _max = el


tester_2d((use_for_loop, use_max, use_max_and_iter, use_max_and_iter_gen, use_max_and_iter_list))


"""
Conclusion:
If you don't need to iterate, use max(), if you need to iterate anyways to filter for example, 
then use a for loop. If you insist in using max() to iterate, you're most likely better off
using a list comprehension. There are exceptions.

Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name                    Secs     %    
    use_max_and_iter        0.361    100  
    use_max_and_iter_gen    0.3607   100  
    use_max_and_iter_list   0.3587   99   
    use_for_loop            0.1643   46   
    use_max                 0.1263   35   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name                    Secs     %    
    use_max_and_iter_gen    0.2393   100  
    use_max_and_iter        0.2377   99   
    use_max_and_iter_list   0.225    94   
    use_for_loop            0.127    53   
    use_max                 0.078    33   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name                    Secs     %    
    use_max_and_iter        0.227    100  
    use_max_and_iter_gen    0.2267   100  
    use_max_and_iter_list   0.1887   83   
    use_for_loop            0.1227   54   
    use_max                 0.076    33   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name                    Secs     %    
    use_max_and_iter_gen    0.2283   100  
    use_max_and_iter        0.2253   99   
    use_max_and_iter_list   0.1853   81   
    use_for_loop            0.1193   52   
    use_max                 0.075    33   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name                    Secs     %    
    use_max_and_iter_gen    0.2227   100  
    use_max_and_iter        0.2217   100  
    use_max_and_iter_list   0.17     76   
    use_for_loop            0.12     54   
    use_max                 0.075    34   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name                    Secs     %    
    use_max_and_iter_list   0.3013   100  
    use_max_and_iter_gen    0.227    75   
    use_max_and_iter        0.2257   75   
    use_for_loop            0.12     40   
    use_max                 0.0757   25   
    
Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                    Secs     %    
    use_max_and_iter        0.3279   100  
    use_max_and_iter_gen    0.3277   100  
    use_max_and_iter_list   0.2538   77   
    use_for_loop            0.1431   44   
    use_max                 0.0899   27   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                    Secs     %    
    use_max_and_iter_gen    0.201    100  
    use_max_and_iter        0.1989   99   
    use_max_and_iter_list   0.15     75   
    use_for_loop            0.1327   66   
    use_max                 0.0549   27   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                    Secs     %    
    use_max_and_iter        0.1823   100  
    use_max_and_iter_gen    0.1815   100  
    use_max_and_iter_list   0.1363   75   
    use_for_loop            0.128    70   
    use_max                 0.0507   28   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                    Secs     %    
    use_max_and_iter        0.1806   100  
    use_max_and_iter_gen    0.1797   100  
    use_for_loop            0.1295   72   
    use_max_and_iter_list   0.1234   68   
    use_max                 0.0476   26   


Python310:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                    Secs     %    
    use_max_and_iter_gen    0.3515   100  
    use_max_and_iter        0.345    98   
    use_max_and_iter_list   0.2936   84   
    use_for_loop            0.185    53   
    use_max                 0.0908   26   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                    Secs     %    
    use_max_and_iter_list   0.2516   100  
    use_max_and_iter        0.2164   86   
    use_max_and_iter_gen    0.2164   86   
    use_for_loop            0.1565   62   
    use_max                 0.0506   20   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                    Secs     %    
    use_max_and_iter        0.1999   100  
    use_max_and_iter_gen    0.1992   100  
    use_max_and_iter_list   0.1572   79   
    use_for_loop            0.1509   75   
    use_max                 0.0451   23   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                    Secs     %    
    use_max_and_iter        0.1954   100  
    use_max_and_iter_gen    0.1943   99   
    use_for_loop            0.1505   77   
    use_max_and_iter_list   0.1355   69   
    use_max                 0.0438   22   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                    Secs     %    
    use_max_and_iter_gen    0.2005   100  
    use_max_and_iter        0.1998   100  
    use_for_loop            0.1567   78   
    use_max_and_iter_list   0.1335   67   
    use_max                 0.0475   24   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                    Secs     %    
    use_max_and_iter_list   0.2665   100  
    use_max_and_iter_gen    0.1964   74   
    use_max_and_iter        0.1959   73   
    use_for_loop            0.1516   56   
    use_max                 0.0454   17   

    
Python312:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                    Secs     %    
    use_max_and_iter        0.3471   100  
    use_max_and_iter_gen    0.3463   100  
    use_max_and_iter_list   0.2103   61   
    use_for_loop            0.1643   47   
    use_max                 0.0893   26   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                    Secs     %    
    use_max_and_iter        0.2132   100  
    use_max_and_iter_gen    0.2113   99   
    use_max_and_iter_list   0.1478   69   
    use_for_loop            0.1421   67   
    use_max                 0.0532   25   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                    Secs     %    
    use_max_and_iter_gen    0.2088   100  
    use_max_and_iter        0.2049   98   
    use_max_and_iter_list   0.1416   68   
    use_for_loop            0.1362   65   
    use_max                 0.0479   23   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                    Secs     %    
    use_max_and_iter_gen    0.2062   100  
    use_max_and_iter        0.2035   99   
    use_max_and_iter_list   0.136    66   
    use_for_loop            0.1338   65   
    use_max                 0.046    22   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                    Secs     %    
    use_max_and_iter        0.2053   100  
    use_max_and_iter_gen    0.2049   100  
    use_max_and_iter_list   0.1377   67   
    use_for_loop            0.1346   66   
    use_max                 0.0472   23   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                    Secs     %    
    use_max_and_iter_list   0.2617   100  
    use_max_and_iter_gen    0.2082   80   
    use_max_and_iter        0.2055   79   
    use_for_loop            0.1337   51   
    use_max                 0.0479   18   

"""
