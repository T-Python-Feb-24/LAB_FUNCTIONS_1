def triangle(n:int):
    '''
    numbers in triangle
    '''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()

triangle(int(input("enter number:")))
print(triangle.__doc__)