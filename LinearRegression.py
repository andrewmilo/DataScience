from statistics import mean
import numpy as np
import matplotlib.pyplot as plt

print range(1,7)
x_axis = np.array(range(1,7), dtype=np.float64)
y_axis = np.array([5,4,6,5,6,7], dtype=np.float64)

def fit_linear_model(x,y):
    # returns m(slope) & b(y-intercept)
    m = (mean(x)*mean(y) - mean(x*y)) / (mean(x)**2 - mean(x**2))  
    b = mean(y) - m*mean(x)
    return m, b

def linear_prediction(x,m,b):
    # value for x, given m & b
    return m*x+b

def squared_error(y_vals, best_fit_line):
    return sum((best_fit_line-y_vals)**2)

def coefficient_of_determination(x_vals, y_vals):
    avg_y = [mean(y_vals) for y in y_vals]
    # sq_error =

# y = mx + b
m, b = fit_linear_model(x_axis,y_axis)
best_fit_line = [linear_prediction(x,m,b) for x in x_axis]

x = 8
y = linear_prediction(x,m,b)
plt.scatter(x, y)

plt.scatter(x_axis,y_axis)
plt.plot(x_axis, best_fit_line)
plt.show()