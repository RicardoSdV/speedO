from itertools import repeat, islice

from src.z_tester import auto_tester_2d

sliceCnt = 10

def repeat_next_comprehend(outer, sliceCnt=sliceCnt, iter=iter, next=next, repeat=repeat):
    for inner in outer:
        iter_inner = iter(inner)
        [next(iter_inner) for _ in repeat(None, sliceCnt)]

def islice_list(outer, sliceCnt=sliceCnt, iter=iter, list=list):
    for inner in outer:
        iter_inner = iter(inner)
        list(islice(iter_inner, 0, sliceCnt))


auto_tester_2d()


"""
Conclusion:
Python314:
Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
Name                     Secs     %    
repeat_next_comprehend   0.2554   100  
islice_list              0.1518   59   

Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
Name                     Secs     %    
repeat_next_comprehend   0.0284   100  
islice_list              0.018    63   

Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
Name                     Secs     %    
repeat_next_comprehend   0.0029   100  
islice_list              0.0019   65   

Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
Name                     Secs     %    
repeat_next_comprehend   0.0003   100  
islice_list              0.0002   57   

Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
Name                     Secs   %    
repeat_next_comprehend   0.0    100  
islice_list              0.0    49   

Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
Name                     Secs   %    
repeat_next_comprehend   0.0    100  
islice_list              0.0    56   
"""
