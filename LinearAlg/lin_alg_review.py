import math

def add_vectors(v1, v2):
    return [n1 + n2 for n1, n2 in zip(v1,v2)]

def subtract_vectors(v1,v2):
    return [n1 - n2 for n1, n2 in zip(v1,v2)]

def multiply_vector(v1, x):
    return [x * y for y in v1]

def dot_product(v1,v2):
    return sum([n1 * n2 for n1, n2 in zip(v1,v2)])

def sum_of_squares(v):
    return sum([v1 * v2 for v1, v2 in zip(v,v)])

def sum_of_squares2(v):
    return dot_product(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

v1 = [1,2,3]
v2 = [41,23,52]

print add_vectors(v1,v2)
print dot_product(v1,v2)
print sum_of_squares2(v1)
print subtract_vectors(v1,v2)
print magnitude(v1)