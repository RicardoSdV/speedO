from src.z_tester import auto_tester_2d


def use_id(outer):
    for inner in outer:
        for el in inner:
            _id = id(el)

class _Counter(object):
    def __init__(self):
        self.id = 0

    def next_id(self):
        self.id += 1
        return self.id

_counter = _Counter()
_next_id = _counter.next_id

def inc_id(outer):
    for inner in outer:
        for el in inner:
            _id = _next_id()


auto_tester_2d()

"""
Conclusion:
Yeah, if you need a unique id for something using its object Id is faster than an incrementing integer,

Python27:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
    Name     Secs     %    
    inc_id   0.8683   100  
    use_id   0.2753   32   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
    Name     Secs     %    
    inc_id   0.8107   100  
    use_id   0.2387   28   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
    Name     Secs    %    
    inc_id   0.798   100  
    use_id   0.239   30   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
    Name     Secs     %    
    inc_id   0.803    100  
    use_id   0.2407   30   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
    Name     Secs     %    
    inc_id   0.8017   100  
    use_id   0.238    30   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
    Name     Secs    %    
    inc_id   0.808   100  
    use_id   0.238   28   

Python38:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name     Secs     %    
    inc_id   0.6991   100  
    use_id   0.2322   33   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name     Secs     %    
    inc_id   0.6633   100  
    use_id   0.2083   31   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name     Secs     %    
    inc_id   0.6631   100  
    use_id   0.2014   30   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name     Secs     %    
    inc_id   0.6683   100  
    use_id   0.2069   31   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name     Secs     %    
    inc_id   0.6671   100  
    use_id   0.2033   30   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name     Secs     %    
    inc_id   0.651    100  
    use_id   0.2023   31   

Python314:
    Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
    Name     Secs     %    
    inc_id   0.3649   100  
    use_id   0.2169   59   
    
    Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
    Name     Secs     %    
    inc_id   0.3437   100  
    use_id   0.1931   56   
    
    Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
    Name     Secs     %    
    inc_id   0.3505   100  
    use_id   0.1979   56   
    
    Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
    Name     Secs     %    
    inc_id   0.3553   100  
    use_id   0.2032   56   
    
    Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
    Name     Secs     %    
    inc_id   0.3569   100  
    use_id   0.2069   57   
    
    Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
    Name     Secs     %    
    inc_id   0.3573   100  
    use_id   0.2051   56   

"""
