# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:16:32 2019

@author: Raj Kumar, raj.kumar2208@yahoo.in
"""
#Question Description 
#Input a and b, such that a >= b

def gcd_strings(a, b):
    r =''
    if(a >= b):
        if((a % b)==0):
            return '1'+''.join('0')*(a-1)
        else:
            while True:
                r += gcd_strings(b, a % b)
                if(len(r) >= a):
                    break
            return r
    else:
        return '0'

if __name__ == "__main__":
    print(gcd_strings(3,1)[0:3])
    print(gcd_strings(3,2)[0:3])
    print(gcd_strings(5,2)[0:5])
    print(gcd_strings(10,4)[0:10])
    