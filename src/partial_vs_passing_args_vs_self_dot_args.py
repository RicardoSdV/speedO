""" If a method uses many other methods within the class & is called very often
would there be efficiency gains to instead of doing self.other_meths() to call
pass them to the method in the form of a partial? """
from functools import partial
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M10

class Class(object):
    __slots__ = ('called_with_locals', )

    def __init__(self):
        self.called_with_locals = partial(
            self.called_for_partial, self.second_called1, self.second_called2, self.second_called3, self.second_called4
        )

    def caller_of_partial(self):
        called_with_locals = self.called_with_locals
        for _ in repeat(None, num):
            called_with_locals()

    def caller_of_meth_with_self_dot_access(self):
        called_and_self_dot_access = self.called_and_self_dot_access
        for _ in repeat(None, num):
            called_and_self_dot_access()

    @staticmethod
    def called_for_partial(meth1, meth2, meth3, meth4):
        meth1()
        meth2()
        meth3()
        meth4()

    def called_and_self_dot_access(self):
        self.second_called1()
        self.second_called2()
        self.second_called3()
        self.second_called4()

    def second_called1(self):
        return

    def second_called2(self):
        return

    def second_called3(self):
        return

    def second_called4(self):
        return


obj = Class()

tester(
    (
        obj.caller_of_meth_with_self_dot_access,
        obj.caller_of_partial,
    )
)

"""
Conclusion: 
    - The partial seems to be worth it in python27, otherwise not enough gain, 
    even detrimental in python312
    
    Python27:
        Testing times mean of 5 rounds: 
        Name                                  Secs     %    
        caller_of_meth_with_self_dot_access   1.721    100  
        caller_of_partial                     1.3252   77   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                                  Secs     %    
        caller_of_meth_with_self_dot_access   1.162    100  
        caller_of_partial                     1.1451   99   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                                  Secs     %    
        caller_of_meth_with_self_dot_access   1.361    100  
        caller_of_partial                     1.3124   96   
        
    Python312:
        Testing times mean of 5 rounds: 
        Name                                  Secs     %    
        caller_of_partial                     0.9892   100  
        caller_of_meth_with_self_dot_access   0.7974   81   

"""


