#!/usr/bin/env python3
import numpy as np

class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

net = Network([2,3,1])
print("weights")
print(net.weights)
print("biases")
print(net.biases)


arr = [1,2,3,4,5]
print(arr[:-1])
print(arr[1:])
