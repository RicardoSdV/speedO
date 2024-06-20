"""
If I want to make a list with list comprehension based on a complex condition which doesn't
fit in the standard list comprehension, is it better to use a generator or a creator
"""
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

k = data.k
k100 = data.k100
k_range = data.k_range


def creator(num):
    return num + 1


def generator():
    for i in k_range:
        yield i + 1


def using_creator():
    for _ in repeat(None, k100):
        result = [creator(i) for i in k_range]


def using_generator():
    for _ in repeat(None, k100):
        result = list(generator())


if __name__ == '__main__':
    tester(
        (
            using_creator,
            using_generator,
        ),
        testing_what='memories'
    )

    tester(
        (
            using_creator,
            using_generator,
        ),
        testing_what='times'
    )


"""
Conclusion:
    - In interpreted python generators get worse and creators better
    - In pypy JIT generators are very poorly optimized

    Python27:
        Testing memories average of 5 rounds: 
        Name              Mibs     %    
        using_creator     0.1734   100  
        using_generator   0.125    72   
        
        Testing times average of 5 rounds: 
        Name              Secs     %    
        using_creator     3.9394   100  
        using_generator   2.2968   57   
        
    Python38:
        Testing memories average of 5 rounds: 
        Name              Mibs     %    
        using_creator     0.2148   100  
        using_generator   0.1219   56   

        Testing times average of 5 rounds: 
        Name              Secs     %    
        using_creator     3.7236   100  
        using_generator   2.6188   70   
        
    Python312:
        Testing memories average of 5 rounds: 
        Name              Mibs     %    
        using_creator     0.0734   100  
        using_generator   0.0211   28   
        
        Testing times average of 5 rounds: 
        Name              Secs     %    
        using_creator     3.1907   100  
        using_generator   2.8827   90   
        
    Pypy313:
        Testing memories average of 5 rounds: 
        Name              Mibs      %    
        using_generator   13.0359   100  
        using_creator     1.7398    13   
        
        Testing times average of 5 rounds: 
        Name              Secs     %    
        using_generator   0.5231   100  
        using_creator     0.1251   24   


"""





