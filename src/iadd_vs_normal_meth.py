from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Example(object):
    def __init__(self):
        self.l = []
        self.append_to_l = self.l.append  # Needed for better measurements in older versions

    def __iadd__(self, el):
        self.append_to_l(el)
        return self

    def add(self, el):
        self.append_to_l(el)


num = data.M10

def call_iadd():
    example = Example()
    for _ in repeat(None, num):
        example += None

def call_meth():
    example = Example()
    for _ in repeat(None, num):
        example.add(num)


if __name__ == '__main__':
    tester(
        (
            call_iadd,
            call_meth,
        )
    )

    tester(
        (
            call_iadd,
            call_meth,
        ),
        testing_what='memories',
    )

"""
Conclusion:
    - iadd starts being worse, getts better in the middle, & ens up being worse too

    Python312:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        call_iadd   0.5374   100  
        call_meth   0.4315   80   
        
        Testing memories mean of 5 rounds: 
        Name        Mibs      %    
        call_iadd   66.3203   100  
        call_meth   62.6055   94  

    Python310:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        call_meth   0.6664   100  
        call_iadd   0.6053   91   
        
        Testing memories mean of 5 rounds: 
        Name        Mibs      %    
        call_meth   96.5508   100  
        call_iadd   67.9844   70   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        call_meth   0.5667   100  
        call_iadd   0.5365   95   

        Testing memories mean of 5 rounds: 
        Name        Mibs      %    
        call_meth   70.2266   100  
        call_iadd   62.4805   89   
        
    Python27:
        Testing times mean of 5 rounds: 
        Name        Secs     %    
        call_iadd   1.137    100  
        call_meth   0.8578   75   
        
        Testing memories mean of 5 rounds: 
        Name        Mibs      %    
        call_iadd   73.4648   100  
        call_meth   69.3203   94   
    
"""
