#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:15:35 2018

@author: shrey.aryan
"""
import math 
import matplotlib.pyplot as plt
import PowerTree
def bin_pow(x,n):
    if n == 0: return 1
    if n == 1: return x
    tmp = bin_pow(x,n//2)
    tmp = tmp*tmp
    if n%2 == 0: return tmp
    return tmp*x

def cost_bin_pow(n):
    if n == 0: return 0
    if n == 1: return 0
    tmp = cost_bin_pow(n//2)
    if  n%2 == 0: return 1 + tmp 
    return 2 + tmp

# test case 
#for i in range(10):
#   print (cost_bin_pow(i))
    
def quartic_pow(x,n):
    if n == 0: return 1
    if n == 1: return x
    if n == 2: return x*x
    if n == 3: return x*x*x
    L = [1,x,x*x,x*x*x]
    return quartic_pow_aux(x,n,L)
    
def quartic_pow_aux(x,n,L):
    tmp = quartic_pow_aux(x,n//4,L)
    tmp = tmp*tmp*tmp*tmp
    if n%4 == 0: return tmp 
    return tmp*L[n%4]

def cost_quartic_pow_aux(n):
    if n < 4: return 0
    tmp = cost_quartic_pow_aux(n//4)
    if n%4 == 0: return tmp + 2
    return 3 + tmp 
    
def cost_quartic_pow(n):
    if n == 0 or n == 1: return 0
    if n == 2: return 1
    if n == 3: return 2
    return 2 + cost_quartic_pow_aux(n)
    
# test case 
#for i in range(10):
#    print (cost_quartic_pow(i))
 
def smallest_factor(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return i
    return -1

def factor_pow(x,n):
    if n == 0: return 1
    if n == 1: return x
    if n >= 2 and smallest_factor(n) == -1: return factor_pow(x,n-1)*x
    if n >= 2 and smallest_factor(n) != -1:
        p = smallest_factor(n)
        q = n/p
        return factor_pow(factor_pow(x,p),q)

def cost_factor_pow(n):
    if n == 0: return 0
    if n == 1: return 0
    if smallest_factor(n) == -1 and n >= 2: return 1+cost_factor_pow(n-1)
    if smallest_factor(n) != -1 and n >= 2: 
        p = smallest_factor(n)
        q = n/p
        return cost_factor_pow(p) + cost_factor_pow(q)
    
def power_from_chain(x,a):
    l = len(a) - 1
    arr = {1:x}
    for k in range(1,l+1):
        a_i = a[k] - a[k-1]
        a_j = a[k-1]
        arr[a[k]] = arr[a_i] * arr[a_j]
    return arr[a[l]]

#print (power_from_chain(2,[1, 2, 3, 6, 12, 15]))

def power_tree_chain(n):
    if n == 1: return [1]
    p = PowerTree.PowerTree()
    while n not in p.parent:
        p.add_layer()
    return p.path_from_root(n)


def power_tree_pow(x,n):
    return power_from_chain(x,power_tree_chain(n))


def cost_power_tree_pow(n):
    a = power_tree_chain(n)
    return len(a) - 1


index = []
c_b = []
c_f = []
c_p = []
for i in range(2,100):
    index.append(i)
    c_b.append(cost_bin_pow(i))
    c_f.append(cost_factor_pow(i))
    c_p.append(cost_power_tree_pow(i))
    
plt.plot(index,c_b,label = 'Binary Cost')
plt.plot(index,c_f,label = "Factor Power Cost")
plt.plot(index,c_p,label = "Power Tree Cost")  
plt.legend()
plt.show()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    