# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:14:03 2019

@author: raj.kumar2208@yahoo.in

Check string palindrom using recursive method
"""

def palindrome_recursive(string):
    char = []
    for i in string:
        char.append(i)
    solve(char)

def solve(char):
    if len(char) <= 1 and len(char) >=0:
        print("String is palindrome")
        return 0
    elif char[0]==char[-1]:
        solve(char[1:-1])
    else:
        print("String is not palindrome")
        return -1

if __name__ == "__main__":
    palindrome_recursive("abc")
    palindrome_recursive("abcacba")
    palindrome_recursive("abba")
    palindrome_recursive("abcd")
    palindrome_recursive("madam")
    palindrome_recursive("abaaba")
    