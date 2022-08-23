#Import random

#Create the function below:

def matrixBuilder(item):
    matriz = []
    for x in range(0,item):
        matriz.append([1]*item)
    return matriz

print(matrixBuilder(3))