# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:41:51 2019

@author: raj.kumar2208@yahoo.in
"""

import numpy as np


def basic_constraints(x,y):
    if((x < N) & (x >= 0) & (y < N) & (y >= 0)):
        return True
    else:
        return False

def movements(matrix,x,y,size):
    global length
    global track
    if (size > length):
        length = size
    track[x][y]=1
    size += 1
    for i in range(8):
        new_x = x+x_corr[i]
        new_y = y+y_corr[i]
        if basic_constraints(new_x,new_y):
            if (matrix[new_x][new_y]==1 & track[new_x][new_y]==0):
                movements(matrix,new_x,new_y,size)
    track = np.zeros((N,N),dtype='int32')
                

# rite to find 1st "1" in given matrix #no using this function
#def find_one(matrix,i,j):
#    if matrix[i][j]==1:
#        return (i,j,True)
#    else:
#        if((j < N-1)):
#            find_one(matrix,i,j+1)
#        else:
#            j=0
#            if (i < N-1):
#                find_one(matrix,i+1,j)
#            else:
#                return (0,0,False)
    

def start_solution(matrix,N):
    global length
    for i in range(N):
        for j in range(N):
            if matrix[i][j]==1:
                movements(matrix,i,j,0)
    if(length==0):
        print("We don't find any 1 in matrix for length calculation")
    else:
        print('largest length is: '+length)

if __name__=="__main__":
    #matrix = np.array((N,N),dtypes='int32')
    matrix = np.array([[1,1,0,0,0],
                        [0,1,1,0,0],
                        [0,0,1,0,1],
                        [1,0,0,0,1],
                        [0,1,0,1,1]])
    
    x_corr=[1, 1, 0, -1, -1, -1, 0, 1]
    y_corr=[0, 1, 1, 1, 0, -1, -1, -1]
    
    N=5
    length=1
    track=np.zeros((N,N),dtype='int32')
    start_solution(matrix,N)
    
