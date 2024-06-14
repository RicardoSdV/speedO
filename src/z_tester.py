from z_data import data
from z_utils import get_lens_2d, call__call_callables__repeatedly_get_average_times, sort_times_names_calc_diff, \
    print_averages


def tester_2d_loops(callables, return_time=False, list_3d=data.slower_3d_list):
    """
    Some test cases involve nested for loops were some variation between the length of the outer and inner
    loops is needed to demonstrate how something behaves with different sizes of data, this tester automates this.
    """

    num_repeats = 3
    names = [func.__name__ for func in callables]

    for list_2d in list_3d:
        len_outer_list, len_inner_list = get_lens_2d(list_2d)
        print('Average of {} rounds, len(outer_list) = {}, len(inner_list) = {}: '.format(
            num_repeats, len_outer_list, len_inner_list)
        )

        times = call__call_callables__repeatedly_get_average_times(num_repeats, callables, return_time, arg=list_2d)

        sorted_names, sorted_times, sorted_percentages = sort_times_names_calc_diff(times, [n for n in names])
        print_averages(sorted_names, sorted_times, sorted_percentages)
        print('')


def tester(callables, is_callables_returning_time=False):
    num_repeats = 5

    times = call__call_callables__repeatedly_get_average_times(num_repeats, callables, is_callables_returning_time)
    names, times, percentages = sort_times_names_calc_diff(times, [func.__name__ for func in callables])

    print('Average of {} rounds: '.format(num_repeats))
    print_averages(names, times, percentages)

