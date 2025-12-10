import sys
from itertools import repeat

from src.z_data import data
from src.z_tester import auto_tester


binFlags = [2**i for i in range(31)]
binMaskLong = (1 << 31) - 1  # All the bits in a 32 bit signed int.
binMaskShort = 1 # It could be all 32 bits but what if its only the first?
num = data.M



if not sys.version.startswith('2.7') and not sys.version.startswith('3.8'):
    def use_bit_count_long(binMask=binMaskLong):
        for _ in repeat(None, num):
            cnt = binMask.bit_count()

    def use_bit_count_short(binMask=binMaskShort):
        for _ in repeat(None, num):
            cnt = binMask.bit_count()


def iter_counter_long(binMask=binMaskLong):
    for _ in repeat(None, num):
        cnt = 0
        for flag in binFlags:
            if flag & binMask:
                cnt += 1

def iter_counter_short(binMask=binMaskShort):
    for _ in repeat(None, num):
        cnt = 0
        for flag in binFlags:
            if flag & binMask:
                cnt += 1


def to_bin_and_count_long(bin=bin, binMask=binMaskLong):
    for _ in repeat(None, num):
        cnt = bin(binMask).count('1')

def to_bin_and_count_short(bin=bin, binMask=binMaskShort):
    for _ in repeat(None, num):
        cnt = bin(binMask).count('1')


def kernighan_shift_long(binMask=binMaskLong):
    for _ in repeat(None, num):
        cnt = 0
        _binMask = binMask
        while _binMask:
            _binMask &= _binMask - 1
            cnt += 1

def kernighan_shift_short(binMask=binMaskShort):
    for _ in repeat(None, num):
        cnt = 0
        _binMask = binMask
        while _binMask:
            _binMask &= _binMask - 1
            cnt += 1


table = [bin(i).count("1") for i in range(256)]

def byte_table_long(binMask=binMaskLong, table=table):
    for _ in repeat(None, num):
        cnt = (
            table[binMask & 0xff] +
            table[(binMask >> 8) & 0xff] +
            table[(binMask >> 16) & 0xff] +
            table[(binMask >> 24) & 0xff]
        )

def byte_table_short(binMask=binMaskShort, table=table):
    for _ in repeat(None, num):
        cnt = (
            table[binMask & 0xff] +
            table[(binMask >> 8) & 0xff] +
            table[(binMask >> 16) & 0xff] +
            table[(binMask >> 24) & 0xff]
        )


auto_tester(segregator='end')

"""
Conclusion:
Once bit_count() is available use that, otherwise you're better off with bin(binMask).count('1'),
kernighan_shift might be good though if you expect to have a small number of small flags most of the time.

Python27:
Name                    Secs     %    
kernighan_shift_long    1.8854   100  
iter_counter_long       1.2898   68   
byte_table_long         0.2408   13   
to_bin_and_count_long   0.145    8    

Name                     Secs     %    
iter_counter_short       0.4778   100  
byte_table_short         0.091    19   
to_bin_and_count_short   0.0796   17   
kernighan_shift_short    0.0486   10  

Python38:
Name                    Secs     %    
kernighan_shift_long    1.1172   100  
iter_counter_long       0.8156   73   
byte_table_long         0.1127   10   
to_bin_and_count_long   0.0995   9    

Name                     Secs     %    
iter_counter_short       0.5853   100  
byte_table_short         0.1094   19   
to_bin_and_count_short   0.0597   10   
kernighan_shift_short    0.0385   7   

Python310:
Name                    Secs     %    
kernighan_shift_long    1.2582   100  
iter_counter_long       0.9417   75   
byte_table_long         0.1407   11   
to_bin_and_count_long   0.1062   8    
use_bit_count_long      0.0193   2    

Name                     Secs     %    
iter_counter_short       0.7097   100  
byte_table_short         0.138    19   
to_bin_and_count_short   0.0643   9    
kernighan_shift_short    0.0464   7    
use_bit_count_short      0.0181   3    

Python314:
Name                    Secs     %    
kernighan_shift_long    1.1372   100  
iter_counter_long       0.7937   70   
byte_table_long         0.102    9    
to_bin_and_count_long   0.0609   5    
use_bit_count_long      0.0111   1    

Name                     Secs     %    
iter_counter_short       0.3339   100  
byte_table_short         0.0674   20   
to_bin_and_count_short   0.035    10   
kernighan_shift_short    0.0294   9    
use_bit_count_short      0.0103   3    

"""

