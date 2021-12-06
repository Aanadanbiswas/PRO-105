import csv
import math

with open(r'standardDeviation.csv',newline= '') as df:
    dataReader = csv.reader(df)
    fileData = list(dataReader)

marksData = fileData[1]

def mean(data):
    total = 0
    for marks in data:
        total += int(marks)
    n = len(data)
    mean = total/n
    return mean

squaredList = []
for marks in marksData:
    a = int(marks)-mean(marksData)
    a = a**2
    squaredList.append(a)

sum = 0
for x in squaredList:
    sum += x

result = sum/len(marksData)-1
standardDeviation = math.sqrt(result)
print(standardDeviation)