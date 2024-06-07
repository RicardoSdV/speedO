from tester import tester

many_nums_list = [i for i in range(10000000)]


def slice_next_12_in_many_nums_list():
    for i in range(len(many_nums_list) - 12):
        next_three = many_nums_list[i:i+12]


def for_i_next_12_in_many_nums_list():
    for i in range(len(many_nums_list) - 11):
        next_twelve = [many_nums_list[i + j] for j in range(12)]

def for_i_next_12_in_many_nums_list_pre_comp_rng():
    range12 = range(12)
    for i in range(len(many_nums_list) - 11):
        next_twelve = [many_nums_list[i + j] for j in range12]


tester(
    (
        slice_next_12_in_many_nums_list,
        for_i_next_12_in_many_nums_list,
        for_i_next_12_in_many_nums_list_pre_comp_rng
    )
)


"""
Conclusion:
    Python38 - Slicing way better
    
    Python27 - Slicing still way better, although slightly slower than python38

"""