"""
What types of methods are fastest to call?
What is the speed difference between the two main types of ways of calling them?
"""
from src.z_data import data
from z_tester import tester


def func():
    return


class TestClass:
    @staticmethod
    def static_method(): return

    @classmethod
    def class_method(cls): return

    def instance_method(self): return

    @property
    def prop(self): return


testObj = TestClass()


def class_dot_static():
    for _ in data.M10_repeat:
        TestClass.static_method()


def class_getattr_static():
    for _ in data.M10_repeat:
        getattr(TestClass, 'static_method')()


def class_dot_cls():
    for _ in data.M10_repeat:
        TestClass.class_method()


def class_getattr_cls():
    for _ in data.M10_repeat:
        getattr(TestClass, 'class_method')()


def obj_dot_static():
    for _ in data.M10_repeat:
        testObj.static_method()


def obj_getattr_static():
    for _ in data.M10_repeat:
        getattr(testObj, 'static_method')()


def obj_dot_cls():
    for _ in data.M10_repeat:
        testObj.class_method()


def obj_getattr_cls():
    for _ in data.M10_repeat:
        getattr(testObj, 'class_method')()


def obj_dot_ins():
    for _ in data.M10_repeat:
        testObj.instance_method()


def obj_getattr_ins():
    for _ in data.M10_repeat:
        getattr(testObj, 'instance_method')()


def obj_dot_prop():
    for _ in data.M10_repeat:
        testObj.prop


def obj_getattr_prop():
    for _ in data.M10_repeat:
        getattr(testObj, 'prop')


def func_for_comp():
    for _ in data.M10_repeat:
        func()


tester(
    (
        class_dot_static,
        class_dot_cls,
        obj_dot_static,
        obj_dot_cls,
        obj_dot_ins,
        obj_dot_prop,
        func_for_comp,
    )
)

tester(
    (
        class_getattr_static,
        class_getattr_cls,
        obj_getattr_static,
        obj_getattr_cls,
        obj_getattr_ins,
        obj_getattr_prop,
        func_for_comp,
    )
)

""" 
Conclusion: 
    - Generally getattr slower, but ratio of slowness stays constant, i.e. about 30% slower to use getattr more or less
    

    Python27:
        - Properties suck, almost twice as slow as instance methods, just used getters and setters
        - Everything else seems is kinda tied, static methods not bad, still functions better
    
        Name               Time     %    
        obj_dot_prop       0.6792   100  
        obj_dot_cls        0.4482   66   
        obj_dot_ins        0.444    65   
        obj_dot_static     0.4088   60   
        class_dot_cls      0.3832   56   
        class_dot_static   0.3486   51   
        func_for_comp      0.2606   38   
                
        Name                   Time     %    
        obj_getattr_prop       0.9222   100  
        obj_getattr_cls        0.717    78   
        obj_getattr_ins        0.709    77   
        obj_getattr_static     0.676    73   
        class_getattr_cls      0.6448   70   
        class_getattr_static   0.5996   65   
        func_for_comp          0.2608   28   


    Python38:
        - Theres not that much difference, except for class methods, avoid those. Properties still not great, but ok.
    
        Name               Time     %    
        class_dot_cls      0.336    100  
        obj_dot_cls        0.3338   99   
        obj_dot_prop       0.2948   88   
        obj_dot_static     0.2914   87   
        class_dot_static   0.2874   86   
        obj_dot_ins        0.2859   85   
        func_for_comp      0.2318   69    
                
        Name                   Time     %    
        obj_getattr_cls        0.4428   100  
        class_getattr_cls      0.4308   97   
        obj_getattr_ins        0.4306   97   
        obj_getattr_static     0.387    87   
        obj_getattr_prop       0.376    85   
        class_getattr_static   0.3708   84   
        func_for_comp          0.2303   52   


    Python312:
        - Properties great now, use instance methods, use functions everything else, bah, class methods keep sucking
    
        Name               Time     %    
        class_dot_cls      0.3492   100  
        obj_dot_cls        0.3401   97   
        class_dot_static   0.229    66   
        obj_dot_static     0.221    63   
        obj_dot_ins        0.1757   50   
        obj_dot_prop       0.1576   45   
        func_for_comp      0.1562   45  
        
        Name                   Time     %    
        obj_getattr_cls        0.3941   100  
        obj_getattr_ins        0.3906   99   
        class_getattr_cls      0.3856   98   
        obj_getattr_prop       0.3571   91   
        obj_getattr_static     0.2808   71   
        class_getattr_static   0.2704   69   
        func_for_comp          0.157    40   
"""
