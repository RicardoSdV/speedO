from z_tester import tester


def using_lambda_for_condition_long_loop():
    condition = lambda x: x == 1
    for i in range(1000000):
        if condition(i):
            continue

def using_normal_condition_long_loop():
    for i in range(1000000):
        if i == 1:
            continue


def using_lambda_for_condition_short_loop():
    for i in range(1000000):
        condition = lambda x: x == 1
        for i in range(10):
            if condition(i):
                continue

def using_normal_condition_short_loop():
    for i in range(1000000):
        for i in range(10):
            if i == 1:
                continue

def using_lambda_for_condition_short_loop_with_decision():
    for i in range(1000000):
        condition = lambda x: x == 1 if i % 2 == 0 else lambda x: x == 2
        for i in range(10):
            if condition(i):
                continue


def using_normal_condition_short_loop_with_decision():
    for i in range(1000000):
        if i % 2 == 0:
            for i in range(10):
                if i == 1:
                    continue
        else:
            for i in range(10):
                if i == 2:
                    continue


tester(
    (
        using_lambda_for_condition_long_loop,
        using_normal_condition_long_loop,
        using_lambda_for_condition_short_loop,
        using_normal_condition_short_loop,
        using_lambda_for_condition_short_loop_with_decision,
        using_normal_condition_short_loop_with_decision
    )
)


""" Conclusion: In python 27 and 38 lambdas are about 2 to 4 times as slow, certainly in python3.12 both are faster and
 the gap is less but lambdas still slower 2 to 3 times"""
