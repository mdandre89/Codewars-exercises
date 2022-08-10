import functools
def chained(*ls):    
    def functio(*args):
        return reduce(lambda args, func: func(args), ls[0], *args)
    return functio