"""
When you have a one or more maybe nested for loops with complex logic inside, is it best
to split the mess into normal functions and call those or use generators? other methods are
present for comparison, obviously you cant do complex loops with list comprehension for example,
but how much faster is it?
"""
from src.z_tester import tester_2d

def creator(num):
    return num


def generator(inner_list):
    for i in inner_list:
        yield i


def using_creator(list_2d):
    for inner_list in list_2d:
        result = [creator(i) for i in inner_list]

def using_generator(list_2d):
    for inner_list in list_2d:
        result = list(generator(inner_list))

def normal_append(list_2d):
    for inner_list in list_2d:
        result = []
        for i in inner_list:
            result.append(i)

def predef_append(list_2d):
    for inner_list in list_2d:
        result = []
        append_to_res = result.append

        for i in inner_list:
            append_to_res(i)

def list_comprehension(list_2d):
    """ List comprehension cant be used when the conditions are complex but let's compare """
    for inner_list in list_2d:
        result = [i for i in inner_list]



if __name__ == '__main__':
    tester_2d(
        (
            using_creator,
            using_generator,
            normal_append,
            predef_append,
            list_comprehension,

        ),
        testing_what='memories'
    )

    tester_2d(
        (
            using_creator,
            using_generator,
            normal_append,
            predef_append,
            list_comprehension,
        ),
        testing_what='times'
    )

"""
Python27:

    Testing memories:
    
    Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
    Name                 Mibs     %    
    using_creator        0.0339   100  
    using_generator      0.0      0    
    normal_append        0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
    Name                 Mibs     %    
    normal_append        0.0026   100  
    using_creator        0.0      0    
    using_generator      0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
    Name                 Mibs     %    
    using_generator      0.1445   100  
    using_creator        0.1068   74   
    normal_append        0.0378   26   
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
    Name                 Mibs     %    
    using_creator        0.0859   100  
    normal_append        0.0326   38   
    using_generator      0.0195   23   
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
    Name                 Mibs     %    
    using_creator        0.7109   100  
    normal_append        0.0846   12   
    using_generator      0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
    Name                 Mibs      %    
    list_comprehension   16.1706   100  
    using_generator      13.4779   83   
    using_creator        13.4232   83   
    predef_append        6.9948    43   
    normal_append        4.7669    28   
    
    
    Testing times:
    
    Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
    Name                 Secs     %    
    using_creator        0.5143   100  
    using_generator      0.4553   89   
    normal_append        0.4133   80   
    predef_append        0.2963   57   
    list_comprehension   0.212    41   
    
    Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
    Name                 Secs     %    
    using_creator        0.3817   100  
    normal_append        0.304    80   
    using_generator      0.237    62   
    predef_append        0.1987   52   
    list_comprehension   0.1347   35   
    
    Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
    Name                 Secs     %    
    using_creator        0.35     100  
    normal_append        0.267    76   
    using_generator      0.185    53   
    predef_append        0.1683   48   
    list_comprehension   0.1047   30   
    
    Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
    Name                 Secs     %    
    using_creator        0.3427   100  
    normal_append        0.258    75   
    using_generator      0.179    52   
    predef_append        0.162    47   
    list_comprehension   0.1057   31   
    
    Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
    Name                 Secs     %    
    using_creator        0.3237   100  
    normal_append        0.2483   77   
    using_generator      0.1643   51   
    predef_append        0.15     46   
    list_comprehension   0.095    28   
    
    Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
    Name                 Secs     %    
    using_creator        0.4237   100  
    normal_append        0.3407   80   
    using_generator      0.2603   61   
    predef_append        0.248    59   
    list_comprehension   0.193    46   
    
    
Python310:
    Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
    Name                 Mibs     %    
    using_creator        0.1081   100  
    using_generator      0.0013   1    
    normal_append        0.0013   1    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
    Name                 Mibs     %    
    normal_append        0.0078   100  
    using_creator        0.0      0    
    using_generator      0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
    Name                 Mibs     %    
    using_creator        0.0729   100  
    using_generator      0.0      0    
    normal_append        0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
    Name                 Mibs     %    
    using_generator      0.1471   100  
    using_creator        0.125    85   
    normal_append        0.0521   35   
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
    Name                 Mibs     %    
    using_creator        0.9193   100  
    using_generator      0.0      0    
    normal_append        0.0      0    
    predef_append        0.0      0    
    list_comprehension   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
    Name                 Mibs      %    
    list_comprehension   19.8177   100  
    using_creator        16.1628   82   
    using_generator      16.0      81   
    predef_append        7.8503    40   
    normal_append        5.8411    28   
    
    
    Testing times:
    
    Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 10: 
    Name                 Secs     %    
    using_creator        0.4257   100  
    using_generator      0.3057   72   
    normal_append        0.2115   50   
    predef_append        0.1911   45   
    list_comprehension   0.1752   41   
    
    Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 100: 
    Name                 Secs     %    
    using_creator        0.3394   100  
    using_generator      0.2139   63   
    normal_append        0.2124   63   
    predef_append        0.1739   51   
    list_comprehension   0.1103   33   
    
    Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 1 000: 
    Name                 Secs     %    
    using_creator        0.3262   100  
    normal_append        0.1988   61   
    using_generator      0.1933   59   
    predef_append        0.1553   48   
    list_comprehension   0.0984   30   
    
    Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 10 000: 
    Name                 Secs     %    
    using_creator        0.3135   100  
    normal_append        0.1905   61   
    using_generator      0.1868   60   
    predef_append        0.1496   48   
    list_comprehension   0.0887   28   
    
    Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 100 000: 
    Name                 Secs     %    
    using_creator        0.3144   100  
    normal_append        0.1942   62   
    using_generator      0.1892   60   
    predef_append        0.1507   48   
    list_comprehension   0.0929   30   
    
    Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 1 000 000: 
    Name                 Secs     %    
    using_creator        0.4197   100  
    normal_append        0.3015   72   
    using_generator      0.296    71   
    predef_append        0.255    61   
    list_comprehension   0.1968   47   
    
"""

