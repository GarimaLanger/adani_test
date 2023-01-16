import random
def matrix_random(r, c):
    return [[random.randrange(0, 101) for i in range(c)] for j in range(r)]

r = int(input("Enter rows"))
c = int(input("Enter columns"))
print(matrix_random(r, c))
