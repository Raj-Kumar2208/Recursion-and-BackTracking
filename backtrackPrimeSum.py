# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:48:32 2019

@author: raj.kumar2208@yahoo.in

Given three numbers, SUM: S, PRIME P and Number of element N,
find ALL N prime P such that their sum is equal to S.

Sample Input 1: N =2, P=7, S = 28
Output 1: 11 17

Sample Input 2: N=3,P=2, S=23
Output 2: 3 7 13
          5 7 11

Sample Input 2: N=4, P=3, S=54
Output 2: 5 7 11 31
          5 7 13 29
          5 7 19 23
          5 13 17 19
          7 11 13 23
          7 11 17 19
"""

import math

def solve_problem(num, prime, temp, sum_num):
    if ((temp == sum_num) and (len(plist)==num)):
        print(" ".join(plist))
        return " ".join(plist)
    if (len(plist)==num or prime >= sum_num):
        return
    else:
        if(temp < sum_num):
            np = next_prime(prime)
            plist.append(str(np))
            solve_problem(num,np,temp+np,sum_num)
            plist.pop()
            solve_problem(num,np,temp,sum_num)
            
    

def next_prime(prime):
    if prime < 2:
        return 2
    found = False
    while not found:
        prime = prime+1
        if (is_Prime(prime) == True):
            found = True
    return prime

def is_Prime(n): 
      
    if(n <= 1): 
        return False
    if(n <= 3): 
        return True
    if(n % 2 == 0 or n % 3 == 0): 
        return False
      
    for i in range(5,int(math.sqrt(n) + 1), 6):  
        if(n % i == 0 or n % (i + 2) == 0): 
            return False
      
    return True

if __name__=="__main__":
    N = 4
    P = 3
    S = 54
    temp = 0
    plist = []
    solve_problem(N,P,temp,S)
