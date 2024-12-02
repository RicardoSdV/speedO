from src.z_data import data
from src.z_tester import tester_2d


num = data.M100

def tupleComprehension(outer):
    for inner in outer:
        tuple(el for el in inner)

def tupleGenComprehension(outer):
    for inner in outer:
        tuple((el for el in inner))


tester_2d(
    (
        tupleComprehension,
        tupleGenComprehension
    ),
    list_3d=data.slower_3d_list,
)

"""
Conclusion:
    Python27:
        
"""
