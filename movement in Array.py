# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:44:25 2019

@author: raj.kumar2208@yahoo.in
"""
import numpy as np

def basic_constraints(x):
    if ((x < N) & (x >= 0)):
        return True
    else:
        return False

def start_solution(array,M,t):
    if((M==0)&(t!=N-1)):
        return False
    if((M==0)&(t==N-1)):
        return True
    for i in prime:
        if(array[t]%i==0):
            l = [i,-i]
            for j in range(2):
                if basic_constraints(t+l[j]):
                    if (start_solution(array,M-1,t+l[j])):
                        return True
            print('a')
            break
    return False
        
    

if __name__ == "__main__":
    prime = [2,3,5,7,11,13,17,19]
    T = int(input())
    for j in range(T):
        N = int(input())
        arr = input()
        M = int(input())
        array=arr.split()
        array=list(map(int, array)) 
        if start_solution(array,M,0):
            print("YES")
        else:
            print("NO")
    
