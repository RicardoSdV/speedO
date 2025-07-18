from src.z_tester import auto_tester_2d

def _yield_gen(inner):
    for el in inner:
        yield el

def yield_gen_tup(outer, gen=_yield_gen):
    for inner in outer:
        res = tuple(gen(inner))

def yield_gen_list(outer, gen=_yield_gen):
    for inner in outer:
        res = list(gen(inner))


def _comprehension_gen(inner):
    return (el for el in inner)

def comp_gen_tup(outer, gen=_comprehension_gen):
    for inner in outer:
        res = tuple(gen(inner))

def comp_gen_list(outer, gen=_comprehension_gen):
    for inner in outer:
        res = list(gen(inner))


def comprehension_list(outer):
    for inner in outer:
        res = [el for el in inner]

def comprehension_tuple(outer):
    for inner in outer:
        res = tuple(el for el in inner)

def comprehension_and_gen_tuple(outer):
    for inner in outer:
        res = tuple((el for el in inner))

def comprehension_list_to_tuple(outer):
    for inner in outer:
        res = tuple([el for el in inner])

def predef_append(outer):
    for inner in outer:
        res = []; app = res.append
        for el in inner:
            app(el)

def predef_append_to_tuple(outer):
    for inner in outer:
        res = []; app = res.append
        for el in inner:
            app(el)
        tuple(res)

def normal_append(outer):
    for inner in outer:
        res = []
        for el in inner:
            res.append(el)

def normal_append_to_tuple(outer):
    for inner in outer:
        res = []
        for el in inner:
            res.append(el)
        tuple(res)

auto_tester_2d()

"""
Conclusion:
    - List comprehension is always the fastest way. Its so fast in fact that its worth it to make a 
    list only to turn it into a tuple, I think, I'm not sure if this test takes into account GC locals.
    
    - If the stuff happening is too complicated for list comprehension, then predef append is the best
    option until 312 where normal appending becomes good.
    
    
    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                          Secs     %    
        comp_gen_list                 0.5217   100  
        yield_gen_list                0.4767   91   
        comp_gen_tup                  0.472    90   
        comprehension_and_gen_tuple   0.4503   86   
        comprehension_tuple           0.4467   86   
        yield_gen_tup                 0.4293   82   
        normal_append_to_tuple        0.421    81   
        normal_append                 0.417    80   
        predef_append_to_tuple        0.3967   76   
        predef_append                 0.3073   59   
        comprehension_list_to_tuple   0.3007   57   
        comprehension_list            0.2187   42   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                          Secs     %    
        normal_append                 0.308    100  
        normal_append_to_tuple        0.3073   100  
        comp_gen_list                 0.252    82   
        yield_gen_list                0.2453   80   
        comp_gen_tup                  0.2413   78   
        comprehension_and_gen_tuple   0.2387   77   
        comprehension_tuple           0.238    77   
        yield_gen_tup                 0.2367   77   
        predef_append_to_tuple        0.2297   75   
        predef_append                 0.2033   66   
        comprehension_list_to_tuple   0.1577   51   
        comprehension_list            0.1337   43   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                          Secs     %    
        normal_append_to_tuple        0.2707   100  
        normal_append                 0.2697   100  
        comp_gen_list                 0.1873   69   
        comp_gen_tup                  0.187    69   
        yield_gen_tup                 0.1857   69   
        comprehension_and_gen_tuple   0.1853   68   
        comprehension_tuple           0.185    68   
        yield_gen_list                0.185    68   
        predef_append_to_tuple        0.1827   67   
        predef_append                 0.1717   63   
        comprehension_list_to_tuple   0.12     44   
        comprehension_list            0.1067   39   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                          Secs     %    
        normal_append                 0.257    100  
        normal_append_to_tuple        0.257    100  
        comprehension_tuple           0.177    69   
        yield_gen_tup                 0.1763   69   
        comprehension_and_gen_tuple   0.175    68   
        comp_gen_tup                  0.1747   68   
        predef_append_to_tuple        0.1713   67   
        comp_gen_list                 0.1713   67   
        yield_gen_list                0.17     66   
        predef_append                 0.1587   62   
        comprehension_list_to_tuple   0.109    42   
        comprehension_list            0.0953   37   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                          Secs     %    
        normal_append                 0.256    100  
        normal_append_to_tuple        0.253    99   
        yield_gen_tup                 0.181    71   
        comp_gen_tup                  0.178    70   
        predef_append_to_tuple        0.1777   69   
        comprehension_tuple           0.1773   69   
        comprehension_and_gen_tuple   0.1753   68   
        comp_gen_list                 0.1677   65   
        yield_gen_list                0.1677   65   
        predef_append                 0.1503   59   
        comprehension_list_to_tuple   0.117    46   
        comprehension_list            0.094    37   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                          Secs     %    
        normal_append                 0.3517   100  
        normal_append_to_tuple        0.3497   99   
        predef_append_to_tuple        0.2947   84   
        yield_gen_list                0.2613   74   
        comp_gen_list                 0.2597   74   
        predef_append                 0.254    72   
        comprehension_list_to_tuple   0.241    69   
        comprehension_tuple           0.228    65   
        comprehension_and_gen_tuple   0.2273   65   
        comp_gen_tup                  0.2257   64   
        yield_gen_tup                 0.2253   64   
        comprehension_list            0.1997   56   


    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                          Secs     %    
        comp_gen_list                 0.3196   100  
        comp_gen_tup                  0.308    96   
        comprehension_tuple           0.2813   88   
        comprehension_and_gen_tuple   0.2761   86   
        yield_gen_list                0.268    84   
        yield_gen_tup                 0.261    82   
        normal_append_to_tuple        0.2376   74   
        normal_append                 0.2084   65   
        predef_append_to_tuple        0.2013   63   
        comprehension_list_to_tuple   0.1779   56   
        predef_append                 0.1707   53   
        comprehension_list            0.1401   44   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                          Secs     %    
        comp_gen_tup                  0.2931   100  
        yield_gen_tup                 0.2822   96   
        comprehension_and_gen_tuple   0.2796   95   
        comprehension_tuple           0.2793   95   
        normal_append_to_tuple        0.2165   74   
        normal_append                 0.202    69   
        comp_gen_list                 0.2009   69   
        yield_gen_list                0.1983   68   
        predef_append_to_tuple        0.1713   57   
        predef_append                 0.1557   53   
        comprehension_list_to_tuple   0.1064   36   
        comprehension_list            0.0868   30   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.2023   100  
        normal_append                 0.1929   95   
        yield_gen_list                0.1778   88   
        comp_gen_tup                  0.1767   87   
        comp_gen_list                 0.1755   87   
        yield_gen_tup                 0.1754   87   
        comprehension_and_gen_tuple   0.1746   86   
        comprehension_tuple           0.1737   86   
        predef_append_to_tuple        0.154    76   
        predef_append                 0.1437   71   
        comprehension_list_to_tuple   0.0948   47   
        comprehension_list            0.0864   43   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.193    100  
        normal_append                 0.177    92   
        yield_gen_list                0.1652   86   
        comp_gen_list                 0.1638   85   
        yield_gen_tup                 0.1625   84   
        comp_gen_tup                  0.1624   84   
        comprehension_tuple           0.1612   84   
        comprehension_and_gen_tuple   0.1584   82   
        predef_append_to_tuple        0.1428   74   
        predef_append                 0.132    68   
        comprehension_list_to_tuple   0.0865   45   
        comprehension_list            0.0739   38   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.1998   100  
        normal_append                 0.1844   92   
        comp_gen_list                 0.1699   85   
        comp_gen_tup                  0.1697   85   
        yield_gen_tup                 0.1687   84   
        comprehension_tuple           0.1683   84   
        yield_gen_list                0.1667   83   
        comprehension_and_gen_tuple   0.1666   83   
        predef_append_to_tuple        0.1578   79   
        predef_append                 0.1369   69   
        comprehension_list_to_tuple   0.1      50   
        comprehension_list            0.0776   39   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.3223   100  
        normal_append                 0.2806   87   
        predef_append_to_tuple        0.279    87   
        yield_gen_list                0.2617   81   
        comp_gen_list                 0.2608   81   
        predef_append                 0.2347   73   
        comp_gen_tup                  0.2261   70   
        yield_gen_tup                 0.2255   70   
        comprehension_list_to_tuple   0.2247   70   
        comprehension_and_gen_tuple   0.2218   69   
        comprehension_tuple           0.2212   69   
        comprehension_list            0.1782   55   
        
         
    Python310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                          Secs     %    
        comp_gen_list                 0.3621   100  
        comp_gen_tup                  0.3261   90   
        yield_gen_list                0.3062   85   
        comprehension_and_gen_tuple   0.3056   84   
        comprehension_tuple           0.3035   84   
        yield_gen_tup                 0.2651   73   
        normal_append_to_tuple        0.244    67   
        predef_append_to_tuple        0.2281   63   
        normal_append                 0.2226   61   
        comprehension_list_to_tuple   0.2099   57   
        predef_append                 0.1988   55   
        comprehension_list            0.1845   51   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                          Secs     %    
        normal_append_to_tuple        0.3209   100  
        comp_gen_list                 0.3164   99   
        normal_append                 0.3055   95   
        yield_gen_list                0.3018   94   
        predef_append_to_tuple        0.286    89   
        predef_append                 0.2664   83   
        comprehension_and_gen_tuple   0.2298   72   
        comprehension_tuple           0.2298   72   
        comp_gen_tup                  0.2293   71   
        yield_gen_tup                 0.2201   69   
        comprehension_list_to_tuple   0.2127   66   
        comprehension_list            0.1965   61   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.2336   100  
        normal_append                 0.2179   93   
        comp_gen_list                 0.2112   90   
        yield_gen_list                0.21     90   
        comprehension_and_gen_tuple   0.189    81   
        yield_gen_tup                 0.1889   81   
        comp_gen_tup                  0.1869   80   
        predef_append_to_tuple        0.1855   79   
        comprehension_tuple           0.1852   79   
        predef_append                 0.1767   76   
        comprehension_list_to_tuple   0.1213   52   
        comprehension_list            0.1117   48   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.2095   100  
        normal_append                 0.1962   94   
        comp_gen_list                 0.1894   90   
        yield_gen_list                0.186    89   
        comp_gen_tup                  0.1829   87   
        comprehension_and_gen_tuple   0.1812   87   
        comprehension_tuple           0.1777   85   
        yield_gen_tup                 0.1756   84   
        predef_append_to_tuple        0.1625   78   
        predef_append                 0.1512   72   
        comprehension_list_to_tuple   0.1039   50   
        comprehension_list            0.0913   44   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.2152   100  
        normal_append                 0.1978   92   
        yield_gen_tup                 0.1912   89   
        comp_gen_tup                  0.1907   89   
        comprehension_and_gen_tuple   0.189    88   
        comprehension_tuple           0.1857   86   
        comp_gen_list                 0.1853   86   
        yield_gen_list                0.1847   86   
        predef_append_to_tuple        0.1705   79   
        predef_append                 0.1529   71   
        comprehension_list_to_tuple   0.1091   51   
        comprehension_list            0.0886   41   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                          Secs     %    
        normal_append_to_tuple        0.3413   100  
        normal_append                 0.2949   86   
        predef_append_to_tuple        0.2899   85   
        comp_gen_list                 0.2884   85   
        yield_gen_list                0.2801   82   
        predef_append                 0.2512   74   
        yield_gen_tup                 0.2483   73   
        comp_gen_tup                  0.2458   72   
        comprehension_and_gen_tuple   0.2453   72   
        comprehension_tuple           0.243    71   
        comprehension_list_to_tuple   0.2309   68   
        comprehension_list            0.1913   56    

    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                          Secs     %    
        comp_gen_list                 0.3328   100  
        comp_gen_tup                  0.3084   93   
        comprehension_tuple           0.2903   87   
        comprehension_and_gen_tuple   0.2902   87   
        yield_gen_list                0.2834   85   
        yield_gen_tup                 0.2625   79   
        predef_append_to_tuple        0.2144   64   
        predef_append                 0.1872   56   
        normal_append_to_tuple        0.1833   55   
        normal_append                 0.1654   50   
        comprehension_list_to_tuple   0.1309   39   
        comprehension_list            0.1046   31   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                          Secs     %    
        comp_gen_list                 0.2313   100  
        comp_gen_tup                  0.2273   98   
        comprehension_and_gen_tuple   0.2267   98   
        yield_gen_list                0.2255   97   
        comprehension_tuple           0.2239   97   
        yield_gen_tup                 0.2219   96   
        predef_append_to_tuple        0.1872   81   
        predef_append                 0.1707   74   
        normal_append_to_tuple        0.1662   72   
        normal_append                 0.1533   66   
        comprehension_list_to_tuple   0.1025   44   
        comprehension_list            0.0884   38   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                          Secs     %    
        yield_gen_list                0.2121   100  
        comp_gen_list                 0.2117   100  
        comprehension_and_gen_tuple   0.1989   94   
        yield_gen_tup                 0.1981   93   
        comprehension_tuple           0.1974   93   
        comp_gen_tup                  0.1969   93   
        predef_append_to_tuple        0.1589   75   
        predef_append                 0.1501   71   
        normal_append_to_tuple        0.1422   67   
        normal_append                 0.1305   62   
        comprehension_list_to_tuple   0.0977   46   
        comprehension_list            0.0891   42   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                          Secs     %    
        yield_gen_list                0.209    100  
        comp_gen_list                 0.2073   99   
        yield_gen_tup                 0.2007   96   
        comprehension_and_gen_tuple   0.1997   96   
        comprehension_tuple           0.1989   95   
        comp_gen_tup                  0.1958   94   
        predef_append_to_tuple        0.1542   74   
        predef_append                 0.1413   68   
        normal_append_to_tuple        0.1344   64   
        normal_append                 0.1236   59   
        comprehension_list_to_tuple   0.1001   48   
        comprehension_list            0.0882   42   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                          Secs     %    
        comp_gen_list                 0.2098   100  
        comp_gen_tup                  0.208    99   
        comprehension_tuple           0.2074   99   
        comprehension_and_gen_tuple   0.2069   99   
        yield_gen_list                0.2067   99   
        yield_gen_tup                 0.2046   98   
        predef_append_to_tuple        0.1591   76   
        predef_append                 0.1424   68   
        normal_append_to_tuple        0.1419   68   
        normal_append                 0.1219   57   
        comprehension_list_to_tuple   0.1087   52   
        comprehension_list            0.088    42   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                          Secs     %    
        yield_gen_list                0.3008   100  
        comp_gen_list                 0.2999   100  
        predef_append_to_tuple        0.2791   93   
        yield_gen_tup                 0.2698   90   
        normal_append_to_tuple        0.2636   88   
        comprehension_tuple           0.2628   87   
        comprehension_and_gen_tuple   0.2593   86   
        comp_gen_tup                  0.2592   86   
        predef_append                 0.2422   81   
        comprehension_list_to_tuple   0.2285   76   
        normal_append                 0.2189   73   
        comprehension_list            0.1856   62    
"""
