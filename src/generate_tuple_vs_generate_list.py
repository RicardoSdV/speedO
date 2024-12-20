from src.z_data import data
from src.z_tester import tester_2d

def generator(inner):
    for el in inner:
        yield el

def gen_tup(outer):
    for inner in outer:
        result = tuple(generator(inner))

def gen_list(outer):
    for inner in outer:
        result = list(generator(inner))

if __name__ == '__main__':
    tester_2d(
        (
            gen_tup,
            gen_list,
        ),
        list_3d=data.slower_3d_list,
        testing_what='times',
    )

    tester_2d(
        (
            gen_tup,
            gen_list,
        ),
        list_3d=data.slower_3d_list,
        testing_what='memories'
    )

"""
Conclusion:
    - Generating a tuple surprisingly fast.
    Python27:
    
        Testing times:

        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Secs     %    
        gen_list   4.6187   100  
        gen_tup    4.1833   91   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Secs     %    
        gen_list   2.3947   100  
        gen_tup    2.2947   96   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Secs     %    
        gen_list   1.851    100  
        gen_tup    1.8313   99   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Secs     %    
        gen_tup    1.7527   100  
        gen_list   1.6747   96   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Secs     %    
        gen_tup    1.7833   100  
        gen_list   1.7243   97   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Secs     %    
        gen_list   2.6883   100  
        gen_tup    2.2843   85   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Secs     %    
        gen_list   2.8417   100  
        gen_tup    2.235    79   
        
        
        Testing memories:
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Mibs     %    
        gen_tup    0.0391   100  
        gen_list   0.0      0    
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Mibs    %    
        gen_tup    0.013   100  
        gen_list   0.0     0    
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Mibs     %    
        gen_list   0.0755   100  
        gen_tup    0.0247   33   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Mibs     %    
        gen_tup    0.1432   100  
        gen_list   0.1419   99   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Mibs     %    
        gen_tup    1.1576   100  
        gen_list   0.2331   20   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Mibs      %    
        gen_list   19.5013   100  
        gen_tup    16.9766   87   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Mibs       %    
        gen_list   191.6146   100  
        gen_tup    179.1237   93   
    
    
    Python38:
        Testing times:
        - Tuple mostly slightly faster
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Secs     %    
        gen_list   2.6729   100  
        gen_tup    2.5613   96   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Secs     %    
        gen_tup    1.945    100  
        gen_list   1.9245   99   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Secs     %    
        gen_list   1.7056   100  
        gen_tup    1.6353   96   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Secs     %    
        gen_list   1.6699   100  
        gen_tup    1.5987   96   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Secs     %    
        gen_list   1.7421   100  
        gen_tup    1.7248   99   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Secs     %    
        gen_list   2.6439   100  
        gen_tup    2.2691   86   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Secs     %    
        gen_list   3.041    100  
        gen_tup    2.3625   78   
        
        
        Testing memories:
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Mibs     %    
        gen_tup    0.1133   100  
        gen_list   0.0      0    
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Mibs     %    
        gen_list   0.0065   100  
        gen_tup    0.0039   60   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Mibs     %    
        gen_tup    0.0729   100  
        gen_list   0.0677   93   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Mibs     %    
        gen_tup    0.2461   100  
        gen_list   0.0638   26   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Mibs     %    
        gen_tup    1.3138   100  
        gen_list   0.0312   2    
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Mibs      %    
        gen_tup    18.2057   100  
        gen_list   17.4583   96   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Mibs       %    
        gen_list   209.7461   100  
        gen_tup    155.2643   74   

    Python312:
        Testing times:
        - Tuple gen always faster

        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Secs     %    
        gen_list   2.8322   100  
        gen_tup    2.6107   92   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Secs     %    
        gen_list   3.0475   100  
        gen_tup    2.2303   73   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Secs     %    
        gen_list   2.2498   100  
        gen_tup    2.0045   89   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Secs     %    
        gen_list   2.0949   100  
        gen_tup    1.9841   95   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Secs     %    
        gen_list   2.0968   100  
        gen_tup    2.0863   100  
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Secs     %    
        gen_list   3.1181   100  
        gen_tup    2.7246   87   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Secs     %    
        gen_list   3.5211   100  
        gen_tup    2.8034   80   
        
        
    Testing memories:
    - Tuple generally less memory specially for more elements, the 100k I can't explain

    Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
    Name       Mibs     %    
    gen_tup    0.0664   100  
    gen_list   0.0      0    
    
    Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
    Name       Mibs   %    
    gen_tup    0.0    100  
    gen_list   0.0    0    
    
    Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
    Name       Mibs     %    
    gen_tup    0.0117   100  
    gen_list   0.0052   44   
    
    Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
    Name       Mibs     %    
    gen_list   0.2174   100  
    gen_tup    0.1536   71   
    
    Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
    Name       Mibs     %    
    gen_tup    1.9414   100  
    gen_list   0.0898   5    
    
    Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
    Name       Mibs      %    
    gen_list   19.9245   100  
    gen_tup    18.0729   91   
    
    Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
    Name       Mibs       %    
    gen_list   200.1471   100  
    gen_tup    177.1641   89   

    PyPy313:
        - Lists just better
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Secs     %    
        gen_tup    0.9841   100  
        gen_list   0.759    77   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Secs     %    
        gen_tup    0.5287   100  
        gen_list   0.5173   98   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Secs     %    
        gen_tup    0.5795   100  
        gen_list   0.5118   88   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Secs     %    
        gen_tup    1.1068   100  
        gen_list   0.9717   88   
        1
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Secs     %    
        gen_tup    3.2439   100  
        gen_list   1.0278   32   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Secs     %    
        gen_tup    2.8083   100  
        gen_list   2.594    92   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Secs     %    
        gen_tup    4.4804   100  
        gen_list   2.1537   48   
        
        
        Testing memories:
        
        Average of 3 rounds, len(outer_list) = 10 000 000, len(inner_list) = 10: 
        Name       Mibs     %    
        gen_tup    0.2695   100  
        gen_list   0.0326   12   
        
        Average of 3 rounds, len(outer_list) = 1 000 000, len(inner_list) = 100: 
        Name       Mibs     %    
        gen_tup    2.9284   100  
        gen_list   1.1055   38   
        
        Average of 3 rounds, len(outer_list) = 100 000, len(inner_list) = 1 000: 
        Name       Mibs      %    
        gen_tup    111.069   100  
        gen_list   47.6393   43   
        
        Average of 3 rounds, len(outer_list) = 10 000, len(inner_list) = 10 000: 
        Name       Mibs        %    
        gen_list   1904.9388   100  
        gen_tup    1227.8542   64   
        
        Average of 3 rounds, len(outer_list) = 1 000, len(inner_list) = 100 000: 
        Name       Mibs        %    
        gen_tup    3229.8594   100  
        gen_list   919.8177    28   
        
        Average of 3 rounds, len(outer_list) = 100, len(inner_list) = 1 000 000: 
        Name       Mibs        %    
        gen_tup    6147.599    100  
        gen_list   2219.4115   36   
        
        Average of 3 rounds, len(outer_list) = 10, len(inner_list) = 10 000 000: 
        Name       Mibs        %    
        gen_tup    6546.7253   100  
        gen_list   6386.7266   98   

"""
