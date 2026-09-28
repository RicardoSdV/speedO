from src.z_data import data
from src.z_tester import auto_tester_2d
from zz_import import clock, intern

def manual_intern(outer):
    elapsed = 0
    data_by_id = {}
    id_by_data = {}
    ids = []; ids_app = ids.append
    _id = id

    for inner in outer:
        start = clock()

        for el in inner:
            if el in id_by_data:
                ids_app(id_by_data[el])
                continue

            el_id = _id(el)
            data_by_id[el_id] = el
            id_by_data[el] = el_id
            ids_app(el_id)

        elapsed += clock() - start

        data_by_id.clear()
        id_by_data.clear()
        del ids[:]

    return elapsed

def builtin_intern(outer):
    elapsed = 0
    data_by_id = {}
    ids = []; ids_app = ids.append
    _id = id; _intern = intern

    for inner in outer:
        start = clock()

        for el in inner:
            el = _intern(el)
            el_id = _id(el)
            ids_app(el_id)
            if el_id not in data_by_id:
                data_by_id[el_id] = el

        elapsed += clock() - start

        data_by_id.clear()
        del ids[:]

    return elapsed

auto_tester_2d(
    list_3d=data.make_super_fast_3d_list_of_rnd_repeat_strs(0.1, 5, 80),
    return_time=True,
)

"""
Conclusion:
Yep, manually interning is faster, im not sure though if there is a better way to leverage intern().

Python27:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10:  
    Name             Secs     %    
    builtin_intern   0.1836   100  
    manual_intern    0.1313   71   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100:  
    Name             Secs     %    
    builtin_intern   0.1071   100  
    manual_intern    0.0579   54   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000:  
    Name             Secs     %    
    builtin_intern   0.0929   100  
    manual_intern    0.0393   42   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 10 000:  
    Name             Secs     %    
    builtin_intern   0.0854   100  
    manual_intern    0.0366   43   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 100 000:  
    Name             Secs     %    
    builtin_intern   0.0839   100  
    manual_intern    0.0338   40   
    
Python38:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10: 
    Name             Secs     %    
    builtin_intern   0.1202   100  
    manual_intern    0.1104   92   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100: 
    Name             Secs     %    
    builtin_intern   0.0746   100  
    manual_intern    0.0519   70   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000: 
    Name             Secs     %    
    builtin_intern   0.0586   100  
    manual_intern    0.035    60   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 10 000: 
    Name             Secs     %    
    builtin_intern   0.056    100  
    manual_intern    0.0311   56   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 100 000: 
    Name             Secs     %    
    builtin_intern   0.056    100  
    manual_intern    0.0305   55   
    
Python314:
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 10: 
    Name             Secs     %    
    builtin_intern   0.1501   100  
    manual_intern    0.1128   75   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 100: 
    Name             Secs     %    
    builtin_intern   0.0899   100  
    manual_intern    0.056    62   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 1 000: 
    Name             Secs     %    
    builtin_intern   0.0629   100  
    manual_intern    0.0353   56   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 10 000: 
    Name             Secs     %    
    builtin_intern   0.0555   100  
    manual_intern    0.0326   59   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 100 000: 
    Name             Secs     %    
    builtin_intern   0.0591   100  
    manual_intern    0.0301   51   

"""
