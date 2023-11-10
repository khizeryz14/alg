import numpy

def gaussJordan():
    n = int(input("Enter number of variables: "))
    myMatrix = numpy.zeros((n, n+1))

    for i in range(n):
        for j in range(n+1):
            myMatrix[i][j] = float(input('A['+str(i)+']'+'['+str(j)+']: '))
    print("Matrix before manipulation: ")
    print(myMatrix)

    try:
        for i in range(n):
            for j in range(n):
                if i != j:
                    ratio = myMatrix[j][i] / myMatrix[i][i]
                    for c in range(n+1):
                        myMatrix[j][c] = myMatrix[j][c] - ratio*myMatrix[i][c]
        print("The diagonal matrix is: ")
        print(myMatrix)
        answerList = []
    except RuntimeWarning as e:
        print(e)
        return 0

    for i in range(n):
        var = myMatrix[i][n] / myMatrix[i][i]
        answerList.append(var)
    i = 1
    for x in answerList:
        print("%s%d = %.2f" % ("Variable no.", i, x))
        i += 1

gaussJordan()
