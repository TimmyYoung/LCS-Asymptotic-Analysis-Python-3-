#Timothy Young, CS 350, HW 7
##This is the dynamic programming approach to finding the length
## of the LCS. Please see report for relevant complexities and 
## theoretical assumptions. 
import numpy as np

def dynamicLCSLength(x = [], y = []):
    m = len(x)
    n = len(y)

    C = [[None]*(n+1) for i in range(m+1)]##Forming the matrix to hold all of the subsequences generated.

    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j == 0):##Start the matrix with leading 0's
                C[i][j] = 0
            elif((x[i-1])==(y[j-1])):
                C[i][j] = C[i-1][j-1] + 1           
            else:
                C[i][j] = max(C[i-1][j],C[i][j-1])
    return C[m][n]##The last element of the matrix is the longest subsequence.



    