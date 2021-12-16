from collections import Counter
import csv 
with open("Height-Weight.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData=[]
for i in range(len(file_data)):
    extract = file_data[i][1]
    newData.append(extract)
data = Counter(newData)
dataRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if 50 < float(height) < 60 :
        dataRange["50-60"] = dataRange["50-60"]+occurence
    elif 60 < float(height) <70:
        dataRange["60-70"] += occurence
    elif 70 < float(height) <80:
        dataRange["70-80"] += occurence
modeRange,modeOccurence = 0,0
for range,occurence in dataRange.items():
    if occurence>modeOccurence:
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float((modeRange[0]+modeRange[1])/2)
print(f"Mode Is {mode:2f}")
