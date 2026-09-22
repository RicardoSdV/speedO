from itertools import islice

from src.z_tester import auto_tester_2d
from zz_import import vzip, vrange

def iter_and_next_use_exc(outer, _iter=iter, _next=next):
    for inner in outer:
        iterInner = _iter(inner)
        try:
            while True:
                el1 = _next(iterInner)
                el2 = _next(iterInner)
        except StopIteration:
            continue

def iter_and_next_use_default(outer, _iter=iter, _next=next):
    for inner in outer:
        iterInner = _iter(inner)
        el2 = True
        while el2:
            el1 = _next(iterInner, False)
            el2 = _next(iterInner, False)

def slice_and_izip(outer, _zip=vzip):
    for inner in outer:
        lenInner = len(inner)
        for el1, el2 in _zip(inner[0: lenInner: 2], inner[1: lenInner: 2]):
            continue

def islice_and_izip(outer, _zip=vzip, _islice=islice):
    for inner in outer:
        lenInner = len(inner)
        for el1, el2 in _zip(_islice(inner, 0, lenInner, 2), _islice(inner, 1, lenInner, 2)):
            continue

def for_xrange_and_index_access(outer, _xrange=vrange):
    for inner in outer:
        for i in _xrange(0, len(inner), 2):
            el1 = inner[i]
            el2 = inner[i+1]

def iter_for_and_next(outer, _iter=iter, _next=next):
    for inner in outer:
        iterInner = _iter(inner)
        for el1 in iterInner:
            el2 = _next(iterInner)

def for_izip_iter(outer, _iter=iter, _izip=vzip):
    for inner in outer:
        iterInner = _iter(inner)
        for el1, el2 in _izip(iterInner, iterInner):
            continue

def use_batched(outer):
    from itertools import batched
    for inner in outer:
        for el1, el2 in batched(inner, 2):
            continue

from sys import version
version = float('.'.join(version.split(' ')[0].split('.')[0: -1]))
if version < 3.12:
    del use_batched


auto_tester_2d()

"""
Conclusion:
- Basically use for_izip_iter and forget about it, specially if you're not making next a local of the function.
Apparently itertools.batched exists in python312+ maybe its worth using that if you dont care about cross compatibility
except it sucks.

Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name                          Secs     %    
    iter_and_next_use_exc         0.577    100  
    iter_and_next_use_default     0.4443   77   
    slice_and_izip                0.332    57   
    islice_and_izip               0.3217   56   
    for_xrange_and_index_access   0.2563   44   
    for_izip_iter                 0.1847   32   
    iter_for_and_next             0.1797   31   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name                          Secs     %    
    iter_and_next_use_default     0.325    100  
    iter_and_next_use_exc         0.279    86   
    for_xrange_and_index_access   0.153    47   
    iter_for_and_next             0.1257   39   
    islice_and_izip               0.1233   38   
    slice_and_izip                0.1057   33   
    for_izip_iter                 0.0803   25   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name                          Secs     %    
    iter_and_next_use_default     0.304    100  
    iter_and_next_use_exc         0.2413   79   
    for_xrange_and_index_access   0.1517   50   
    iter_for_and_next             0.1163   38   
    islice_and_izip               0.0913   30   
    slice_and_izip                0.0817   27   
    for_izip_iter                 0.0607   20   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name                          Secs     %    
    iter_and_next_use_default     0.31     100  
    iter_and_next_use_exc         0.2367   76   
    for_xrange_and_index_access   0.1493   48   
    iter_for_and_next             0.1167   38   
    islice_and_izip               0.0893   28   
    slice_and_izip                0.0823   27   
    for_izip_iter                 0.06     19   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name                          Secs     %    
    iter_and_next_use_default     0.3117   100  
    iter_and_next_use_exc         0.2387   77   
    for_xrange_and_index_access   0.15     48   
    iter_for_and_next             0.1183   38   
    slice_and_izip                0.092    30   
    islice_and_izip               0.0893   28   
    for_izip_iter                 0.059    19   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name                          Secs     %    
    iter_and_next_use_default     0.3083   100  
    iter_and_next_use_exc         0.2287   74   
    for_xrange_and_index_access   0.1477   48   
    slice_and_izip                0.1293   42   
    iter_for_and_next             0.1153   37   
    islice_and_izip               0.088    28   
    for_izip_iter                 0.0577   19   

Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                          Secs     %    
    islice_and_izip               0.236    100  
    iter_and_next_use_default     0.2117   90   
    slice_and_izip                0.2045   87   
    for_xrange_and_index_access   0.2042   87   
    iter_and_next_use_exc         0.2029   86   
    for_izip_iter                 0.1228   52   
    iter_for_and_next             0.0893   38   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1405   100  
    for_xrange_and_index_access   0.1263   90   
    iter_and_next_use_exc         0.1095   78   
    islice_and_izip               0.0948   67   
    slice_and_izip                0.0716   51   
    iter_for_and_next             0.0686   49   
    for_izip_iter                 0.0605   43   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                          Secs     %    
    for_xrange_and_index_access   0.1475   100  
    iter_and_next_use_default     0.1334   90   
    iter_and_next_use_exc         0.0975   66   
    islice_and_izip               0.0812   55   
    slice_and_izip                0.0712   48   
    iter_for_and_next             0.064    43   
    for_izip_iter                 0.049    33   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                          Secs     %    
    for_xrange_and_index_access   0.1537   100  
    iter_and_next_use_default     0.1331   87   
    iter_and_next_use_exc         0.0962   63   
    slice_and_izip                0.0787   51   
    islice_and_izip               0.0785   51   
    iter_for_and_next             0.0621   40   
    for_izip_iter                 0.0507   33   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                          Secs     %    
    for_xrange_and_index_access   0.1523   100  
    iter_and_next_use_default     0.1268   83   
    iter_and_next_use_exc         0.0964   63   
    slice_and_izip                0.0894   59   
    islice_and_izip               0.0781   51   
    iter_for_and_next             0.0624   41   
    for_izip_iter                 0.0488   32   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                          Secs     %    
    for_xrange_and_index_access   0.151    100  
    slice_and_izip                0.1287   85   
    iter_and_next_use_default     0.128    85   
    iter_and_next_use_exc         0.0969   64   
    islice_and_izip               0.0802   53   
    iter_for_and_next             0.0643   43   
    for_izip_iter                 0.0484   32   

Python314:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name                          Secs     %    
    islice_and_izip               0.2912   100  
    slice_and_izip                0.2327   80   
    iter_and_next_use_default     0.2006   69   
    iter_and_next_use_exc         0.181    62   
    use_batched                   0.1402   48   
    for_xrange_and_index_access   0.1381   47   
    for_izip_iter                 0.138    47   
    iter_for_and_next             0.0831   28   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1305   100  
    islice_and_izip               0.1057   81   
    iter_and_next_use_exc         0.1037   79   
    for_xrange_and_index_access   0.0882   68   
    use_batched                   0.0832   64   
    slice_and_izip                0.0793   61   
    for_izip_iter                 0.0634   49   
    iter_for_and_next             0.0609   47   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1262   100  
    for_xrange_and_index_access   0.1129   89   
    iter_and_next_use_exc         0.0975   77   
    islice_and_izip               0.0909   72   
    use_batched                   0.0864   68   
    slice_and_izip                0.0818   65   
    iter_for_and_next             0.0622   49   
    for_izip_iter                 0.0603   48   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1283   100  
    for_xrange_and_index_access   0.1218   95   
    iter_and_next_use_exc         0.0976   76   
    use_batched                   0.0899   70   
    slice_and_izip                0.0875   68   
    islice_and_izip               0.0866   68   
    iter_for_and_next             0.063    49   
    for_izip_iter                 0.0626   49   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1272   100  
    for_xrange_and_index_access   0.1204   95   
    slice_and_izip                0.1006   79   
    iter_and_next_use_exc         0.0968   76   
    use_batched                   0.0894   70   
    islice_and_izip               0.0893   70   
    for_izip_iter                 0.0627   49   
    iter_for_and_next             0.0625   49   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name                          Secs     %    
    iter_and_next_use_default     0.1286   100  
    slice_and_izip                0.1275   99   
    for_xrange_and_index_access   0.1197   93   
    iter_and_next_use_exc         0.0965   75   
    use_batched                   0.0892   69   
    islice_and_izip               0.0885   69   
    iter_for_and_next             0.0629   49   
    for_izip_iter                 0.0622   48  
"""
