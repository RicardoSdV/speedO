from src.z_tester import tester_2d

def _normal_appender(_list):
    result = []
    for i in _list:
        result.append(i)
    return result

def _predef_appender(_list):
    result = []
    append = result.append
    for i in _list:
        append(i)
    return result

def _generator(_list):
    for i in _list:
        yield i

def normal_append(list_2d, cal=_normal_appender):
    for inner in list_2d:
        cal(inner)

def predef_append(list_2d, cal=_predef_appender):
    for inner in list_2d:
        cal(inner)

def generate_list(list_2d, cal=_generator):
    for inner in list_2d:
        list(cal(inner))

def generate_tuple(list_2d, cal=_generator):
    for inner in list_2d:
        tuple(cal(inner))

tester_2d(
    (
        normal_append,
        predef_append,
        generate_list,
        generate_tuple,
    ),
)


"""
Conclusion:
    - If you're going to create a generator to immediately consume it into a list or a tuple
    it makes more sense to use a predefined append or a normal append in python312. 
    
    - However, it remains a question if it still makes sense to use a generator when the only purpose
    is to iterate over it once in some other loop, the entire premise of this test is that
    you do want a sequence after calling the generator.
    
    - Also, keeps proving how bad the normal append is until 312
    
    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name             Secs     %    
        generate_list    0.4997   100  
        normal_append    0.4597   92   
        generate_tuple   0.4277   86   
        predef_append    0.3413   68   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name             Secs     %    
        normal_append    0.311    100  
        generate_list    0.2423   78   
        generate_tuple   0.232    75   
        predef_append    0.2053   66   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name             Secs     %    
        normal_append    0.2653   100  
        generate_list    0.1863   70   
        generate_tuple   0.1837   69   
        predef_append    0.171    64   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name             Secs     %    
        normal_append    0.256    100  
        generate_tuple   0.1737   68   
        generate_list    0.171    67   
        predef_append    0.1613   63   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name             Secs     %    
        normal_append    0.2527   100  
        generate_tuple   0.174    69   
        generate_list    0.162    64   
        predef_append    0.1557   62   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name             Secs     %    
        normal_append    0.3723   100  
        generate_list    0.273    73   
        predef_append    0.27     73   
        generate_tuple   0.2297   62   
        
    Python38:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name             Secs     %    
        generate_list    0.2604   100  
        generate_tuple   0.2501   96   
        normal_append    0.2229   86   
        predef_append    0.1945   75   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name             Secs     %    
        generate_tuple   0.2719   100  
        normal_append    0.1982   73   
        generate_list    0.1912   70   
        predef_append    0.1549   56   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name             Secs     %    
        normal_append    0.1846   100  
        generate_list    0.1724   93   
        generate_tuple   0.1704   92   
        predef_append    0.1406   76   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name             Secs     %    
        normal_append    0.1748   100  
        generate_list    0.1611   92   
        generate_tuple   0.1557   89   
        predef_append    0.1287   74   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name             Secs     %    
        normal_append    0.1717   100  
        generate_list    0.1582   92   
        generate_tuple   0.1573   92   
        predef_append    0.1279   75   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name             Secs     %    
        normal_append    0.293    100  
        generate_list    0.2673   91   
        predef_append    0.2436   83   
        generate_tuple   0.2277   78   
        
    Python310:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name             Secs     %    
        generate_list    0.2916   100  
        generate_tuple   0.2639   91   
        normal_append    0.2408   83   
        predef_append    0.2242   77   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name             Secs     %    
        normal_append    0.3009   100  
        generate_list    0.2892   96   
        predef_append    0.2642   88   
        generate_tuple   0.2148   71   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name             Secs     %    
        normal_append    0.2148   100  
        generate_list    0.2036   95   
        generate_tuple   0.185    86   
        predef_append    0.1739   81   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name             Secs     %    
        normal_append    0.194    100  
        generate_list    0.1828   94   
        generate_tuple   0.1795   93   
        predef_append    0.1543   80   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name             Secs     %    
        normal_append    0.193    100  
        generate_tuple   0.1881   98   
        generate_list    0.1831   95   
        predef_append    0.1507   78   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name             Secs     %    
        normal_append    0.2921   100  
        generate_list    0.2826   97   
        predef_append    0.2542   87   
        generate_tuple   0.2484   85   
        
    Python312:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name             Secs     %    
        generate_list    0.2821   100  
        generate_tuple   0.2596   92   
        predef_append    0.1985   70   
        normal_append    0.181    64   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name             Secs     %    
        generate_list    0.3033   100  
        predef_append    0.2432   80   
        normal_append    0.2244   74   
        generate_tuple   0.2231   74   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name             Secs     %    
        generate_list    0.226    100  
        generate_tuple   0.201    89   
        predef_append    0.1686   75   
        normal_append    0.1457   64   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name             Secs     %    
        generate_list    0.2037   100  
        generate_tuple   0.197    97   
        predef_append    0.1488   73   
        normal_append    0.1271   62   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name             Secs     %    
        generate_list    0.2096   100  
        generate_tuple   0.2033   97   
        predef_append    0.1557   74   
        normal_append    0.1331   63   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name             Secs     %    
        generate_list    0.3161   100  
        generate_tuple   0.2728   86   
        predef_append    0.2661   84   
        normal_append    0.2391   76   

"""