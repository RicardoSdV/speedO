from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Class(object):
    __slots__ = ('some_attr', )
    def __init__(self): self.some_attr = 1

    @staticmethod
    def static_meth_that_receives_attr(attr): return attr

    @staticmethod
    def static_meth_that_receives_10_attr(attr):
        for _ in repeat(None, 10):
            other = attr
        return other

    @staticmethod
    def static_meth_that_receives_100_attr(attr):
        for _ in repeat(None, 100):
            other = attr
        return other


    def meth_that_receives_attr(self, attr):
        return attr + 1

    def meth_that_receives_10_attr(self, attr):
        for _ in repeat(None, 10):
            other = attr
        return other

    def meth_that_receives_100_attr(self, attr):
        for _ in repeat(None, 100):
            other = attr
        return other


    def meth_that_accesses_attr(self):
        return self.some_attr + 1

    def meth_that_accesses_10_attr(self):
        for _ in repeat(None, 10):
            other = self.some_attr
        return other

    def meth_that_accesses_100_attr(self):
        for _ in repeat(None, 100):
            other = self.some_attr
        return other


    def meth_that_accesses_attr_10_local(self):
        attr = self.some_attr
        for _ in repeat(None, 10):
            other = attr
        return other

    def meth_that_accesses_attr_100_local(self):
        attr = self.some_attr
        for _ in repeat(None, 100):
            other = attr
        return other


    def call_meth_which_accesses_attr(self):
        self.meth_that_accesses_attr()

    def call_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.meth_that_receives_attr(local_attr)

    def call_static_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.static_meth_that_receives_attr(local_attr)


    def call_10_meth_which_accesses_attr(self):
        self.meth_that_accesses_10_attr()

    def call_10_meth_which_accesses_attr_local(self):
        self.meth_that_accesses_attr_10_local()

    def call_10_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.meth_that_receives_10_attr(local_attr)

    def call_10_static_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.static_meth_that_receives_10_attr(local_attr)


    def call_100_meth_which_accesses_attr(self):
        self.meth_that_accesses_100_attr()

    def call_100_meth_which_accesses_attr_local(self):
        self.meth_that_accesses_attr_100_local()

    def call_100_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.meth_that_receives_100_attr(local_attr)

    def call_100_static_meth_and_pass_attr(self):
        local_attr = self.some_attr
        self.static_meth_that_receives_100_attr(local_attr)


M10 = data.M10
M = data.M
obj = Class()

def call__call_meth_which_accesses_attr():
    for _ in repeat(None, M10):
        obj.call_meth_which_accesses_attr()

def call__call_meth_and_pass_attr():
    for _ in repeat(None, M10):
        obj.call_meth_and_pass_attr()

def call__call_static_meth_and_pass_attr():
    for _ in repeat(None, M10):
        obj.call_static_meth_and_pass_attr()


def call__call_10_meth_which_accesses_attr():
    for _ in repeat(None, M):
        obj.call_10_meth_which_accesses_attr()

def call__call_10_meth_which_accesses_attr_local():
    for _ in repeat(None, M):
        obj.call_10_meth_which_accesses_attr_local()

def call__call_10_meth_and_pass_attr():
    for _ in repeat(None, M):
        obj.call_10_meth_and_pass_attr()

def call__call_10_static_meth_and_pass_attr():
    for _ in repeat(None, M):
        obj.call_10_static_meth_and_pass_attr()


def call__call_100_meth_which_accesses_attr():
    for _ in repeat(None, M):
        obj.call_100_meth_which_accesses_attr()

def call__call_100_meth_which_accesses_attr_local():
    for _ in repeat(None, M):
        obj.call_100_meth_which_accesses_attr_local()

def call__call_100_meth_and_pass_attr():
    for _ in repeat(None, M):
        obj.call_100_meth_and_pass_attr()

def call__call_100_static_meth_and_pass_attr():
    for _ in repeat(None, M):
        obj.call_100_static_meth_and_pass_attr()


tester(
    (
        call__call_meth_which_accesses_attr,
        call__call_meth_and_pass_attr,
        call__call_static_meth_and_pass_attr,
    )
)

tester(
    (
        call__call_10_meth_which_accesses_attr,
        call__call_10_meth_which_accesses_attr_local,
        call__call_10_meth_and_pass_attr,
        call__call_10_static_meth_and_pass_attr,
    )
)

tester(
    (
        call__call_100_meth_which_accesses_attr,
        call__call_100_meth_which_accesses_attr_local,
        call__call_100_meth_and_pass_attr,
        call__call_100_static_meth_and_pass_attr,
    )
)

"""
Conclusion:
    Seems like if you're going to use an attribute within a loop you should declare it
    locally, what method is used does not seem to be too important, therefore, all methods
    should be instance methods, unless needed to be static or class methods to access them
    through the class object. Seems like it should be declared locally as close as possible
    to the loop, or place were its used multiple times.
    
    Probably applies to callables too?
    
    Python312:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        call__call_static_meth_and_pass_attr            0.4228   100  
        call__call_meth_and_pass_attr                   0.4024   95   
        call__call_meth_which_accesses_attr             0.3765   89   
        
        call__call_10_meth_which_accesses_attr          0.1663   100  
        call__call_10_static_meth_and_pass_attr         0.165    99   
        call__call_10_meth_and_pass_attr                0.1563   94   
        call__call_10_meth_which_accesses_attr_local    0.1548   93   
        
        call__call_100_meth_which_accesses_attr         0.8245   100  
        call__call_100_meth_which_accesses_attr_local   0.7315   89   
        call__call_100_meth_and_pass_attr               0.6965   84   
        call__call_100_static_meth_and_pass_attr        0.694    84   
        
    Python310:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        call__call_meth_and_pass_attr                   0.7782   100  
        call__call_static_meth_and_pass_attr            0.7422   95   
        call__call_meth_which_accesses_attr             0.7272   93   
 
        call__call_10_meth_which_accesses_attr          0.2552   100  
        call__call_10_meth_and_pass_attr                0.2008   79   
        call__call_10_static_meth_and_pass_attr         0.1871   73   
        call__call_10_meth_which_accesses_attr_local    0.1863   73   
 
        call__call_100_meth_which_accesses_attr         1.4098   100  
        call__call_100_meth_and_pass_attr               0.7829   56   
        call__call_100_meth_which_accesses_attr_local   0.7818   55   
        call__call_100_static_meth_and_pass_attr        0.7796   55   
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        call__call_meth_and_pass_attr                   0.6827   100  
        call__call_meth_which_accesses_attr             0.6528   96   
        call__call_static_meth_and_pass_attr            0.6391   94   
        
        call__call_10_meth_which_accesses_attr          0.234    100  
        call__call_10_static_meth_and_pass_attr         0.1746   75   
        call__call_10_meth_and_pass_attr                0.1707   73   
        call__call_10_meth_which_accesses_attr_local    0.17     73   
        
        call__call_100_meth_which_accesses_attr         1.2138   100  
        call__call_100_static_meth_and_pass_attr        0.6756   56   
        call__call_100_meth_and_pass_attr               0.6657   55   
        call__call_100_meth_which_accesses_attr_local   0.6594   54   
        
    Python27:
        Testing times mean of 5 rounds: 
        Name                                            Secs     %    
        call__call_meth_and_pass_attr                   1.0682   100  
        call__call_meth_which_accesses_attr             1.0076   94   
        call__call_static_meth_and_pass_attr            0.9922   93   

        call__call_10_meth_which_accesses_attr          0.3304   100  
        call__call_10_meth_and_pass_attr                0.2526   76   
        call__call_10_meth_which_accesses_attr_local    0.2488   75   
        call__call_10_static_meth_and_pass_attr         0.2454   74   

        call__call_100_meth_which_accesses_attr         1.7976   100  
        call__call_100_static_meth_and_pass_attr        0.8936   50   
        call__call_100_meth_which_accesses_attr_local   0.877    49   
        call__call_100_meth_and_pass_attr               0.867    48   

"""