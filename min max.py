import numpy
N,M = (int(i) for i in input().split())
M = numpy.array([[int(i) for i in input().split()] for j in range(N)])
arr_min = numpy.min(M,axis=1)
print(numpy.max(arr_min))

