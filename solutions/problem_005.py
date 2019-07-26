def cons(a, b):
    def pair(f):
        return f(a,b)
    return pair

def car(cons):
    return cons(lambda x, y: x)

def cdr(cons):
    return cons(lambda x, y: y)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
