"""
When a class defines an instance method & it calls other methods from within the class does it make sense to make
said called methods static? & classmethods? & private? etc
"""
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


class Cls(object):
    @staticmethod
    def called_pub_stat_meth(): return
    @classmethod
    def called_pub_cls_meth(cls): return
    def called_pub_ins_meth(self): return

    @staticmethod
    def __called_priv_stat_meth(): return
    @classmethod
    def __called_priv_cls_meth(cls): return
    def __called_priv_ins_meth(self): return

    def ins_meth_calls_pub_stat(self): self.called_pub_stat_meth()
    def ins_meth_calls_pub_cls(self): self.called_pub_cls_meth()
    def ins_meth_calls_pub_ins(self): self.called_pub_ins_meth()

    def ins_meth_calls_priv_stat(self): self.__called_priv_stat_meth()
    def ins_meth_calls_priv_cls(self): self.__called_priv_cls_meth()
    def ins_meth_calls_priv_ins(self): self.__called_priv_ins_meth()


obj = Cls()
M10 = data.M10


def ins_meth_calls_pub_stat():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_pub_stat()


def ins_meth_calls_pub_cls():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_pub_cls()


def ins_meth_calls_pub_ins():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_pub_ins()


def ins_meth_calls_priv_stat():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_priv_stat()


def ins_meth_calls_priv_cls():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_priv_cls()


def ins_meth_calls_priv_ins():
    for _ in repeat(None, M10):
        obj.ins_meth_calls_priv_ins()



if __name__ == '__main__':
    tester(
        (
            ins_meth_calls_pub_ins,
            ins_meth_calls_pub_stat,
            ins_meth_calls_pub_cls,
            ins_meth_calls_priv_ins,
            ins_meth_calls_priv_stat,
            ins_meth_calls_priv_cls,

        ),
        num_repeats=5,
    )

    tester(
        (
            ins_meth_calls_pub_ins,
            ins_meth_calls_pub_stat,
            ins_meth_calls_pub_cls,
            ins_meth_calls_priv_ins,
            ins_meth_calls_priv_stat,
            ins_meth_calls_priv_cls,

        ),
        testing_what='memories'
    )

"""
Conclusion:
    - Memory should not be an issue, unless maybe very long callstacks, should test that.
    - For Python27 not that much difference in speed, later versions optimized for instance methods
    - Private & public methods very similar performance.


    Python27:
    
        Testing times average of 5 rounds: 
        Name                       Secs     %    
        ins_meth_calls_priv_cls    0.7022   100  
        ins_meth_calls_pub_cls     0.6938   99   
        ins_meth_calls_pub_ins     0.6924   99   
        ins_meth_calls_priv_ins    0.6894   98   
        ins_meth_calls_pub_stat    0.677    96   
        ins_meth_calls_priv_stat   0.674    96   
        
        Testing memories average of 5 rounds: 
        Name                       Mibs     %    
        ins_meth_calls_pub_ins     0.0305   100  
        ins_meth_calls_pub_cls     0.0016   5    
        ins_meth_calls_priv_ins    0.0008   3    
        ins_meth_calls_priv_cls    0.0008   3    
        ins_meth_calls_pub_stat    0.0      0    
        ins_meth_calls_priv_stat   0.0      0    
        
    Python38:
    
        Testing times average of 5 rounds: 
        Name                       Secs     %    
        ins_meth_calls_pub_cls     0.5897   100  
        ins_meth_calls_priv_cls    0.5802   98   
        ins_meth_calls_priv_stat   0.5365   91   
        ins_meth_calls_pub_stat    0.5324   90   
        ins_meth_calls_pub_ins     0.5275   89   
        ins_meth_calls_priv_ins    0.5264   89   
        
        Testing memories average of 5 rounds: 
        Name                       Mibs     %    
        ins_meth_calls_pub_ins     0.0766   100  
        ins_meth_calls_priv_ins    0.0078   10   
        ins_meth_calls_pub_stat    0.0016   2    
        ins_meth_calls_pub_cls     0.0      0    
        ins_meth_calls_priv_stat   0.0      0    
        ins_meth_calls_priv_cls    0.0      0    
        
    Python312:
    
        Testing times average of 5 rounds: 
        Name                       Secs     %    
        ins_meth_calls_pub_cls     0.4843   100  
        ins_meth_calls_priv_cls    0.483    100  
        ins_meth_calls_pub_stat    0.3579   74   
        ins_meth_calls_priv_stat   0.3553   73   
        ins_meth_calls_pub_ins     0.3145   65   
        ins_meth_calls_priv_ins    0.3128   65   
        
        Testing memories average of 5 rounds: 
        Name                       Mibs     %    
        ins_meth_calls_pub_ins     0.0383   100  
        ins_meth_calls_pub_stat    0.0023   6    
        ins_meth_calls_pub_cls     0.0008   2    
        ins_meth_calls_priv_stat   0.0008   2    
        ins_meth_calls_priv_ins    0.0      0    
        ins_meth_calls_priv_cls    0.0      0 
        
    Pypy313:
        - Non conclusive, the scores vary wildly from run to run,
        might be getting optimized since its not doing any work
    
        Testing times average of 5 rounds: 
        Name                       Secs     %    
        ins_meth_calls_priv_ins    0.0063   100  
        ins_meth_calls_pub_ins     0.0061   97   
        ins_meth_calls_pub_cls     0.006    95   
        ins_meth_calls_pub_stat    0.0059   93   
        ins_meth_calls_priv_stat   0.0058   92   
        ins_meth_calls_priv_cls    0.0058   92   

        Testing memories average of 5 rounds: 
        Name                       Mibs     %    
        ins_meth_calls_priv_ins    0.1109   100  
        ins_meth_calls_priv_stat   0.0633   56   
        ins_meth_calls_pub_stat    0.0148   13   
        ins_meth_calls_priv_cls    0.0063   6    
        ins_meth_calls_pub_cls     0.0016   1    
        ins_meth_calls_pub_ins     0.0008   1    

"""

# end
