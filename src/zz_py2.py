""" For python 2 specific things """

def prnt(*args, **kwargs):
    end = kwargs.pop('end', '\n')
    if end == '\n':
        print ' '.join(args)
    else:
        print ' '.join(args)+end,
