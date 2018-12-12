# Gradient Descent
from __future__ import division
import random
from math import sqrt

def step_fn(v, direction, step_size):
    """
    Moves step_size in a direction from v
    Parameters:
        v - a position vector
        direction - a direction vector
        step_size - size of the steps we take from v to (v+direction)
    Returns:
        A new vector that is displaced from v by step_size * direction.
    """
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v,direction)]

def gradient_fn(v):
    """
    Gradient function.
    """
    def mean_squares(v):
        """
        Returns mean of vector values.
        """
        return mean([v_i**2 for v_i in v])

    return [2 * v_i for v_i in v]

def distance(v1,v2):
    return sqrt(
        sum([(v1_i - v2_i)**2 for v1_i, v2_i in zip(v1,v2)])
    )

# starting vector point
v = [random.randint(-25,25) for i in xrange(3)]

tolerance = .000000000000000001

while True:
    gradient = gradient_fn(v)
    next_point = step_fn(v, gradient, -0.01)
    
    if distance(next_point, v) < tolerance:
        break
    
    v = next_point

print v