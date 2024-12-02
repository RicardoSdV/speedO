import sys

def dict_growth():
    _dict = {}
    prev_size = sys.getsizeof(_dict)
    prev_num_elements = 0
    print('%8s %8s %8s' % ('Num el', 'Diff', 'Size'))

    for i in range(1000):
        _dict[i] = i
        size = sys.getsizeof(_dict)
        if size != prev_size:
            num_elements = i + 1
            difference = num_elements - prev_num_elements
            print('%8d %8d %8d' % (num_elements, difference, size))
            prev_size = size
            prev_num_elements = num_elements

dict_growth()


"""
Conclusion:
    There seems to be no rhyme nor reason to list growth rates

    Python27:
        Num el     Diff     Size
        6          6        1040
        22         16       3344
        86         64       12560
        342        256      49424
    
    Python38 & 310:
          Num el     Diff     Size
           1        1      232
           6        5      360
          11        5      640
          22       11     1176
          43       21     2272
          86       43     4696
         171       85     9312
         342      171    18520
         683      341    36960
    
    Python312:
      Num el     Diff     Size
           1        1      224
           6        5      352
          11        5      632
          22       11     1168
          43       21     2264
          86       43     4688
         171       85     9304
         342      171    18512
         683      341    36952
"""
