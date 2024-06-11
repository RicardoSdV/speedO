from time import time, sleep


def tester(callables):
    sleep_interval = 0.1

    for func in callables:
        start_time = time()
        func()
        duration = time() - start_time

        print('{} {}'.format(func.__name__, duration))

        sleep(sleep_interval)
