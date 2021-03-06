import pandas as pd
import numpy as np

df = pd.read_csv('simrank.csv', sep=',')

ones = df[df['class'] == 1]['score']
zeros = df[df['class'] == 0]['score']

dataFrameOnes = pd.DataFrame(data=ones, dtype=np.float64)
dataFrameZeros = pd.DataFrame(data=zeros, dtype=np.float64)

meanOnes = dataFrameOnes['score'].mean()
meanZeros = dataFrameZeros['score'].mean()

print(meanOnes)
print(meanZeros)

value = 0.0009
a = 0
b = 1

normValue = (b - a) * (value - meanZeros) / (meanOnes - meanZeros) + a
print(normValue)

if normValue >= 1.0:
	finalValue = 1.0
elif normValue <= 0.0:
	finalValue = 0.0
else:
	finalValue = normValue

print(finalValue)
