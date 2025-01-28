from src.z_data import data
from src.z_tester import auto_tester


def make_del_tuples(tuples=data.M10__six_int_tuples):
    newList = [(one, two, three, four, five, six+1) for one, two, three, four, five, six in tuples]

def mod_list_in_place(lists=data.M10__six_int_lists):
    for _list in lists:
        _list[-1] += 1

auto_tester()


