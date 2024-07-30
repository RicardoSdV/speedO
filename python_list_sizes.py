import sys

def list_growth():
    lst = []
    prev_size = sys.getsizeof(lst)
    prev_num_elements = 0
    print('%8s %8s %8s' % ('Num el', 'Diff', 'Size'))

    for i in range(1000):
        lst.append(i)
        size = sys.getsizeof(lst)
        if size != prev_size:
            num_elements = i + 1
            difference = num_elements - prev_num_elements
            print('%8d %8d %8d' % (num_elements, difference, size))
            prev_size = size
            prev_num_elements = num_elements

list_growth()


"""
Conclusion:
    There seems to be no rhyme nor reason to list growth rates

    Python27:
        Num el     Diff     Size
           1        1       96
           5        4      128
           9        4      192
          17        8      264
          26        9      344
          36       10      432
          47       11      528
          59       12      640
          73       14      768
          89       16      912
         107       18     1072
         127       20     1248
         149       22     1448
         174       25     1672
         202       28     1928
         234       32     2216
         270       36     2536
         310       40     2896
         355       45     3304
         406       51     3760
         463       57     4272
         527       64     4848
         599       72     5496
         680       81     6232
         772       92     7056
         875      103     7984
         991      116     9024
     
    Python38:
        Num el     Diff     Size
           1        1       88
           5        4      120
           9        4      184
          17        8      256
          26        9      336
          36       10      424
          47       11      520
          59       12      632
          73       14      760
          89       16      904
         107       18     1064
         127       20     1240
         149       22     1440
         174       25     1664
         202       28     1920
         234       32     2208
         270       36     2528
         310       40     2888
         355       45     3296
         406       51     3752
         463       57     4264
         527       64     4840
         599       72     5488
         680       81     6224
         772       92     7048
         875      103     7976
         991      116     9016

    Python310 & 312:
        Num el     Diff     Size
           1        1       88
           5        4      120
           9        4      184
          17        8      248
          25        8      312
          33        8      376
          41        8      472
          53       12      568
          65       12      664
          77       12      792
          93       16      920
         109       16     1080
         129       20     1240
         149       20     1432
         173       24     1656
         201       28     1912
         233       32     2200
         269       36     2520
         309       40     2872
         353       44     3256
         401       48     3704
         457       56     4216
         521       64     4792
         593       72     5432
         673       80     6136
         761       88     6936
         861      100     7832
         973      112     8856
"""
