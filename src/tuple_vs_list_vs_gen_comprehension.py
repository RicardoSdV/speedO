from src.z_data import data
from src.z_tester import tester_2d


num = data.M100

def tupleComprehension(outer):
    for inner in outer:
        tuple(el for el in inner)

def tupleGenComprehension(outer):
    for inner in outer:
        tuple((el for el in inner))

def listComprehension(outer):
    for inner in outer:
        [el for el in inner]

def listGenComprehension(outer):
    for inner in outer:
        list((el for el in inner))

def tupleListComprehension(outer):
    for inner in outer:
        tuple([el for el in inner])


tester_2d(
    (
        tupleComprehension,
        tupleGenComprehension,
        listComprehension,
        listGenComprehension,
        tupleListComprehension,
    ),
)

"""
Conclusion:
    - Basically, use list comprehension.

    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                     Secs     %    
        listGenComprehension     0.4837   100  
        tupleComprehension       0.442    91   
        tupleGenComprehension    0.442    91   
        tupleListComprehension   0.2957   61   
        listComprehension        0.2053   42   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                     Secs     %    
        listGenComprehension     0.244    100  
        tupleComprehension       0.234    96   
        tupleGenComprehension    0.2337   96   
        tupleListComprehension   0.152    62   
        listComprehension        0.1317   54   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                     Secs     %    
        listGenComprehension     0.1823   100  
        tupleGenComprehension    0.181    99   
        tupleComprehension       0.18     99   
        tupleListComprehension   0.118    65   
        listComprehension        0.105    57   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                     Secs     %    
        tupleComprehension       0.173    100  
        tupleGenComprehension    0.172    99   
        listGenComprehension     0.1653   96   
        tupleListComprehension   0.111    64   
        listComprehension        0.0987   56   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                     Secs     %    
        tupleComprehension       0.1663   100  
        tupleGenComprehension    0.166    100  
        listGenComprehension     0.1607   97   
        tupleListComprehension   0.1143   69   
        listComprehension        0.0927   56   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                     Secs     %    
        listGenComprehension     0.2627   100  
        tupleListComprehension   0.238    91   
        tupleComprehension       0.227    86   
        tupleGenComprehension    0.2233   85   
        listComprehension        0.197    75   
    
    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                     Secs     %    
        listGenComprehension     0.282    100  
        tupleGenComprehension    0.2703   96   
        tupleComprehension       0.2651   94   
        tupleListComprehension   0.1675   59   
        listComprehension        0.1336   47   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                     Secs     %    
        tupleComprehension       0.2773   100  
        tupleGenComprehension    0.2753   99   
        listGenComprehension     0.1952   70   
        tupleListComprehension   0.1036   37   
        listComprehension        0.0861   31   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                     Secs     %    
        listGenComprehension     0.1767   100  
        tupleGenComprehension    0.1736   98   
        tupleComprehension       0.1729   98   
        tupleListComprehension   0.0929   53   
        listComprehension        0.0824   47   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                     Secs     %    
        listGenComprehension     0.1651   100  
        tupleGenComprehension    0.1583   96   
        tupleComprehension       0.1581   96   
        tupleListComprehension   0.0881   53   
        listComprehension        0.0725   44   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                     Secs     %    
        listGenComprehension     0.167    100  
        tupleGenComprehension    0.1661   99   
        tupleComprehension       0.1622   97   
        tupleListComprehension   0.0947   56   
        listComprehension        0.0736   44   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                     Secs     %    
        listGenComprehension     0.2581   100  
        tupleComprehension       0.2264   88   
        tupleGenComprehension    0.2257   87   
        tupleListComprehension   0.2236   87   
        listComprehension        0.1785   69   
    
    Python310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                     Secs     %    
        listGenComprehension     0.3195   100  
        tupleComprehension       0.2906   91   
        tupleGenComprehension    0.2882   90   
        tupleListComprehension   0.209    65   
        listComprehension        0.1772   55   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                     Secs     %    
        listGenComprehension     0.2999   100  
        tupleGenComprehension    0.2177   73   
        tupleComprehension       0.2171   72   
        tupleListComprehension   0.2109   70   
        listComprehension        0.1925   64   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                     Secs     %    
        listGenComprehension     0.2039   100  
        tupleComprehension       0.1838   90   
        tupleGenComprehension    0.1803   88   
        tupleListComprehension   0.1207   59   
        listComprehension        0.1122   55   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                     Secs     %    
        listGenComprehension     0.1854   100  
        tupleComprehension       0.1786   96   
        tupleGenComprehension    0.177    95   
        tupleListComprehension   0.101    54   
        listComprehension        0.0927   50   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                     Secs     %    
        tupleComprehension       0.1837   100  
        tupleGenComprehension    0.1809   98   
        listGenComprehension     0.1801   98   
        tupleListComprehension   0.1087   59   
        listComprehension        0.0856   47   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                     Secs     %    
        listGenComprehension     0.2843   100  
        tupleComprehension       0.245    86   
        tupleGenComprehension    0.2436   86   
        tupleListComprehension   0.2247   79   
        listComprehension        0.1913   67   
    
    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                     Secs     %    
        listGenComprehension     0.3192   100  
        tupleGenComprehension    0.291    91   
        tupleComprehension       0.2887   90   
        tupleListComprehension   0.1233   39   
        listComprehension        0.1055   33   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                     Secs     %    
        listGenComprehension     0.2277   100  
        tupleComprehension       0.224    98   
        tupleGenComprehension    0.2236   98   
        tupleListComprehension   0.1014   45   
        listComprehension        0.0873   38   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                     Secs     %    
        listGenComprehension     0.2995   100  
        tupleComprehension       0.2393   80   
        tupleGenComprehension    0.2378   79   
        tupleListComprehension   0.15     50   
        listComprehension        0.1242   41   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                     Secs     %    
        listGenComprehension     0.3246   100  
        tupleGenComprehension    0.3128   96   
        tupleComprehension       0.3093   95   
        tupleListComprehension   0.1538   47   
        listComprehension        0.1381   43   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                     Secs     %    
        tupleComprehension       0.3136   100  
        listGenComprehension     0.3097   99   
        tupleGenComprehension    0.3084   98   
        tupleListComprehension   0.1447   46   
        listComprehension        0.1282   41   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                     Secs     %    
        listGenComprehension     0.3495   100  
        tupleComprehension       0.3485   100  
        tupleGenComprehension    0.3483   100  
        tupleListComprehension   0.2624   75   
        listComprehension        0.2402   69   
        
"""
