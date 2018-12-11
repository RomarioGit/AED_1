from random import shuffle
from time import time

def bubble_sort(vetor):
    fim = len(vetor)
    while fim > 1:
        i = 0
        while i < fim -1:
            if vetor[i] > vetor[i+1]:
                temp = vetor[i+1]
                vetor[i+1] = vetor[i]
                vetor[i] = temp
            i+=1
        fim -= 1
vetor = list(range(0,10000))
shuffle(vetor)
print(vetor)
antes = time()
bubble_sort(vetor)
depois = time()
print(depois)
print(vetor)



