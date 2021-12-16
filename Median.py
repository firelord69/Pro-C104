import csv
with open('Height-Weight.csv',newline='') as f:
    reader=csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []
for i in range(len(file_data)):
    extract = file_data[i][1]
    newData.append(extract)
newDatalen = len(newData)
newData.sort()
if newDatalen %2 == 0:
    median1 = float(newData[newDatalen//2])
    median2 = float(newData[newDatalen//2-1])
    median = (median1+median2)/2
else:
    median = newData(newDatalen//2)
    print(newDatalen)
print("Median Is "+str(median))