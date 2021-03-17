#Timothy Young, CS 350, HW7
##Compute the length of the longest common subsequence of sequences x,y.

#This file is the testing suite for comparing the brute force vs.
# the dynamic programming methods of computing the length of the 
#LCS. Please see report for empyrical analysis and theoretical assumptions.
from bruteForceLCS import *
from dynamicLCS import *
from test import *
import timeit

xAvg = ['A','G','G']
yAvg = ['G','A']

xAvg2 = ['A','G','G','A','G','T']
yAvg2 = ['G','A','G','A']

xAvg4 = ['A','G','G','A','G','T','A','G','G','A','G','T']
yAvg4 = ['G','A','G','A','G','A']

##Takes over 60s runtime. Uncomment if you dare!
##Used for average runtime analysis. Please see report.
#xAvg3 = ['A','G','G','A','G','A','G','A','T','A','G','T','A','G','G','A','G','A','G','A','T','A','G','T']
#yAvg3 = ['G','A','G','A','G','A','G','A','T','G','A','G','A','G','A','G','A','T']
###############################################################

xWorst = ['A','G']
yWorst = ['T','C']

xWorst2 = ['A','G','G','A']
yWorst2 = ['T','C','C','T']

xWorst3 = ['A','G','G','A','G','A','G','A']
yWorst3 = ['T','C','C','T','C','T','C','T']

xBest = ['A','B']
yBest = ['A']


if __name__ == "__main__":
    print("Best/Base Case Scenarios:")
    print("--------------------------")
    print("BF Best Case Length: ", bruteWrapper(xBest,yBest))

    print("Best Case Brute Force LCS Time: ", timeit.timeit('bruteWrapper(xBest,yBest)','from main import bruteWrapper,xBest,yBest',number = 10000),"fractional seconds")

    print('\n')

    print("Dynamic LCS Best Case Length: ", dynamicLCSLength(xBest,yBest))

    print("Best Case Dynamic LCS Time: ",timeit.timeit('dynamicLCSLength(xBest,yBest)','from main import dynamicLCSLength,xBest,yBest',number = 10000),"fractional seconds")
    print("------------------------------------------------------------------")
    print("Average Case Scenarios:")
    print("--------------------------")
    print('\n')

    print("BF Avg. Case Length: ", bruteWrapper(xAvg,yAvg))

    print("Avg Case Brute Force LCS Time: ", timeit.timeit('bruteWrapper(xAvg,yAvg)','from main import bruteWrapper,xAvg,yAvg',number = 10000),"fractional seconds")

    print('\n')

    print("Dynamic LCS Avg. Case Length: ", dynamicLCSLength(xAvg,yAvg))

    print("Avg. Case Dynamic LCS Time: ",timeit.timeit('dynamicLCSLength(xAvg,yAvg)','from main import dynamicLCSLength,xAvg,yAvg',number = 10000),"fractional seconds")

    print('\n')

    print("BF Avg. Case Length(n=6,m=2): ", bruteWrapper(xAvg2,yAvg2))

    print("Avg Case Brute Force LCS Time(n=6,m=2): ", timeit.timeit('bruteWrapper(xAvg2,yAvg2)','from main import bruteWrapper,xAvg2,yAvg2',number = 10000),"fractional seconds")

    print('\n')

    print("Dynamic LCS Avg. Case Length(n=6,m=2): ", dynamicLCSLength(xAvg2,yAvg2))

    print("Avg. Case Dynamic LCS Time(n=6,m=2): ",timeit.timeit('dynamicLCSLength(xAvg2,yAvg2)','from main import dynamicLCSLength,xAvg2,yAvg2',number = 10000),"fractional seconds")

    print('\n')
    print("BF Avg. Case Length(n=12,m=6): ", bruteWrapper(xAvg4,yAvg4))

    print("Avg Case Brute Force LCS Time(n=12,m=6): ", timeit.timeit('bruteWrapper(xAvg4,yAvg4)','from main import bruteWrapper,xAvg4,yAvg4',number = 10000),"fractional seconds")

    print('\n')

    print("Dynamic LCS Avg. Case Length(n=12,m=6): ", dynamicLCSLength(xAvg4,yAvg4))

    print("Avg. Case Dynamic LCS Time(n=12,m=6): ",timeit.timeit('dynamicLCSLength(xAvg4,yAvg4)','from main import dynamicLCSLength,xAvg4,yAvg4',number = 10000),"fractional seconds")

    print('\n')

    ##Takes 60s to complete runtime. #############################
    #print("BF Avg. Case Length(n=24,m=18):", bruteWrapper(xAvg3,yAvg3))

    #print("Avg Case Brute Force LCS Time(n=24,m=18): ", timeit.timeit('bruteWrapper(xAvg3,yAvg3)','from main import bruteWrapper,xAvg3,yAvg3',number = 10000),"fractional seconds")

    #print('\n')

    #print("Dynamic LCS Avg. Case Length(n=24,m=18): ", dynamicLCSLength(xAvg3,yAvg3))

    #print("Avg. Case Dynamic LCS Time(n=24,m=18): ",timeit.timeit('dynamicLCSLength(xAvg3,yAvg3)','from main import dynamicLCSLength,xAvg3,yAvg3',number = 10000),"fractional seconds")

    print("------------------------------------------------------------------")
    print("Worst-Case Scenarios:")
    print("--------------------------")
    print('\n')

    print("BF Worst Case Length: ", bruteWrapper(xWorst,yWorst))
    
    print("Worst Case Brute Force LCS Time: ", timeit.timeit('bruteWrapper(xWorst,yWorst)','from main import bruteWrapper,xWorst,yWorst',number = 10000),"fractional seconds")

    print('\n')

    print("Dynamic LCS Worst Case Length: ", dynamicLCSLength(xWorst,yWorst))

    print("Worst Case Dynamic LCS Time: ",timeit.timeit('dynamicLCSLength(xWorst,yWorst)','from main import dynamicLCSLength,xWorst,yWorst',number = 10000),"fractional seconds")

    print('\n')

    #print("Note: The average/worst case does not differ for the DP implementation")
    #print("------------------------------------------------------------------")
    #print("Worst-Case Experimental(Change Input Size):")
    #print("--------------------------")
    #print('\n')

    #print("BF Worst Case Length: ", bruteWrapper(xWorst2,yWorst2))
    
    #print("Worst Case Brute Force LCS Time: ", timeit.timeit('bruteWrapper(xWorst2,yWorst2)','from main import bruteWrapper,xWorst2,yWorst2',number = 10000),"fractional seconds")

    #print('\n')

    #print("Dynamic LCS Worst Case Length: ", dynamicLCSLength(xWorst2,yWorst2))

    #print("Worst Case Dynamic LCS Time: ",timeit.timeit('dynamicLCSLength(xWorst2,yWorst2)','from main import dynamicLCSLength,xWorst2,yWorst2',number = 10000),"fractional seconds")

    #print('\n')

    #print('\n')

    #print("BF Worst Case Length: ", bruteWrapper(xWorst3,yWorst3))
    
    #print("Worst Case Brute Force LCS Time: ", timeit.timeit('bruteWrapper(xWorst3,yWorst3)','from main import bruteWrapper,xWorst3,yWorst3',number = 10000),"fractional seconds")

    #print('\n')

    #print("Dynamic LCS Worst Case Length: ", dynamicLCSLength(xWorst3,yWorst3))

    #print("Worst Case Dynamic LCS Time: ",timeit.timeit('dynamicLCSLength(xWorst3,yWorst3)','from main import dynamicLCSLength,xWorst3,yWorst3',number = 10000),"fractional seconds")




















