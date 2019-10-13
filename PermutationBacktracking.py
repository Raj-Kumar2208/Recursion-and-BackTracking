# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:24:58 2019

@author: raj.kumnar2208@yahoo.in

Problem: Given a string,  Print all the permutation of string

Sample Input: abc
Sample Output: abc acb bac cab bca cba

"""

def permutation(string):
    char = []
    for i in string:
        char.append(i)
    size = len(char)
    solve(char,0,size)

def solve(char,start,end):
    if start == end:
        print(to_string(char))
    else:
        for i in range(start,len(char)):
            char = swap(char,start,i)
            solve(char,start+1,end)
            char = swap(char,start,i)

def to_string(char):
    return "".join(char)

def swap(char,i,j):
    temp = char[i]
    char[i] = char[j]
    char[j] = temp
    return char

if __name__ == "__main__":
    string = input("Enter the string: ")
    permutation(string)