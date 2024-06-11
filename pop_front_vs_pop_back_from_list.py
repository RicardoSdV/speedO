from z_tester import tester

list_of_few_nums_lists = [[i for i in range(100)] for j in range(100000)]


def many_front_pops_from_small_list():
    for few_nums_list in list_of_few_nums_lists:
        for i in range(10):
            few_nums_list.pop(0)


def many_back_pops_from_small_list():
    for few_nums_list in list_of_few_nums_lists:
        for i in range(10):
            few_nums_list.pop()


many_nums_list = [i for i in range(10000000)]


def few_front_pops_from_many_nums_lists():
    for i in range(1000):
        many_nums_list.pop(0)


def few_back_pops_from_many_nums_lists():
    for i in range(1000):
        many_nums_list.pop()


tester(
    (
        many_front_pops_from_small_list,
        many_back_pops_from_small_list,
        few_front_pops_from_many_nums_lists,
        few_back_pops_from_many_nums_lists,
    )
)

"""
Conclusion:
    Python312 - Simmilar to python38 but slightly faster specially for small lists

    Python38 - For small lists the difference is not that big but sill twice as fast to pop back
    than to pop front, for large lists, its is almost a sin to pop front, thousands of times more
    efficient to pop back
    
    Python27 - Small lists operations are slower, which im not sure if, but the gap between front 
    and back popping is reduced. For large lists the difference is similarly sinful 

"""

