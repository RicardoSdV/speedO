from src.z_tester import auto_tester_2d

def list_comprehension_and_extend(outer):
    for inner in outer:
        l1 = []
        l1.extend([el for el in inner])

def gen_comprehension_and_extend(outer):
    for inner in outer:
        l1 = []
        l1.extend((el for el in inner))

def simple_append(outer):
    for inner in outer:
        l1 = []
        for el in inner:
            l1.append(el)

def predef_append(outer):
    for inner in outer:
        l1 = []
        l1_app = l1.append
        for el in inner:
            l1_app(el)

auto_tester_2d()

"""
Conclusion:
- The general trend seems that with very few elements append is faster, 
potentially due to the overhead of creating a new empty list just to extend 
another, and with a lot of elements 1 000 000 + append is also faster, 
possibly due to having to make and gc such a large list. Also generator 
comprehension sucks, so does simple append in older python, but we knew 
that already. Please see: extend_vs_append_to_list.py

    Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name                            Secs    %    
    gen_comprehension_and_extend    0.477   100  
    simple_append                   0.425   89   
    predef_append                   0.311   65   
    list_comprehension_and_extend   0.282   59   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name                            Secs     %    
    simple_append                   0.306    100  
    gen_comprehension_and_extend    0.2467   81   
    predef_append                   0.206    67   
    list_comprehension_and_extend   0.159    52   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name                            Secs     %    
    simple_append                   0.2817   100  
    gen_comprehension_and_extend    0.1863   66   
    predef_append                   0.168    60   
    list_comprehension_and_extend   0.1207   43   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name                            Secs     %    
    simple_append                   0.271    100  
    gen_comprehension_and_extend    0.172    63   
    predef_append                   0.1607   59   
    list_comprehension_and_extend   0.1137   42   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name                            Secs     %    
    simple_append                   0.262    100  
    gen_comprehension_and_extend    0.1667   64   
    predef_append                   0.157    60   
    list_comprehension_and_extend   0.112    43   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name                            Secs     %    
    simple_append                   0.4083   100  
    gen_comprehension_and_extend    0.3043   75   
    predef_append                   0.302    74   
    list_comprehension_and_extend   0.2943   72   

Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.2876   100  
    simple_append                   0.2205   77   
    list_comprehension_and_extend   0.1955   68   
    predef_append                   0.1821   63   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                            Secs     %    
    simple_append                   0.2112   100  
    gen_comprehension_and_extend    0.2006   95   
    predef_append                   0.1604   76   
    list_comprehension_and_extend   0.1053   50   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                            Secs     %    
    simple_append                   0.1936   100  
    gen_comprehension_and_extend    0.1761   91   
    predef_append                   0.1586   82   
    list_comprehension_and_extend   0.0973   50   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                            Secs     %    
    simple_append                   0.1911   100  
    gen_comprehension_and_extend    0.1628   85   
    predef_append                   0.1424   75   
    list_comprehension_and_extend   0.0886   46   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                            Secs     %    
    simple_append                   0.193    100  
    gen_comprehension_and_extend    0.1691   88   
    predef_append                   0.1481   77   
    list_comprehension_and_extend   0.0985   51   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                            Secs     %    
    simple_append                   0.3343   100  
    gen_comprehension_and_extend    0.3105   93   
    predef_append                   0.2874   86   
    list_comprehension_and_extend   0.2729   82   
    
Python314:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.3453   100  
    predef_append                   0.1866   54   
    simple_append                   0.1515   44   
    list_comprehension_and_extend   0.1427   41   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.2269   100  
    predef_append                   0.1731   76   
    simple_append                   0.1576   69   
    list_comprehension_and_extend   0.1259   56   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.1809   100  
    predef_append                   0.1388   77   
    simple_append                   0.1314   73   
    list_comprehension_and_extend   0.1003   55   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.177    100  
    predef_append                   0.1278   72   
    simple_append                   0.1242   70   
    list_comprehension_and_extend   0.1011   56   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.1778   100  
    predef_append                   0.1276   72   
    simple_append                   0.1265   71   
    list_comprehension_and_extend   0.1032   57   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                            Secs     %    
    gen_comprehension_and_extend    0.3104   100  
    list_comprehension_and_extend   0.2787   90   
    simple_append                   0.2639   85   
    predef_append                   0.2636   85   
"""
