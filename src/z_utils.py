import time

from memory_profiler import memory_usage


def print_averages(names, results, percentages, testing_what):
    results = [round(_time, 4) for _time in results]

    res_col_name = 'Secs' if testing_what == 'times' else 'Mibs' if testing_what == 'memories' else None

    name_width = max(len(name) for name in names + ['Name']) + 2
    time_width = max(len(str(result)) for result in results + [res_col_name]) + 2
    percentage_width = max(len(str(percentage)) for percentage in percentages + ['%']) + 2

    print('{:<{}} {:<{}} {:<{}}'.format('Name', name_width, res_col_name, time_width, '%', percentage_width))
    for name, _time, percentage in zip(names, results, percentages):
        print("{:<{}} {:<{}} {:<{}}".format(name, name_width, _time, time_width, percentage, percentage_width))


def sort_results_names_calc_diff(results, names):
    sorted_names, sorted_times, sorted_percentages, super_max_time = [], [], [], None

    while results and names:
        max_index = results.index(max(results))
        max_name = names.pop(max_index)
        max_time = results.pop(max_index)

        sorted_names.append(max_name)
        sorted_times.append(max_time)

        if super_max_time is None:
            super_max_time = max_time
            sorted_percentages.append(100)
        else:
            sorted_percentages.append(
                int(round(max_time/super_max_time, 2) * 100)
            )

    return sorted_names, sorted_times, sorted_percentages


def call_callables_get_times(callables, arg, return_time):
    times = []
    for func in callables:

        if arg is not None:
            if return_time:
                elapsed = func(arg)
            else:
                start_time = time.time()
                func(arg)
                elapsed = time.time() - start_time
        else:
            if return_time:
                elapsed = func()
            else:
                start_time = time.time()
                func()
                elapsed = time.time() - start_time

        times.append(elapsed)

    return times


def call_callables_get_memories(callables, _, __):
    memories = []
    for func in callables:
        mem_usages = memory_usage(func)
        max_mem_use = max(mem_usages) - min(mem_usages)
        memories.append(max_mem_use)
    return memories


def call__call_callables__repeatedly_get_average_results(
        num_repeats, callables, testing_what, return_time, print_rounds, arg=None
):
    if print_rounds: print('Repeating the test {} times'.format(num_repeats))

    if testing_what == 'times':
        caller_of_callables = call_callables_get_times
    elif testing_what == 'memories':
        caller_of_callables = call_callables_get_memories
    else:
        raise TypeError('call__call_callables__repeatedly_get_average_results only supports testing_what memories or times')

    resultss = []
    for i in range(num_repeats):
        if print_rounds: print('    Repeat number: {}'.format(i+1))

        resultss.append(
            caller_of_callables(callables, arg, return_time)
        )

    if print_rounds: print('')

    return [sum(times) / num_repeats for times in zip(*resultss)]


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
    return make_big_nums_readable(len(list_2d)), make_big_nums_readable(len(list_2d[0]))


