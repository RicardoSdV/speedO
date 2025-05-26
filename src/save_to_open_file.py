import pickle
from os.path import join

from src.z_data import data
from src.z_tester import auto_tester


num = data.M
path = join('bin', 'save_to_open_file.log')


def save_to_open_file():
    file = None
    try:
        file = open(path, 'w')
        write = file.write

        for el in data.yield_hun_chars(num):
            write(el)

    finally:
        if file: file.close()


def append_to_list():
    _list = []
    append = _list.append

    for el in data.yield_hun_chars(num):
        append(el)

    return _list

def append_and_save():
    _list = []
    append = _list.append

    for el in data.yield_hun_chars(num):
        append(el)

    with open(path, 'w') as file:
        file.writelines(_list)


def generator_save():
    with open(path, 'w') as file:
        file.writelines(data.yield_hun_chars(num))


auto_tester()


"""
Conclusion:

Python27:
Name                Secs     %    
save_to_open_file   0.2426   100  
append_and_save     0.2188   90   
generator_save      0.186    77   
append_to_list      0.0418   17   

Python38:
Name                  Secs     %    
append_and_save       0.6419   100  
generator_save        0.6257   97   
save_to_open_file     0.6249   97   
append_to_list        0.0359   6    

Python310:
Name                Secs     %    
append_and_save     0.6518   100  
generator_save      0.6327   97   
save_to_open_file   0.6317   97   
append_to_list      0.0391   6    



"""

