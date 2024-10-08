"""
Compare the performance of IPLs when they don't need to grow

Work in progress
"""
import sys
from itertools import repeat, islice
from random import choice
from string import printable

from numpy import empty

from src.z_data import data
from src.z_tester import tester

rep_cnt = data.k10

# lines1 = tuple((''.join(choice(printable) for _ in repeat(None, 120)) for _ in repeat(None, 1000)))
# lines2 = tuple(reversed(lines1))

lines1 = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
lines2 = tuple(reversed(lines1))

if sys.version.startswith('3'):
    class IPL:
        """ In Place List """
        __slots__ = ('_idx', '_list', '_len_list')

        def __init__(self):
            self._idx = -1
            self._list = []
            self._len_list = 0  # Yes, faster than len()

        def append(self, element):
            self._idx += 1
            try:
                self._list[self._idx] = element
            except IndexError:
                self._list.append(element)
                self._len_list += 1

        def reset(self):
            yield from islice(self._list, self._idx+1)
            self._idx = -1

    class IPL2:
        """ In Place List """
        __slots__ = ('_idx', '_list', '_len_list', '_append')

        def __init__(self):
            self._idx = -1
            self._list = []
            self._len_list = 0  # Yes, faster than len()
            self._append = self._append_gen()

        def _append_gen(self):
            for i in range(self._len_list):
                element = yield
                self._list[i] = element
                yield i

        def append(self, element):
            try:
                next(self._append)
                self._idx = self._append.send(element)
            except StopIteration:
                self._list.append(element)
                self._len_list += 1
                self._idx += 1
                self._append = self._append_gen()

        def reset(self):
            yield from islice(self._list, self._idx+1)
else:
    pass

def run_ipl():
    ipl = IPL()
    append_to_ipl = ipl.append
    reset_ipl = ipl.reset
    _lines1, _lines2 = lines1, lines2

    for _ in repeat(None, rep_cnt):
        for line in _lines1: append_to_ipl(line)
        for el in reset_ipl(): continue
        for line in lines2: append_to_ipl(line)
        for el in reset_ipl(): continue

    print(ipl._list)

def run_ipl2():
    ipl = IPL2()
    append_to_ipl = ipl.append
    reset_ipl = ipl.reset
    _lines1, _lines2 = lines1, lines2

    for _ in repeat(None, rep_cnt):
        for line in _lines1: append_to_ipl(line)
        for el in reset_ipl(): continue
        for line in lines2: append_to_ipl(line)
        for el in reset_ipl(): continue

    print(ipl._list)


def run_normal_list():
    _list = []
    append_to_list = _list.append
    _lines1, _lines2 = lines1, lines2

    for _ in repeat(None, rep_cnt):
        for line in _lines1: append_to_list(line)
        for el in _list: continue
        _list = []
        for line in _lines2: append_to_list(line)
        for el in _list: continue
        _list = []

if __name__ == '__main__':
    tester(
        (
            run_ipl,
            run_ipl2,
            run_normal_list,
        ),
        num_repeats = 5,
    )
    # tester(
    #     (
    #         run_ipl,
    #         run_normal_list,
    #     ),
    #     testing_what='memories',
    # )

"""
Conclusion:
    - Mod in place about 4 times as slow, however im not convinced that the
    cost of garbage collection is properly accounted for, since the memory
    profiler shows the diff of memory being used by the program during the 
    execution of the function, & if all the memory is being deallocated every
    cycle of the loop it should show 0 mem difference, or close to that, the
    equivalent of a couple lists of 1000 elements, which it definitely does not.
    
    - I dont include the numpy array version because its about twice as slow than
    the pure python version. And I can't be bothered to rerun all the versions
    
    Python312:
        Testing times mean of 5 rounds: 
        Name              Secs     %    
        run_ipl           14.029   100  
        run_normal_list   5.6951   41   
        
        Testing memories mean of 5 rounds: 
        Name              Mibs        %    
        run_normal_list   2721.5625   100  
        run_ipl           0.0         0    

    Python310:
        Testing times mean of 5 rounds: 
        Name              Secs      %    
        run_ipl           19.6829   100  
        run_normal_list   5.4711    28   
        
        Testing memories mean of 5 rounds: 
        Name              Mibs        %    
        run_normal_list   2339.8008   100  
        run_ipl           0.0         0    
            
    Python38:
        Testing times mean of 5 rounds: 
        Name              Secs      %    
        run_ipl           20.5205   100  
        run_normal_list   5.0218    24   

        Testing memories mean of 5 rounds: 
        Name              Mibs        %    
        run_normal_list   2703.5898   100  
        run_ipl           0.4219      0    
        
    Important note:
        If you run, only the speed test long enough this will happen:
    
        Traceback (most recent call last):
      File "C:\prjs\speedO\src\list_in_place_vs_new_list.py", line 127, in <module>
        tester(
      File "C:\prjs\speedO\src\z_tester.py", line 39, in tester
        resultss = call_caller_of_callables_repeatedly_get_resultss(
      File "C:\prjs\speedO\src\z_utils.py", line 97, in call_caller_of_callables_repeatedly_get_resultss
        caller_of_callables(callables, arg, return_time)
      File "C:\prjs\speedO\src\z_utils.py", line 62, in call_callables_get_times
        func()
      File "C:\prjs\speedO\src\list_in_place_vs_new_list.py", line 120, in run_normal_list
        for line in _lines2: append_to_list(line)
    MemoryError
    
    And the way the tester works, implies that modify the list in place will not cause a memory error
    since it will run before the normal list test, which means that mod in place is safer than
    creating and deleting a bunch of lists. However more likely it suggests that the garbage collector
    is not collecting the dereferenced lists within the function, so they just accumulate, this should not
    happen in a "normal" program, however, it does suggest that the times are not taking into account the
    garbage collecting
"""

