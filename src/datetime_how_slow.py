"""
Is it worth it to have an inaccurate global datetime object & reference it or is the hazzle
not worth it?

"""
import sys
from copy import copy
from datetime import datetime
from itertools import repeat

from src.z_data import data
from src.z_tester import tester


num = data.M10
_now = datetime.utcnow()


if sys.version_info >= (3, 12):
    from datetime import UTC
    def call_now():
        for _ in repeat(None, num):
            local_now = datetime.now(UTC)
else:
    # This works in 312 but its dog slow
    def call_now():
        for _ in repeat(None, num):
            local_now = datetime.utcnow()


if sys.version >= (3, ):
    from datetime import timezone
    utc = timezone.utc

    def call_now_pass_utc():
        for _ in repeat(None, num):
            local_now = datetime.now(utc)
else:
    import pytz
    utc = pytz.utc

    def call_now_pass_utc():
        for _ in repeat(None, num):
            local_now = datetime.now(utc)

def global_now():
    for _ in repeat(None, num):
        local_now = _now

def copy_of_global_now():
    for _ in repeat(None, num):
        local_now = copy(global_now)

if __name__ == '__main__':
    tester(
        (
            call_now,
            call_now_pass_utc,
            global_now,
            copy_of_global_now,
        )
    )


"""
Conclusion:
    Clearly, in any version, using a global now is about six times faster than recalculating
    now. If the accuracy & complexity tradeoff is worth it then it probably should be done,
    even though, in a real situation the reference to the global now probably needs to be imported
    into a bunch of places.
    
    And since its an immutable object the copy thing doesn't really make sense

    Python312:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_now             1.0107   100  
        call_now_pass_utc    0.9963   99   
        copy_of_global_now   0.5335   53   
        global_now           0.0778   8 

    Python310:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_now_pass_utc    1.2684   100  
        copy_of_global_now   0.8397   66   
        call_now             0.5935   47   
        global_now           0.1016   8     
        
    Python38:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_now_pass_utc    1.0332   100  
        copy_of_global_now   0.8345   81   
        call_now             0.4937   48   
        global_now           0.0732   7    
        
    Python27:
        Testing times mean of 5 rounds: 
        Name                 Secs     %    
        call_now_pass_utc    8.5386   100  
        call_now             2.7264   32   
        copy_of_global_now   1.3596   16   
        global_now           0.0818   1    
    
"""


