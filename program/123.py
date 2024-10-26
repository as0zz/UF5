import numpy
def f(x):
    return numpy.sin(numpy.exp(x)) * (x ** 0.5)
value = 1
s = f(value)
print(value, s)