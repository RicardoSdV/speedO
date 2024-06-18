"""
I need this_group and next_group for a program, what is the best way of getting them?
Also, indexes are incremented by different values depending on if patterns found
"""
from collections import deque
from itertools import repeat

from src.z_data import data
from src.z_tester import tester

chars = data.M_pattern_list
# chars = data.M_no_pattern_list
# chars = ['A','A','A','A','A','B','A','A','B','A','A','B','B','B','B','B']


def _slice():
    cnt = 0
    group_size = 3
    group_size_times_two = 6

    for i in range(len(chars) - group_size_times_two + 1):
        i_plus_group_size = i + group_size
        this_group = chars[i: i_plus_group_size]
        next_group = chars[i_plus_group_size: i + group_size_times_two]

        if this_group == next_group:
            cnt += 1



def slice_in_place():
    cnt = 0
    group_size = 3
    group_size_times_two = 6

    this_group = list(repeat(None, group_size))
    next_group = list(repeat(None, group_size))

    for i in range(group_size, len(chars) - group_size_times_two + 1):
        i_plus_group_size = i + group_size
        this_group[:] = chars[i: i_plus_group_size]
        next_group[:] = chars[i_plus_group_size: i + group_size_times_two]

        if this_group == next_group:
            cnt += 1



def for_in_place():
    cnt = 0
    group_size = 3
    group_size_times_two = 6
    range_group_size = range(group_size)

    this_group = list(repeat(None, group_size))
    next_group = list(repeat(None, group_size))

    for i in range(len(chars) - group_size_times_two + 1):

        for j in range_group_size:
            i_plus_j = i + j

            this_group[j] = chars[i_plus_j]
            next_group[j] = chars[i_plus_j + group_size]

        if this_group == next_group:
            cnt += 1


def for_and_pop_form_deques():
    cnt = 0
    group_size = 3

    this_group = deque(list(repeat(None, group_size)), maxlen=group_size)
    next_group = deque(list(repeat(None, group_size)), maxlen=group_size)


    for char in chars:

        this_group.popleft()
        this_group.append(next_group.popleft())
        next_group.append(char)

        if this_group == next_group:
            cnt += 1



tester(
    (
        slice_in_place,
        for_in_place,
        _slice,
        for_and_pop_form_deques,
    )
)


"""
Conclusion:
    - Popping from deque great, slice catching up, probs slicing in place slower
    because all the new lists are not getting garbage collected during timer, for
    pobs suck bc of math
    
    pypy310:
        - Using pypy really does make for loops worth it again
    
        Average of 5 rounds: 
        Name                      Time     %    
        for_and_pop_form_deques   0.929    100  
        slice_in_place            0.8678   93   
        _slice                    0.6876   74   
        for_in_place              0.5739   62   

    Python312:
        Average of 5 rounds: 
        Name                      Time     %    
        for_in_place              2.4434   100  
        slice_in_place            2.362    97   
        _slice                    1.7183   70   
        for_and_pop_form_deques   1.5989   65   
    
    
    Python38:
        Name                      Time     %    
        for_in_place              3.0972   100  
        slice_in_place            2.3674   76   
        _slice                    1.6562   53   
        for_and_pop_form_deques   1.5262   49
    
    Python27:
        Name                      Time     %    
        for_in_place              3.7488   100  
        slice_in_place            2.9662   79   
        _slice                    2.3534   63   
        for_and_pop_form_deques   1.917    51   


"""
