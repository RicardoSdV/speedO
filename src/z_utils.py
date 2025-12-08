from collections import defaultdict
from functools import partial
from sys import _getframe
from time import time

from memory_profiler import memory_usage


def pretty_print_results(names, results, percentages, testing_what):
    results = [round(_time, 4) for _time in results]

    res_col_name = 'Secs' if testing_what == 'times' else 'Mibs' if testing_what == 'memories' else None

    name_width = max(len(name) for name in names + ['Name']) + 2
    time_width = max(len(str(result)) for result in results + [res_col_name]) + 2
    percentage_width = max(len(str(percentage)) for percentage in percentages + ['%']) + 2

    print('{:<{}} {:<{}} {:<{}}'.format('Name', name_width, res_col_name, time_width, '%', percentage_width))
    for name, _time, percentage in zip(names, results, percentages):
        print("{:<{}} {:<{}} {:<{}}".format(name, name_width, _time, time_width, percentage, percentage_width))


def sort_results_names_calc_diff(results, names):
    sorted_names, sorted_times, sorted_percentages, super_max_result = [], [], [], None
    append_to_sorted_percentages = sorted_percentages.append

    while results and names:
        max_index = results.index(max(results))
        max_name = names.pop(max_index)
        max_result = results.pop(max_index)

        sorted_names.append(max_name)
        sorted_times.append(max_result)

        if super_max_result is None:
            super_max_result = max_result
            append_to_sorted_percentages(100)
        else:
            if super_max_result > 0:
                append_to_sorted_percentages(
                    int(round(max_result/super_max_result, 2) * 100)
                )
            else:
                append_to_sorted_percentages(0)

    return sorted_names, sorted_times, sorted_percentages


def call_callables_get_times(callables, getArg, return_time, open_file):
    times = []
    i = 0
    for func in callables:
        arg = getArg()

        if isinstance(arg, tuple):
            this_arg = arg[i]
            i += 1
            if i > len(arg):
                i = 0
            if return_time:
                if open_file:
                    elapsed = func(this_arg, open_file)
                else:
                    elapsed = func(this_arg)
            else:
                if open_file:
                    start_time = time()
                    func(this_arg, open_file)
                    elapsed = time() - start_time
                else:
                    start_time = time()
                    func(this_arg)
                    elapsed = time() - start_time

        elif arg is not None:
            if return_time:
                if open_file:
                    elapsed = func(arg, open_file)
                else:
                    elapsed = func(arg)
            else:
                if open_file:
                    start_time = time()
                    func(arg, open_file)
                    elapsed = time() - start_time
                else:
                    start_time = time()
                    func(arg)
                    elapsed = time() - start_time
        else:
            if return_time:
                if open_file:
                    elapsed = func(open_file)
                else:
                    elapsed = func()
            else:
                if open_file:
                    start_time = time()
                    func(open_file)
                    elapsed = time() - start_time
                else:
                    start_time = time()
                    func()
                    elapsed = time() - start_time

        times.append(elapsed)

        if open_file:
            open_file.seek(0)
            open_file.truncate()

    return times

def call_callables_get_memories(callables, getArg, *_):
    arg = getArg()
    arg = () if arg is None else (arg, )
    memories = []
    for func in callables:
        mem_usages = memory_usage((func, arg, {}))
        max_mem_use = max(mem_usages) - min(mem_usages)
        memories.append(max_mem_use)
    return memories


def call_caller_of_callables_repeatedly_get_resultss(
        num_repeats, callables, testing_what, return_time, print_rounds, arg=None, open_file=None, make_new=False
):
    if print_rounds: print('Repeating the test {} times'.format(num_repeats))

    if testing_what == 'times':
        caller_of_callables = call_callables_get_times
    elif testing_what == 'memories':
        caller_of_callables = call_callables_get_memories
    else:
        raise TypeError('call_caller_of_callables_repeatedly_get_resultss only supports testing_what memories or times')

    from src.z_data import data
    if make_new:
        getArg = partial(getattr, data, arg)
    else:
        getArg = partial(lambda: arg)

    resultss = []; append = resultss.append
    for i in range(num_repeats):
        if print_rounds: print('    Repeat number: %s' % (i+1))
        append(
            caller_of_callables(callables, getArg, return_time, open_file)
        )

    print('')

    return resultss


def calc_mean(resultss, num_repeats):
    return [sum(times) / num_repeats for times in zip(*resultss)]

def calc_min(resultss):
    return [min(times) for times in zip(*resultss)]


def make_big_nums_readable(num):
    num = str(num)
    readable_num = []
    cnt = 0
    for char in reversed(num):
        if cnt == 3:
            cnt = 0
            readable_num.append(' ')
        readable_num.append(char)
        cnt += 1

    return ''.join(reversed(readable_num))


def get_lens_2d(list_2d):
    if isinstance(list_2d, tuple):
        list_2d = list_2d[0]

    return make_big_nums_readable(len(list_2d)), make_big_nums_readable(len(list_2d[0]))


def get_public_callables(
        exclude={
            'auto_tester', 'repeat', 'ifilter', 'deque', 'partial', 'join',
            'list_of_tuples_of_two_lens_of_rand_ints', 'cycle', 'list_of_tuples_of_rand_ints',
            'weakref', 'cycle', 'dyn_list_of_list_of_rand_ints', 'namedtuple',
            'auto_tester_2d', 'chain', 'islice'
        },
        frameNum=2,
):
    res = (
        local for name, local in _getframe(frameNum).f_locals.items()
        if not name.startswith('_') and callable(local) and name not in exclude
    )
    return res

def start_segregator(callable, num_parts):
    return '_'.join(callable.__name__.split('_')[:num_parts])

def end_segregator(callable, num_parts):
    end = '_'.join(callable.__name__.split('_')[-num_parts:])
    return int(end) if end.isdigit() else end

def get_segregated_callables(segregator, num_parts):
    callables = get_public_callables(frameNum=3)

    segCallables = defaultdict(list)
    for callable in callables:
        segCallables[segregator(callable, num_parts)].append(callable)

    segCallables = list(segCallables.values())
    segCallables.sort(key=lambda callables: segregator(callables[0], num_parts))

    return segCallables

get_start_segregated_callables = partial(get_segregated_callables, start_segregator)
get_end_segregated_callables   = partial(get_segregated_callables, end_segregator)

def base_auto_tester(tester, **kwargs):
    seggregator = kwargs.pop('segregator')
    seg_parts = kwargs.pop('seg_parts')

    if seggregator == 'start':
        for callables in get_start_segregated_callables(seg_parts):
            tester(tuple(callables), **kwargs)

    elif seggregator == 'end':
        for callables in get_end_segregated_callables(seg_parts):
            tester(tuple(callables), **kwargs)
    else:
        tester(tuple(get_public_callables(frameNum=3)), **kwargs)
