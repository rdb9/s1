#python program to find sum of cubes of smaller number  than the specified number
def sum_of_cubes(n):   #function definition
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
    return total
print("Sum of cubes of smaller number than the specified number: ",sum_of_cubes(3))  #function call

