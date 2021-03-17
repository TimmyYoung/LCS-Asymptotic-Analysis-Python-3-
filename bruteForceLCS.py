#Timothy Young, CS 350, HW 7
##This is the brute force algorithm for computing the LCS. 
##Using recursion, we can backtrace through every element, essentially performing a BF search. Please see report for complexities.
def bruteWrapper(x = [], y = []):
    
    return bruteForceLCS(0,0,x,y)



def bruteForceLCS(i,j, x = [], y = []):
    if (i == len(x) or j == len(y)):##Default base case
        return 0

    if (x[i] == y[j]):
        return 1 + bruteForceLCS(i+1,j+1,x,y)##Add to the length calculation for the LCS.

    return max((bruteForceLCS(i+1,j,x,y),(bruteForceLCS(i,j+1,x,y)))##Iterate based on the max condition)

