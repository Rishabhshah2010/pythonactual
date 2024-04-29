def printNumbersTail(n):
    if n > 0:
        printNumbersTail(n - 1)
        print(n)

printNumbersTail(10)
    