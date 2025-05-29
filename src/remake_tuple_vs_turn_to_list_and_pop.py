from src.z_data import list_of_tuples_of_rand_ints, data
from src.z_tester import auto_tester


tuples = list_of_tuples_of_rand_ints(data.M)


def make_new():
    for el in tuples:
        a, b, c, d, e, f, g, h = el
        new = (a, b, c, d, e, f, g)

def to_list():
    for el in tuples:
        el = list(el)
        h = el.pop()


auto_tester()


"""
Conclusion:
Just make a new tuple

Python27:
Name       Secs     %    
to_list    0.144    100  
make_new   0.0508   35  
    
Python38:
Name       Secs     %    
to_list    0.0588   100  
make_new   0.0441   75  

Python310:
Name       Secs     %    
to_list    0.0557   100  
make_new   0.0469   84   

Python312:
Name       Secs     %    
to_list    0.0484   100  
make_new   0.0389   80   

"""
