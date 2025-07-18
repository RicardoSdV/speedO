from z_utils import get_lens_2d, call_caller_of_callables_repeatedly_get_resultss, sort_results_names_calc_diff, \
    pretty_print_results, calc_mean, calc_min, get_public_callables, get_end_segregated_callables, get_start_segregated_callables, base_auto_tester

from zz_import import prnt, vzip



def tester_2d(callables, list_3d=None, return_time=False, testing_what='times', open_file=None, make_new=False):
    """
    Some tests involve nested loops were some variation between loop length is needed
    to demonstrate how something behaves with different data sizes, this tester automates this.
    """
    from z_data import data

    num_repeats = 3
    names = [func.__name__ for func in callables]

    if list_3d is None and not make_new:
        list_3d = data.faster_3d_list

    print('Testing {}:\n'.format(testing_what))
    for list_2d in list_3d:

        len_outer_list, len_inner_list = get_lens_2d(list_2d)

        prnt('Average of {} rounds, len(outer) = {}, len(inner) = {}: '.format(
            num_repeats, len_outer_list, len_inner_list), end='')

        resultss = call_caller_of_callables_repeatedly_get_resultss(
            num_repeats, callables, testing_what, return_time, False,
            arg=list_2d, open_file=open_file, make_new=make_new,
        )

        result = calc_mean(resultss, num_repeats)

        sorted_names, sorted_results, sorted_percentages = sort_results_names_calc_diff(result, [n for n in names])
        pretty_print_results(sorted_names, sorted_results, sorted_percentages, testing_what)
        print('')
    print('')


def tester(
        callables, testing_what='times', is_callables_returning_time=False, print_rounds=False,
        num_repeats=5, calking_what='default', info='', print_num_rounds=False, open_file=None,
        make_new=False,
):

    resultss = call_caller_of_callables_repeatedly_get_resultss(
        num_repeats, callables, testing_what, is_callables_returning_time,
        print_rounds, open_file, make_new,
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

    if info: info = '({})'.format(info)

    if print_num_rounds: print('Testing {} {} of {} rounds: {}'.format(testing_what, calking_what, num_repeats, info))
    pretty_print_results(names, results, percentages, testing_what)


def auto_tester(
        testing_what='times', is_callables_returning_time=False, print_rounds=False, num_repeats=5,
        calking_what='default', info='', segregator=('start', 'end'), seg_parts=1, open_file=None,
        make_new=False,
):
    """ Entirely fed up with writing the names of the callables over and over,
    so will test most callables that don't start with _ in the file """

    base_auto_tester(
        tester, testing_what=testing_what, is_callables_returning_time=is_callables_returning_time,
        print_rounds=print_rounds, num_repeats=num_repeats, calking_what=calking_what, info=info,
        segregator=segregator, seg_parts=seg_parts, open_file=open_file, make_new=make_new,
    )


def auto_tester_2d(
        list_3d=None, return_time=False, testing_what='times', segregator=('start', 'end'),
        seg_parts=1, open_file=None, make_new=False,
):
    base_auto_tester(
        tester_2d, list_3d=list_3d, return_time=return_time, testing_what=testing_what,
        segregator=segregator, seg_parts=seg_parts, open_file=open_file, make_new=make_new,
    )
































# End
