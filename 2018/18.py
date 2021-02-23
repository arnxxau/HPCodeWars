import numpy

size = int(input(""))
matrix = numpy.zeros((size, size))
counter = 0
loop = 0

for i in range(0, size):
    arrayParticle = list(map(str, input().split()))
    for p in range(0, len(arrayParticle)):
        matrix[i][p] = arrayParticle[p]

matrix = numpy.flipud(matrix)
techShots = int(input(""))
while loop != techShots:
    loop = loop + 1
    shotArray = input("").split(" ")
    shotX = int(shotArray[0])
    shotY = int(shotArray[1])

    if matrix[shotY][shotX] == 1:
        counter = counter + 1
        matrix[shotY][shotX] = 0

print(counter)
