# -*- coding: utf-8 -*-
"""hw2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VEZGJ_itQ4zebNgdZoaNTuvp1LkvQXxQ
"""

import numpy as np
from scipy.misc import derivative
from math import sin, cos


## Problem 1

def f(x):
  return 1/x

def f1(x,c):
  return x + c

def deriv_f1(x):
  return 1

def f2(x):
  return x*x

def f3(x):
  return sin(x)

def f4(x, c):
  return c*x

def deriv_f4(c):
  return c

def deriv(f, x):
  return derivative(f, x, dx=1e-6)

x1 = 0
w1 = 2
x2 = 0
w2 = 1

x2w2_out = cos(w2*x2)+2
forward_x1 = np.zeros(6)

print("The input: x1={}, w1={}, x2={}, w2={}\n".format(x1,w1,x2,w2))

for i in range(6):
  forward_x1[0] = x1
  forward_x1[1] = f4(forward_x1[0], w1)
  forward_x1[2] = f3(forward_x1[1])
  forward_x1[3] = f2(forward_x1[2])
  forward_x1[4] = f1(forward_x1[3], x2w2_out)
  forward_x1[5] = f(forward_x1[4])

print("Forward calculation for x1:\t\t", forward_x1)

back_x1 = np.ones(6)
for i in range(6):
  back_x1[5] = 1
  back_x1[4] = back_x1[5] * deriv(f, forward_x1[4])
  back_x1[3] = back_x1[4] * deriv_f1(forward_x1[3])
  back_x1[2] = back_x1[3] * deriv(f2, forward_x1[2])
  back_x1[1] = back_x1[2] * deriv(f3, forward_x1[1])
  back_x1[0] = back_x1[1] * deriv_f4(forward_x1[0])
  
print("Back propagation for x1:\t\t", back_x1)
print("partial derivative with respect to x1:\t\t", back_x1[0])


forward_w1 = forward_x1.copy()
forward_w1[0] = w1
print("\nForward calculation for w1:\t\t", forward_w1)

back_w1 = np.ones(6)
for i in range(6):
  back_w1[5] = 1
  back_w1[4] = back_w1[5] * deriv(f, forward_w1[4])
  back_w1[3] = back_w1[4] * deriv_f1(forward_w1[3])
  back_w1[2] = back_w1[3] * deriv(f2, forward_w1[2])
  back_w1[1] = back_w1[2] * deriv(f3, forward_w1[1])
  back_w1[0] = back_w1[1] * deriv_f4(forward_w1[0])
  
print("Back propagation for x1:\t\t", back_w1)
print("partial derivative with respect to x1:\t\t", back_w1[0])

## Problem 2

w = np.array([[0.1,0.2,0.3],[-0.4,0.5,0.6],[-0.7,-0.8,0.9]])
x = np.array([[1],[1],[1]])


def L2(yhat, y):
    t = np.abs(yhat-y).flatten()
    loss = np.dot(t, t)/y.size
    return loss

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))    
    return s

def matrix_mul(first, second):
  return np.matmul(first, second)


## Derivatives of all functions used from above
def L2_prime(x):
  return 2*x

def sigmoid_derivative(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)    
    return ds

## todo TEST IT LATER
def mul_x_derivative(x, q):
  result = []
  for i in q:
    t = i * x.flatten()
    result = np.append(result, t)
  return np.reshape((x.size, q.size))
  


wx = matrix_mul(w, x)
sig = sigmoid(wx)
l2_loss = L2(sig, x)
print("Forward calculation:", l2_loss)


before_l2 = 2*sig*sig*1
before_sig = before_l2 * (1-sig) * sig
back_result = np.matmul(w.T, before_sig)
print("Final result for back propagation:\n", back_result)
