import matplotlib.pyplot as plt
import numpy as np

def activation_function(x):
    if x < 0.0:
        return -1.0
    else:
        return 1.0
"""
rnge = np.linspace(-10.0, 10.0, num=1000)
values = [activation_function(i) for i in rnge]
plt.plot(rnge, values)
plt.show()"""


def perceptron(input, weights):
    sum_of_input_times_weight = sum([i * w for i,w in zip(input,weights)])
    output =  activation_function(sum_of_input_times_weight)
    return output

# print(perceptron([1,2,3,4,5],[1,1,2,1,1]))

def predict(inp_vec,weights):
    """
    inp_vec:
        An input vector consisting of sepal length
    return:
        A class label, either 1 for 'setosa' or -1
    """
    class_label = perceptron(inp_vec,weights)
    return class_label

weights = [-2.60105969, 3.61349319]

# new flowers
assert predict([5.6, 4.8], weights) == 1
assert predict([3.4, 4.1], weights) == 1
assert predict([5.8, 1.9], weights) == -1
assert predict([6.2, 2.4], weights) == -1

# flowers we already know
assert predict([5.4,  3.9], weights) == 1
assert predict([5.7,  4.4], weights) == 1