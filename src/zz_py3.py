""" For python 3 specific things """

def prnt(*args, **kwargs):
    end = kwargs.pop('end', '\n')
    print(*args, end=end)

vzip = zip
vrange = range
