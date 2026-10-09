from src.z_tester import auto_tester_2d


def use_setdefault_newEntries(outer):
    d = {}; setD = d.setdefault
    for inner in outer:
        for el in inner:
            setD(el, el)

def use_literals_newEntries(outer):
    d = {}
    for inner in outer:
        for el in inner:
            if el in d:
                d[el]
            else:
                d[el] = el


def use_setdefault_dupes(outer):
    d = {}; setD = d.setdefault
    for inner in outer:
        for el in inner:
            setD(1, 1)

def use_literals_dupes(outer):
    d = {}
    for inner in outer:
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
        use_setdefault_dupes   0.3273   100  
        use_literals_dupes     0.299    91   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                   Secs     %    
        use_setdefault_dupes   0.294    100  
        use_literals_dupes     0.2603   89   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2907   100  
        use_literals_dupes     0.261    90   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2913   100  
        use_literals_dupes     0.262    90   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2937   100  
        use_literals_dupes     0.2613   89   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                   Secs     %    
        use_setdefault_dupes   0.2953   100  
        use_literals_dupes     0.263    89   
    
    New entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.3327   100  
        use_literals_newEntries     0.2993   90   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100:  
        Name                        Secs     %    
        use_setdefault_newEntries   0.2907   100  
        use_literals_newEntries     0.26     89   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000:  
        Name                        Secs     %    
        use_literals_newEntries     0.3497   100  
        use_setdefault_newEntries   0.334    96   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000:  
        Name                        Secs     %    
        use_literals_newEntries     0.375    100  
        use_setdefault_newEntries   0.3427   91   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000:  
        Name                        Secs     %    
        use_literals_newEntries     0.3823   100  
        use_setdefault_newEntries   0.349    91   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000:  
        Name                        Secs     %    
        use_literals_newEntries     0.3843   100  
        use_setdefault_newEntries   0.363    94   
        
Python38:
    Dupes:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                   Secs     %    
        use_literals_dupes     0.2257   100  
        use_setdefault_dupes   0.1926   85   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                   Secs     %    
        use_literals_dupes     0.2048   100  
        use_setdefault_dupes   0.1727   84   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1982   100  
        use_setdefault_dupes   0.1676   85   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2016   100  
        use_setdefault_dupes   0.1685   84   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1971   100  
        use_setdefault_dupes   0.1675   85   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                   Secs     %    
        use_literals_dupes     0.1978   100  
        use_setdefault_dupes   0.1687   85   

    New Entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                        Secs     %    
        use_literals_newEntries     0.2189   100  
        use_setdefault_newEntries   0.1964   90   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                        Secs     %    
        use_literals_newEntries     0.2069   100  
        use_setdefault_newEntries   0.1777   86   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2484   100  
        use_setdefault_newEntries   0.1972   79   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2712   100  
        use_setdefault_newEntries   0.2027   75   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2735   100  
        use_setdefault_newEntries   0.2121   78   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2955   100  
        use_setdefault_newEntries   0.2286   77   
        
Python314:
    Dupes:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                   Secs     %    
        use_literals_dupes     0.2413   100  
        use_setdefault_dupes   0.2096   87   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                   Secs     %    
        use_literals_dupes     0.2177   100  
        use_setdefault_dupes   0.1848   85   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2178   100  
        use_setdefault_dupes   0.1802   83   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2184   100  
        use_setdefault_dupes   0.181    83   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2198   100  
        use_setdefault_dupes   0.1843   84   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                   Secs     %    
        use_literals_dupes     0.2212   100  
        use_setdefault_dupes   0.187    85   
    
    New Entries:
        Average of 3 rounds, len(outer) = 1 000 000, len(inner) = 10: 
        Name                        Secs     %    
        use_literals_newEntries     0.2247   100  
        use_setdefault_newEntries   0.204    91   
        
        Average of 3 rounds, len(outer) = 100 000, len(inner) = 100: 
        Name                        Secs     %    
        use_literals_newEntries     0.1979   100  
        use_setdefault_newEntries   0.1788   90   
        
        Average of 3 rounds, len(outer) = 10 000, len(inner) = 1 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2403   100  
        use_setdefault_newEntries   0.2034   85   
        
        Average of 3 rounds, len(outer) = 1 000, len(inner) = 10 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2599   100  
        use_setdefault_newEntries   0.2149   83   
        
        Average of 3 rounds, len(outer) = 100, len(inner) = 100 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.2628   100  
        use_setdefault_newEntries   0.219    83   
        
        Average of 3 rounds, len(outer) = 10, len(inner) = 1 000 000: 
        Name                        Secs     %    
        use_literals_newEntries     0.281    100  
        use_setdefault_newEntries   0.2389   85   


"""
