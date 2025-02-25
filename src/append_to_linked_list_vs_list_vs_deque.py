from collections import deque
from src.z_tester import tester_2d


class _Node(object):
    __slots__ = ('n', 'v')

    def __init__(self, n, v):
        self.n = n
        self.v = v

def obj_linked_list(outer, N=_Node):
    for inner in outer:
        head = N(None, None)
        tail = head
        for i in inner:
            new_node = N(None, i)
            tail.n = new_node
            tail = new_node

def list_linked_list(outer):
    for inner in outer:
        head = [None, None]
        tail = head
        for i in inner:
            new = [None, i]
            tail[0] = new
            tail = new

def list_predef_append(outer):
    for inner in outer:
        _list = []
        append = _list.append
        for i in inner:
            append(i)

def list_normal_append(outer):
    for inner in outer:
        _list = []
        for i in inner:
            _list.append(i)

def deque_predef_append(outer, Deque=deque):
    for inner in outer:
        deq = Deque()
        append = deq.append
        for i in inner:
            append(i)

def deque_normal_append(outer, Deque=deque):
    for inner in outer:
        deq = Deque()
        for i in inner:
            deq.append(i)

tester_2d(
    (
        obj_linked_list,
        list_linked_list,
        list_predef_append,
        list_normal_append,
        deque_predef_append,
        deque_normal_append,
    ),
)

"""
Conclusion:
        - Theres no reason to implement a singly linked list in python that I can think of,
        but if you are, use a list for the nodes, never an object, also the longer the linked
        list the slower it is to append to it compared to other methods, which seems wierd, since
        the whole point of a linked list is O(1) appending but yeah it may be that theres less
        resizing for longer list()s 
        
        - Also, theres probably a better way of implementing the linked lists, no dummy node, 
        and no modifying nodes after creation, maybe? but yeah there no fixing 100x slower I think
  
    Python27:
        - Appending to a deque surprisingly fast, it remains to be seen how slow it is to iterate
        over the elements after, but, if appending happens in a perf critical part you might consider
        a deque instead of a list, specially for very long sequences 100k +.
    
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                  Secs     %    
        obj_linked_list       1.582    100  
        list_linked_list      0.5913   37   
        list_normal_append    0.413    26   
        deque_normal_append   0.3353   21   
        list_predef_append    0.298    19   
        deque_predef_append   0.2487   16   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                  Secs     %    
        obj_linked_list       1.4333   100  
        list_linked_list      0.5477   38   
        list_normal_append    0.2993   21   
        deque_normal_append   0.248    17   
        list_predef_append    0.196    14   
        deque_predef_append   0.1547   11   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                  Secs     %    
        obj_linked_list       2.2793   100  
        list_linked_list      1.398    61   
        list_normal_append    0.2643   12   
        deque_normal_append   0.2453   11   
        list_predef_append    0.1647   7    
        deque_predef_append   0.152    7    
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                  Secs      %    
        obj_linked_list       11.2307   100  
        list_linked_list      10.9587   98   
        list_normal_append    0.4353    4    
        deque_normal_append   0.3973    4    
        list_predef_append    0.2797    2    
        deque_predef_append   0.2377    2    
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                  Secs      %    
        list_linked_list      16.146    100  
        obj_linked_list       16.1427   100  
        list_normal_append    0.4247    3    
        deque_normal_append   0.4023    2    
        list_predef_append    0.2613    2    
        deque_predef_append   0.2487    2    
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                  Secs      %    
        obj_linked_list       12.1143   100  
        list_linked_list      10.935    90   
        list_normal_append    0.351     3    
        list_predef_append    0.255     2    
        deque_normal_append   0.2463    2    
        deque_predef_append   0.156     1    
        
    Python38:
        - deque still dominating for > 100 appends, although I'd recon most 
        lists are < 100 elements so less of an excuse to use deque in python38
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                  Secs     %    
        obj_linked_list       0.9819   100  
        list_linked_list      0.3103   32   
        deque_normal_append   0.2091   21   
        list_normal_append    0.2019   21   
        deque_predef_append   0.184    19   
        list_predef_append    0.1675   17   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                  Secs     %    
        obj_linked_list       0.888    100  
        list_linked_list      0.298    34   
        list_normal_append    0.196    22   
        deque_normal_append   0.172    19   
        list_predef_append    0.154    17   
        deque_predef_append   0.1313   15   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                  Secs     %    
        obj_linked_list       1.4717   100  
        list_linked_list      0.893    61   
        list_normal_append    0.1917   13   
        deque_normal_append   0.1698   12   
        list_predef_append    0.1424   10   
        deque_predef_append   0.127    9    
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                  Secs     %    
        obj_linked_list       5.2841   100  
        list_linked_list      4.7054   89   
        list_normal_append    0.1808   3    
        deque_normal_append   0.1725   3    
        list_predef_append    0.1352   3    
        deque_predef_append   0.1306   2    
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                  Secs     %    
        obj_linked_list       7.5466   100  
        list_linked_list      7.1514   95   
        deque_normal_append   0.1837   2    
        list_normal_append    0.1799   2    
        deque_predef_append   0.1382   2    
        list_predef_append    0.1322   2    
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                  Secs     %    
        obj_linked_list       6.4349   100  
        list_linked_list      5.7454   89   
        list_normal_append    0.2783   4    
        list_predef_append    0.2431   4    
        deque_normal_append   0.1878   3    
        deque_predef_append   0.1445   2    
    
    Python310:
        - List and deque getting closer, but still deque slightly better
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                  Secs     %    
        obj_linked_list       1.0538   100  
        list_linked_list      0.3397   32   
        deque_normal_append   0.233    22   
        list_normal_append    0.2193   21   
        deque_predef_append   0.2041   19   
        list_predef_append    0.193    18   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                  Secs     %    
        obj_linked_list       0.9468   100  
        list_linked_list      0.3221   34   
        list_normal_append    0.2961   31   
        list_predef_append    0.2587   27   
        deque_normal_append   0.1899   20   
        deque_predef_append   0.1467   15   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                  Secs     %    
        obj_linked_list       1.4963   100  
        list_linked_list      0.8824   59   
        list_normal_append    0.2162   14   
        deque_normal_append   0.1872   13   
        list_predef_append    0.171    11   
        deque_predef_append   0.1437   10   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                  Secs     %    
        obj_linked_list       5.1005   100  
        list_linked_list      4.6248   91   
        list_normal_append    0.1986   4    
        deque_normal_append   0.1882   4    
        list_predef_append    0.1521   3    
        deque_predef_append   0.1518   3    
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                  Secs     %    
        obj_linked_list       7.6695   100  
        list_linked_list      6.9311   90   
        deque_normal_append   0.2      3    
        list_normal_append    0.1925   3    
        deque_predef_append   0.1527   2    
        list_predef_append    0.1495   2    
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                  Secs     %    
        obj_linked_list       6.3585   100  
        list_linked_list      5.858    92   
        list_normal_append    0.2933   5    
        list_predef_append    0.2467   4    
        deque_normal_append   0.206    3    
        deque_predef_append   0.1601   3    

        
    Python312:
        - deque and list pretty tied, but list slightly better now, and as we know
        normal appending is now good in 312 
        
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                  Secs     %    
        obj_linked_list       0.8645   100  
        list_linked_list      0.338    39   
        deque_predef_append   0.267    31   
        deque_normal_append   0.2537   28   
        list_predef_append    0.1777   21   
        list_normal_append    0.1639   19   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                  Secs     %    
        obj_linked_list       0.8094   100  
        list_linked_list      0.2967   37   
        list_predef_append    0.1654   20   
        deque_normal_append   0.1647   20   
        deque_predef_append   0.1547   19   
        list_normal_append    0.1507   19   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                  Secs     %    
        obj_linked_list       1.4247   100  
        list_linked_list      0.8799   62   
        list_predef_append    0.1469   10   
        deque_normal_append   0.1453   10   
        deque_predef_append   0.135    9    
        list_normal_append    0.1306   9    
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                  Secs     %    
        obj_linked_list       4.9052   100  
        list_linked_list      4.522    92   
        deque_normal_append   0.1465   3    
        list_predef_append    0.1436   3    
        deque_predef_append   0.1429   3    
        list_normal_append    0.1245   3    
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                  Secs     %    
        obj_linked_list       7.4973   100  
        list_linked_list      6.672    89   
        deque_normal_append   0.1499   2    
        deque_predef_append   0.1429   2    
        list_predef_append    0.1389   2    
        list_normal_append    0.1242   2    
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                  Secs     %    
        obj_linked_list       6.3406   100  
        list_linked_list      5.8317   92   
        list_predef_append    0.2482   4    
        list_normal_append    0.2296   4    
        deque_normal_append   0.1567   2    
        deque_predef_append   0.1502   2    
    
"""

