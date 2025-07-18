from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester

_strs_interned = {data.hun_chars_intern}
_strs_no_intern = {data.hun_chars_str}

num = data.M10

def in_interned(_strs_interned = _strs_interned):
    for _ in repeat(None, num):
        'dlahbflk_dflkhs_dfl_bflshb_qhb_flsdbf_lksbfel_bsfpiwb_fskdbj_vkcxzbviuwgsf_lkubsdkflab_osohfvmaskds' in _strs_interned

def in_no_intern(_strs_no_intern = _strs_no_intern):
    for _ in repeat(None, num):
        'dlahbflk/dflkhs/dfl/bflshb/qhb/flsdbf/lksbfel/bsfpiwb/fskdbj/vkcxzbviuwgsf/lkubsdkflab/osohfvmaskd/' in _strs_no_intern

auto_tester()


"""
Conclusion:
    Python27:
        Name           Secs     %    
        in_no_intern   0.2058   100  
        in_interned    0.1604   78    
        
    Python38:
        Name           Secs     %    
        in_no_intern   0.1733   100  
        in_interned    0.1256   73   

    Python310:
        Name           Secs     %    
        in_no_intern   0.1733   100  
        in_interned    0.1307   75   
        
    Python312:
        Name           Secs     %    
        in_no_intern   0.1455   100  
        in_interned    0.1109   76   
"""
