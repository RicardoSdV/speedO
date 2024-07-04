from z_utils import get_lens_2d, call__call_callables__repeatedly_get_resultss, sort_results_names_calc_diff, \
    pretty_print_results, calc_mean, calc_min


def tester_2d_loops(callables, list_3d, return_time=False):
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

        times = call__call_callables__repeatedly_get_resultss(
            num_repeats, callables, return_time, False, arg=list_2d
        )

        sorted_names, sorted_times, sorted_percentages = sort_results_names_calc_diff(times, [n for n in names])
        pretty_print_results(sorted_names, sorted_times, sorted_percentages)
        print('')


def tester(callables, testing_what='times', is_callables_returning_time=False, print_rounds=True, num_repeats=5, calking_what='default'):

    resultss = call__call_callables__repeatedly_get_resultss(
        num_repeats, callables, testing_what, is_callables_returning_time, print_rounds
    )

    if calking_what == 'default':
        calking_what = 'mean' if testing_what == 'times' else 'min' if testing_what == 'memories' else None

    if calking_what == 'mean':
        results = calc_mean(resultss, num_repeats)
    elif calking_what == 'min':
        results = calc_min(resultss)
    else:
        raise ValueError('Can only handle default, mean and min')

    calking_what = 'mean'  # Theoretically the min makes some sense for memory, since the gc deallocates mem
                           # when it feels like it and other allocs and dallocs happen simultaneously, so,
                           # theoretically, out of an infinite number of runs, the one where the memchange is
                           # the least is the one with the most accurate results, since the only memchange that
                           # must happen is the alloc of whatever thing is being created in the test


    names, results, percentages = sort_results_names_calc_diff(results, [func.__name__ for func in callables])

    print('Testing {} {} of {} rounds: '.format(testing_what, calking_what, num_repeats))
    pretty_print_results(names, results, percentages, testing_what)



































# End
