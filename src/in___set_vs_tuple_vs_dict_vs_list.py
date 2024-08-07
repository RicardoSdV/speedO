""" When you just need to check weather or not something is in something else
 what datastructure should you use?? """
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

_tuple_2 = (1,2)
_tuple_4 = (1,2,3,4)
_tuple_8 = (1,2,3,4,5,6,7,8)
_tuple_16 = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)

_list_2 = [1,2]
_list_4 = [1,2,3,4]
_list_8 = [1,2,3,4,5,6,7,8]
_list_16 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

_set_2 = {1,2}
_set_4 = {1,2,3,4}
_set_8 = {1,2,3,4,5,6,7,8}
_set_16 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16}

_dict_2 = {1: None,2: None}
_dict_4 = {1: None,2: None,3: None,4: None}
_dict_8 = {1: None,2: None,3: None,4: None,5: None,6: None,7: None,8: None}
_dict_16 = {1: None,2: None,3: None,4: None,5: None,6: None,7: None,8: None,9: None,10: None,11: None,12: None,13: None,14: None,15: None,16: None}

num = data.M10


def in_tuple_of_2_first_el():
    struct = _tuple_2
    for _ in repeat(None, num):
        res = 1 in struct

def in_tuple_of_4_first_el():
    struct = _tuple_4
    for _ in repeat(None, num):
        res = 1 in struct

def in_tuple_of_8_first_el():
    struct = _tuple_8
    for _ in repeat(None, num):
        res = 1 in struct

def in_tuple_of_16_first_el():
    struct = _tuple_16
    for _ in repeat(None, num):
        res = 1 in struct

def in_tuple_of_2_last_el():
    struct = _tuple_2
    for _ in repeat(None, num):
        res = 2 in struct

def in_tuple_of_4_last_el():
    struct = _tuple_4
    for _ in repeat(None, num):
        res = 4 in struct

def in_tuple_of_8_last_el():
    struct = _tuple_8
    for _ in repeat(None, num):
        res = 8 in struct

def in_tuple_of_16_last_el():
    struct = _tuple_16
    for _ in repeat(None, num):
        res = 16 in struct

def in_tuple_of_2_is_not():
    struct = _tuple_2
    for _ in repeat(None, num):
        res = 3 in struct

def in_tuple_of_4_is_not():
    struct = _tuple_4
    for _ in repeat(None, num):
        res = 5 in struct

def in_tuple_of_8_is_not():
    struct = _tuple_8
    for _ in repeat(None, num):
        res = 9 in struct

def in_tuple_of_16_is_not():
    struct = _tuple_16
    for _ in repeat(None, num):
        res = 17 in struct


def in_list_of_2_first_el():
    struct = _list_2
    for _ in repeat(None, num):
        res = 1 in struct

def in_list_of_4_first_el():
    struct = _list_4
    for _ in repeat(None, num):
        res = 1 in struct

def in_list_of_8_first_el():
    struct = _list_8
    for _ in repeat(None, num):
        res = 1 in struct

def in_list_of_16_first_el():
    struct = _list_16
    for _ in repeat(None, num):
        res = 1 in struct

def in_list_of_2_last_el():
    struct = _list_2
    for _ in repeat(None, num):
        res = 2 in struct

def in_list_of_4_last_el():
    struct = _list_4
    for _ in repeat(None, num):
        res = 4 in struct

def in_list_of_8_last_el():
    struct = _list_8
    for _ in repeat(None, num):
        res = 8 in struct

def in_list_of_16_last_el():
    struct = _list_16
    for _ in repeat(None, num):
        res = 16 in struct

def in_list_of_2_is_not():
    struct = _list_2
    for _ in repeat(None, num):
        res = 3 in struct

def in_list_of_4_is_not():
    struct = _list_4
    for _ in repeat(None, num):
        res = 5 in struct

def in_list_of_8_is_not():
    struct = _list_8
    for _ in repeat(None, num):
        res = 9 in struct

def in_list_of_16_is_not():
    struct = _list_16
    for _ in repeat(None, num):
        res = 17 in struct


def in_set_of_2_first_el():
    struct = _set_2
    for _ in repeat(None, num):
        res = 1 in struct

def in_set_of_4_first_el():
    struct = _set_4
    for _ in repeat(None, num):
        res = 1 in struct

def in_set_of_8_first_el():
    struct = _set_8
    for _ in repeat(None, num):
        res = 1 in struct

def in_set_of_16_first_el():
    struct = _set_16
    for _ in repeat(None, num):
        res = 1 in struct

def in_set_of_2_last_el():
    struct = _set_2
    for _ in repeat(None, num):
        res = 2 in struct

def in_set_of_4_last_el():
    struct = _set_4
    for _ in repeat(None, num):
        res = 4 in struct

def in_set_of_8_last_el():
    struct = _set_8
    for _ in repeat(None, num):
        res = 8 in struct

def in_set_of_16_last_el():
    struct = _set_16
    for _ in repeat(None, num):
        res = 16 in struct

def in_set_of_2_is_not():
    struct = _set_2
    for _ in repeat(None, num):
        res = 3 in struct

def in_set_of_4_is_not():
    struct = _set_4
    for _ in repeat(None, num):
        res = 5 in struct

def in_set_of_8_is_not():
    struct = _set_8
    for _ in repeat(None, num):
        res = 9 in struct

def in_set_of_16_is_not():
    struct = _set_16
    for _ in repeat(None, num):
        res = 17 in struct


def in_dict_of_2_first_el():
    struct = _dict_2
    for _ in repeat(None, num):
        res = 1 in struct

def in_dict_of_4_first_el():
    struct = _dict_4
    for _ in repeat(None, num):
        res = 1 in struct

def in_dict_of_8_first_el():
    struct = _dict_8
    for _ in repeat(None, num):
        res = 1 in struct

def in_dict_of_16_first_el():
    struct = _dict_16
    for _ in repeat(None, num):
        res = 1 in struct

def in_dict_of_2_last_el():
    struct = _dict_2
    for _ in repeat(None, num):
        res = 2 in struct

def in_dict_of_4_last_el():
    struct = _dict_4
    for _ in repeat(None, num):
        res = 4 in struct

def in_dict_of_8_last_el():
    struct = _dict_8
    for _ in repeat(None, num):
        res = 8 in struct

def in_dict_of_16_last_el():
    struct = _dict_16
    for _ in repeat(None, num):
        res = 16 in struct

def in_dict_of_2_is_not():
    struct = _dict_2
    for _ in repeat(None, num):
        res = 3 in struct

def in_dict_of_4_is_not():
    struct = _dict_4
    for _ in repeat(None, num):
        res = 5 in struct

def in_dict_of_8_is_not():
    struct = _dict_8
    for _ in repeat(None, num):
        res = 9 in struct

def in_dict_of_16_is_not():
    struct = _dict_16
    for _ in repeat(None, num):
        res = 17 in struct

tester(
    (
        in_tuple_of_2_first_el,
        in_tuple_of_4_first_el,
        in_tuple_of_8_first_el,
        in_tuple_of_16_first_el,
        in_list_of_2_first_el,
        in_list_of_4_first_el,
        in_list_of_8_first_el,
        in_list_of_16_first_el,
        in_set_of_2_first_el,
        in_set_of_4_first_el,
        in_set_of_8_first_el,
        in_set_of_16_first_el,
        in_dict_of_2_first_el,
        in_dict_of_4_first_el,
        in_dict_of_8_first_el,
        in_dict_of_16_first_el,
    )
)

tester(
    (
        in_tuple_of_2_last_el,
        in_tuple_of_4_last_el,
        in_tuple_of_8_last_el,
        in_tuple_of_16_last_el,
        in_list_of_2_last_el,
        in_list_of_4_last_el,
        in_list_of_8_last_el,
        in_list_of_16_last_el,
        in_set_of_2_last_el,
        in_set_of_4_last_el,
        in_set_of_8_last_el,
        in_set_of_16_last_el,
        in_dict_of_2_last_el,
        in_dict_of_4_last_el,
        in_dict_of_8_last_el,
        in_dict_of_16_last_el,
    ),
    print_rounds=False
)

tester(
    (
        in_tuple_of_2_is_not,
        in_tuple_of_4_is_not,
        in_tuple_of_8_is_not,
        in_tuple_of_16_is_not,
        in_list_of_2_is_not,
        in_list_of_4_is_not,
        in_list_of_8_is_not,
        in_list_of_16_is_not,
        in_set_of_2_is_not,
        in_set_of_4_is_not,
        in_set_of_8_is_not,
        in_set_of_16_is_not,
        in_dict_of_2_is_not,
        in_dict_of_4_is_not,
        in_dict_of_8_is_not,
        in_dict_of_16_is_not,
    ),
    print_rounds=False,
)

"""
Conclusion:
        - If very sure most of the time searched for element is in the
        first couple elements, then tuple.
        
        - If you dont know, or el not likely to be in initial elements, 
        or not likely to be in there at all, probably go for set, even
        is sometimes very slightly slower
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        in_set_of_8_first_el      0.1518   100  
        in_set_of_2_first_el      0.1506   99   
        in_set_of_4_first_el      0.1504   99   
        in_set_of_16_first_el     0.1504   99   
        in_dict_of_4_first_el     0.1424   94   
        in_dict_of_2_first_el     0.1424   94   
        in_dict_of_8_first_el     0.1422   94   
        in_dict_of_16_first_el    0.142    94   
        in_list_of_16_first_el    0.1212   80   
        in_tuple_of_8_first_el    0.1212   80   
        in_list_of_4_first_el     0.1208   80   
        in_list_of_2_first_el     0.1208   80   
        in_list_of_8_first_el     0.1208   80   
        in_tuple_of_2_first_el    0.1204   79   
        in_tuple_of_16_first_el   0.12     79   
        in_tuple_of_4_first_el    0.119    78   
        
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        in_list_of_16_last_el    1.0012   100  
        in_tuple_of_16_last_el   0.8888   89   
        in_list_of_8_last_el     0.5134   51   
        in_tuple_of_8_last_el    0.4644   46   
        in_list_of_4_last_el     0.2994   30   
        in_tuple_of_4_last_el    0.2716   27   
        in_list_of_2_last_el     0.1828   18   
        in_tuple_of_2_last_el    0.1714   17   
        in_set_of_16_last_el     0.1506   15   
        in_set_of_2_last_el      0.15     15   
        in_set_of_4_last_el      0.15     15   
        in_set_of_8_last_el      0.1496   15   
        in_dict_of_2_last_el     0.1436   14   
        in_dict_of_8_last_el     0.143    14   
        in_dict_of_4_last_el     0.1426   14   
        in_dict_of_16_last_el    0.1424   14   
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        in_list_of_16_is_not    1.0696   100  
        in_tuple_of_16_is_not   0.9402   88   
        in_list_of_8_is_not     0.5786   54   
        in_tuple_of_8_is_not    0.526    49   
        in_list_of_4_is_not     0.3564   33   
        in_tuple_of_4_is_not    0.3222   30   
        in_list_of_2_is_not     0.2436   23   
        in_tuple_of_2_is_not    0.2218   21   
        in_set_of_16_is_not     0.1536   14   
        in_set_of_4_is_not      0.1534   14   
        in_set_of_2_is_not      0.1528   14   
        in_set_of_8_is_not      0.1526   14   
        in_dict_of_16_is_not    0.145    14   
        in_dict_of_4_is_not     0.1436   13   
        in_dict_of_2_is_not     0.1434   13   
        in_dict_of_8_is_not     0.1432   13   
    
    Python38:
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        in_dict_of_8_first_el     0.1273   100  
        in_dict_of_2_first_el     0.1266   99   
        in_dict_of_16_first_el    0.1254   99   
        in_dict_of_4_first_el     0.1252   98   
        in_set_of_8_first_el      0.1216   96   
        in_set_of_16_first_el     0.1214   95   
        in_set_of_4_first_el      0.1214   95   
        in_set_of_2_first_el      0.121    95   
        in_tuple_of_4_first_el    0.1125   88   
        in_list_of_16_first_el    0.1119   88   
        in_list_of_8_first_el     0.1119   88   
        in_tuple_of_8_first_el    0.1118   88   
        in_tuple_of_2_first_el    0.1115   88   
        in_tuple_of_16_first_el   0.1114   88   
        in_list_of_2_first_el     0.1111   87   
        in_list_of_4_first_el     0.1108   87   
        
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        in_tuple_of_16_last_el   0.7785   100  
        in_list_of_16_last_el    0.7616   98   
        in_tuple_of_8_last_el    0.4229   54   
        in_list_of_8_last_el     0.4081   52   
        in_tuple_of_4_last_el    0.2494   32   
        in_list_of_4_last_el     0.2378   31   
        in_tuple_of_2_last_el    0.1582   20   
        in_list_of_2_last_el     0.1533   20   
        in_dict_of_4_last_el     0.1269   16   
        in_dict_of_16_last_el    0.1248   16   
        in_dict_of_2_last_el     0.1243   16   
        in_dict_of_8_last_el     0.1235   16   
        in_set_of_2_last_el      0.1212   16   
        in_set_of_16_last_el     0.1204   15   
        in_set_of_8_last_el      0.1203   15   
        in_set_of_4_last_el      0.1199   15   
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        in_tuple_of_16_is_not   0.8887   100  
        in_list_of_16_is_not    0.8759   99   
        in_tuple_of_8_is_not    0.4668   53   
        in_list_of_8_is_not     0.4485   50   
        in_tuple_of_4_is_not    0.2906   33   
        in_list_of_4_is_not     0.276    31   
        in_set_of_2_is_not      0.2499   28   
        in_tuple_of_2_is_not    0.2036   23   
        in_list_of_2_is_not     0.1959   22   
        in_dict_of_4_is_not     0.1288   14   
        in_dict_of_8_is_not     0.1272   14   
        in_dict_of_16_is_not    0.1269   14   
        in_dict_of_2_is_not     0.1269   14   
        in_set_of_16_is_not     0.1238   14   
        in_set_of_4_is_not      0.1229   14   
        in_set_of_8_is_not      0.1228   14   
    
    Python310:
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        in_dict_of_16_first_el    0.1335   100  
        in_dict_of_8_first_el     0.1335   100  
        in_dict_of_2_first_el     0.1333   100  
        in_dict_of_4_first_el     0.133    100  
        in_set_of_2_first_el      0.12     90   
        in_set_of_16_first_el     0.1197   90   
        in_set_of_4_first_el      0.1197   90   
        in_set_of_8_first_el      0.1195   89   
        in_tuple_of_4_first_el    0.1157   87   
        in_list_of_4_first_el     0.1152   86   
        in_tuple_of_8_first_el    0.1152   86   
        in_list_of_8_first_el     0.1149   86   
        in_tuple_of_2_first_el    0.1148   86   
        in_tuple_of_16_first_el   0.1148   86   
        in_list_of_16_first_el    0.1146   86   
        in_list_of_2_first_el     0.1143   86   
        
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        in_list_of_16_last_el    0.7206   100  
        in_tuple_of_16_last_el   0.7114   99   
        in_list_of_8_last_el     0.4327   60   
        in_tuple_of_8_last_el    0.4052   56   
        in_list_of_4_last_el     0.2148   30   
        in_tuple_of_4_last_el    0.2037   28   
        in_list_of_2_last_el     0.1441   20   
        in_tuple_of_2_last_el    0.138    19   
        in_dict_of_8_last_el     0.1335   19   
        in_dict_of_2_last_el     0.1329   18   
        in_dict_of_4_last_el     0.1328   18   
        in_dict_of_16_last_el    0.1326   18   
        in_set_of_2_last_el      0.1204   17   
        in_set_of_4_last_el      0.1199   17   
        in_set_of_16_last_el     0.1192   17   
        in_set_of_8_last_el      0.1186   16   
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        in_list_of_16_is_not    0.7489   100  
        in_tuple_of_16_is_not   0.7451   99   
        in_list_of_8_is_not     0.4474   60   
        in_tuple_of_8_is_not    0.4336   57   
        in_list_of_4_is_not     0.2409   32   
        in_tuple_of_4_is_not    0.236    32   
        in_list_of_2_is_not     0.1711   23   
        in_tuple_of_2_is_not    0.1701   23   
        in_dict_of_8_is_not     0.1329   18   
        in_dict_of_2_is_not     0.1322   18   
        in_dict_of_16_is_not    0.1318   18   
        in_dict_of_4_is_not     0.1315   18   
        in_set_of_16_is_not     0.1201   16   
        in_set_of_2_is_not      0.1196   16   
        in_set_of_4_is_not      0.1195   16   
        in_set_of_8_is_not      0.1194   16   
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                      Secs     %    
        in_set_of_8_first_el      0.1119   100  
        in_set_of_2_first_el      0.1114   100  
        in_set_of_16_first_el     0.1112   99   
        in_set_of_4_first_el      0.111    99   
        in_dict_of_2_first_el     0.1096   98   
        in_dict_of_4_first_el     0.1094   98   
        in_dict_of_16_first_el    0.109    97   
        in_dict_of_8_first_el     0.1082   97   
        in_list_of_4_first_el     0.1043   93   
        in_list_of_2_first_el     0.1042   93   
        in_list_of_8_first_el     0.1037   93   
        in_list_of_16_first_el    0.1035   93   
        in_tuple_of_8_first_el    0.0981   88   
        in_tuple_of_16_first_el   0.0978   87   
        in_tuple_of_2_first_el    0.0974   87   
        in_tuple_of_4_first_el    0.0972   87   
        
        Testing times mean of 5 rounds: 
        Name                     Secs     %    
        in_tuple_of_16_last_el   0.5965   100  
        in_list_of_16_last_el    0.4866   82   
        in_tuple_of_8_last_el    0.3229   54   
        in_list_of_8_last_el     0.2797   47   
        in_tuple_of_4_last_el    0.188    32   
        in_list_of_4_last_el     0.1813   30   
        in_list_of_2_last_el     0.1373   23   
        in_tuple_of_2_last_el    0.1271   21   
        in_set_of_2_last_el      0.111    19   
        in_set_of_4_last_el      0.1107   19   
        in_set_of_8_last_el      0.1104   19   
        in_set_of_16_last_el     0.1095   18   
        in_dict_of_4_last_el     0.1091   18   
        in_dict_of_8_last_el     0.1089   18   
        in_dict_of_16_last_el    0.1088   18   
        in_dict_of_2_last_el     0.1088   18   
        
        Testing times mean of 5 rounds: 
        Name                    Secs     %    
        in_tuple_of_16_is_not   0.626    100  
        in_list_of_16_is_not    0.5102   82   
        in_tuple_of_8_is_not    0.3546   56   
        in_list_of_8_is_not     0.2994   48   
        in_tuple_of_4_is_not    0.2207   35   
        in_list_of_4_is_not     0.1964   31   
        in_tuple_of_2_is_not    0.155    25   
        in_list_of_2_is_not     0.1483   24   
        in_dict_of_16_is_not    0.1132   18   
        in_set_of_4_is_not      0.1113   18   
        in_set_of_16_is_not     0.1108   18   
        in_set_of_8_is_not      0.1108   18   
        in_set_of_2_is_not      0.1101   18   
        in_dict_of_4_is_not     0.1089   17   
        in_dict_of_8_is_not     0.1084   17   
        in_dict_of_2_is_not     0.1082   17   

"""

