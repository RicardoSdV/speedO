from tester import tester


class TestClass:
    @staticmethod
    def callable(): return

testObj = TestClass()


def dot_call_to_obj():
    for i in range(1000000):
        testObj.callable()

def getattr_call_to_obj():
    for i in range(1000000):
        getattr(testObj, 'callable')

tester(
    (
        dot_call_to_obj,
        getattr_call_to_obj
    )
)


""" Conclusion: equally good in all tested versions """

