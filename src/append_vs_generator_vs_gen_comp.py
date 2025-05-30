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

def _gen_comp(_list):
    return (i for i in _list)

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

def gen_comp_list(list_2d, cal=_gen_comp):
    for inner in list_2d:
        list(cal(inner))

def gen_comp_tuple(list_2d, cal=_gen_comp):
    for inner in list_2d:
        tuple(cal(inner))

tester_2d(
    (
        normal_append,
        predef_append,
        generate_list,
        generate_tuple,
        gen_comp_list,
        gen_comp_tuple,
    ),
)


"""
Conclusion:
    - If you're going to create a generator to immediately consume it into a list or a tuple
    it makes more sense to use a predefined append or a normal append in python312.
    Unless the list is massive, > 100 000, then generate a tuple.
    
    - However, it remains a question if it still makes sense to use a generator when the only purpose
    is to iterate over it once in some other loop, the entire premise of this test is that
    you do want a sequence after calling the generator.
    
    - Also, keeps proving how bad the normal append is until 312
    
    Python27:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name             Secs     %    
        gen_comp_list    0.5147   100  
        gen_comp_tuple   0.469    91   
        generate_list    0.4667   91   
        normal_append    0.4593   89   
        generate_tuple   0.4247   83   
        predef_append    0.3483   68   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name             Secs     %    
        normal_append    0.3107   100  
        gen_comp_list    0.2503   81   
        generate_list    0.244    79   
        gen_comp_tuple   0.2397   77   
        generate_tuple   0.233    75   
        predef_append    0.2097   67   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name             Secs     %    
        normal_append    0.2683   100  
        gen_comp_tuple   0.19     71   
        gen_comp_list    0.1887   70   
        generate_list    0.186    69   
        generate_tuple   0.185    69   
        predef_append    0.1693   63   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name             Secs     %    
        normal_append    0.257    100  
        generate_tuple   0.1783   69   
        gen_comp_tuple   0.1763   69   
        gen_comp_list    0.1733   67   
        generate_list    0.1697   66   
        predef_append    0.1603   62   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name             Secs     %    
        normal_append    0.246    100  
        gen_comp_tuple   0.17     69   
        generate_tuple   0.168    68   
        gen_comp_list    0.162    66   
        generate_list    0.1593   65   
        predef_append    0.151    61   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name             Secs     %    
        normal_append    0.364    100  
        generate_list    0.2747   75   
        gen_comp_list    0.2733   75   
        predef_append    0.2677   74   
        generate_tuple   0.237    65   
        gen_comp_tuple   0.2357   65   
        
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