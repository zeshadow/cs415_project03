

def loadFile(filename):
    """
    Input:
        Filename

    Return:
        A list of integer values read in from a file
    """
    a = []
    with open(filename, 'r') as fp:
        for line in fp:
            line = line.strip() # strip all white spaces
            a.append(line) # append the 'string'

    a = [int(x) for x in a] # take the 'string' and turn it into an int

    return a # return the list of ints

def knapSack(F, capacity, valueList, weightList):
    """
    This must start at i = 1 & j = 1.
    Input:
        F = initalized list of values
        capacity = capacity of knapsack
        valueList = list of values
        weightList = list of weights

    This is a void function and just edits F.
    """

    for i in range(len(F)): # row
        for j in range(len(F[i])): # column
            value = 0 # compiler was complaining
            if F[i][j] == 0:
                if j < weightList[i]:
                    value = F[i-1][j]
                else:
                    value = max(F[i-1][j], valueList[i] + F[i-1][j-weightList[i]])
            F[i][j] = value
            # print value

    # return F[i][j]

    # return F



def subset(F,capacity,valueList, weightList):
    subset = []
    i = len(F) - 1  # Value list
    j = capacity - 1  # Weight list

    while i >= 0:

        val = F[i][j]

        if (valueList[i] + F[i - 1][j - weightList[i]]) == val:
            subset.append(i + 1)
            j = j - weightList[i]

        i = i - 1

        # done

    return subset






def main():
    capacity = loadFile('KnapsackTestData/p01_c.txt')
    capacity = int(capacity[0])
    value = loadFile('KnapsackTestData/p01_v.txt')
    weight = loadFile('KnapsackTestData/p01_w.txt')

    # Number of items in the list
    numOfItems = len(value)

    # Initializing array
    vec = [[0]*capacity for i in range(numOfItems)]
    # for i in range(numOfItems):
    #     vec[i][0] = 0

    knapSack(vec, capacity, value, weight)
    sub = subset(vec, capacity, value, weight)

    for i in vec:
        print(i)

    print("Optimal Value:" , vec[len(value)-1][capacity-1] )
    print("Optimal Subset:" , sub)

main()
