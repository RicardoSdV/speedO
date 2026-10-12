from src.z_tester import auto_tester_2d


def use_setdefault_newEntries(outer):
    for inner in outer:
        d = {}; setD = d.setdefault
        for el in inner:
            setD(el, el)

def use_literals_newEntries(outer):
    for inner in outer:
        d = {}
        for el in inner:
            if el in d:
                d[el]
            else:
                d[el] = el


def use_setdefault_dupes(outer):
    for inner in outer:
        d = {}; setD = d.setdefault
        for el in inner:
            setD(1, 1)

def use_literals_dupes(outer):
    for inner in outer:
        d = {}
        for el in inner:
            if 1 in d:
                d[1]
            else:
                d[1] = 1



auto_tester_2d(segregator='end')


"""
Conclusion:
Why would you need this: t1 = (1, 2); t2 = (1, 2); d = {t1: t1}; assert id(d.setdefault(t2, t2)) == id(t1)

In python3 simple, use .setdefault, its faster.

In python27 it depends how many duplicates vs new entries you expect.


Python27:
    Dupes:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                   Secs     %    
        use_setdefault_dupes   0.3667   100  
        use_literals_dupes     0.324    88   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2957   100  
        use_literals_dupes     0.2677   91   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2907   100  
        use_literals_dupes     0.2617   90   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                   Secs    %    
        use_setdefault_dupes   0.289   100  
        use_literals_dupes     0.263   91   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2913   100  
        use_literals_dupes     0.26     89   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2897   100  
        use_literals_dupes     0.2597   90   
    
    New entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.48     100  
        use_literals_newEntries     0.4213   88   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.3997   100  
        use_literals_newEntries     0.3743   94   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.3667   100  
        use_literals_newEntries     0.3477   95   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.5673   100  
        use_literals_newEntries     0.5007   88   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.5097   100  
        use_literals_newEntries     0.478    94   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.549    100  
        use_literals_newEntries     0.5323   97   
        
Python38:
    Dupes:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                   Secs     %    
        use_literals_dupes     0.2337   100  
        use_setdefault_dupes   0.2197   94   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                   Secs     %    
        use_literals_dupes     0.2062   100  
        use_setdefault_dupes   0.1755   85   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1991   100  
        use_setdefault_dupes   0.1671   84   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1996   100  
        use_setdefault_dupes   0.1661   83   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                   Secs     %    
        use_literals_dupes     0.194    100  
        use_setdefault_dupes   0.1648   85   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1929   100  
        use_setdefault_dupes   0.1643   85   

    New Entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                        Secs     %    
        use_literals_newEntries     0.3043   100  
        use_setdefault_newEntries   0.2718   89   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                        Secs     %    
        use_literals_newEntries     0.2796   100  
        use_setdefault_newEntries   0.2478   89   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2663   100  
        use_setdefault_newEntries   0.2263   85   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2581   100  
        use_setdefault_newEntries   0.2186   85   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                        Secs    %    
        use_literals_newEntries     0.463   100  
        use_setdefault_newEntries   0.413   89   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.5029   100  
        use_setdefault_newEntries   0.4483   89   
        
Python314:
    Dupes:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                   Secs     %    
        use_literals_dupes     0.265    100  
        use_setdefault_dupes   0.2547   96   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                   Secs     %    
        use_literals_dupes     0.2201   100  
        use_setdefault_dupes   0.1902   86   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2153   100  
        use_setdefault_dupes   0.1817   84   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2166   100  
        use_setdefault_dupes   0.1814   84   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2194   100  
        use_setdefault_dupes   0.1857   85   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2195   100  
        use_setdefault_dupes   0.1842   84   
    
    New Entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                        Secs     %    
        use_setdefault_newEntries   0.293    100  
        use_literals_newEntries     0.2824   96   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                        Secs     %    
        use_literals_newEntries     0.2581   100  
        use_setdefault_newEntries   0.2394   93   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2636   100  
        use_setdefault_newEntries   0.2288   87   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2575   100  
        use_setdefault_newEntries   0.2207   86   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.49     100  
        use_setdefault_newEntries   0.4332   88   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.5068   100  
        use_setdefault_newEntries   0.4543   90   


"""
