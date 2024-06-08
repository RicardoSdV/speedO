"""
When you cant use normal list comprehension because the list needs to starts with a
custom first element what is the best way??
"""
from tester import tester

strs_list_2D = [['' for i in range(100)] for j in range(100000)]


def using_append():
    for strs_list in strs_list_2D:
        result = ['example']
        for _str in strs_list:
            result.append('    {}'.format(_str))

def using_concat():
    for strs_list in strs_list_2D:
        result = ['example'] + ['    {}'.format(_str) for _str in strs_list]


def using_extend():
    for strs_list in strs_list_2D:
        result = ['example'].extend(['    {}'.format(_str) for _str in strs_list])

tester(
    (
        using_append,
        using_concat,
        using_extend,
    )
)

"""
Conclusion:

    Python27 - Concat & extend noticeably better
    
    Python38 - Barely no difference

"""