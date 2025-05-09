"""
Obviously using startswith is safer but when using absolute paths it is very difficult for in to fail
so in that case is there any significant advantage to using in over startswith??
"""
import re
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

num = data.M

path = 'myDir1\\myDir2\\myDir3\\myDir4\\myDir5\\myDir6\\file.py'
other = 'myDir7\\myDir8\\myDir9\\myDir10\\myDir11\\myDir12\\file.py'
subPath = 'myDir1\\myDir2\\myDir3'
_match = re.compile(r'^myDir1\\myDir2\\myDir3').match

def starts_with(path=path, subPath=subPath, other=other):
    for _ in repeat(None, num):
        path.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)
        other.startswith(subPath)

def use_in(path=path, subPath=subPath, other=other):
    for _ in repeat(None, num):
        subPath in path
        other in path
        other in path
        other in path
        other in path
        other in path
        other in path
        other in path
        other in path

def regex(subPath=subPath, other=other, match=_match):
    for _ in repeat(None, num):
        match(subPath)
        match(other)
        match(other)
        match(other)
        match(other)
        match(other)
        match(other)
        match(other)
        match(other)

auto_tester()

"""
Conclusion:
    - Regex slow
    - in about 3 - 5 times faster.
    
    Python27:
        Name          Secs     %    
        regex         1.109    100  
        starts_with   0.5432   49   
        use_in        0.1284   12  
        
    Python38:
        Name          Secs     %    
        regex         0.9576   100  
        starts_with   0.4147   43   
        use_in        0.1022   11   
    
    Python310:
        Name          Secs     %    
        regex         1.2066   100  
        starts_with   0.4132   34   
        use_in        0.1135   9    
        
    Python312:
        Name          Secs     %    
        regex         0.9621   100  
        starts_with   0.3738   39   
        use_in        0.0834   9    
"""
