import csv
with open('Height-Weight.csv',newline='') as f :
    reader=csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []
for i in range(len(file_data)):
    num = file_data[i][1]
    newData.append(float(num))
n = len(newData)
total = 0
for x in newData :
    total = total+x
mean = total/n
print("Height Mean is "+ str(mean))

with open('Height-Weight.csv',newline='') as f :
    reader=csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []
for i in range(len(file_data)):
    num = file_data[i][2]
    newData.append(float(num))
n = len(newData)
total = 0
for x in newData :
    total = total+x
mean = total/n
print("Weight Mean is "+ str(mean))