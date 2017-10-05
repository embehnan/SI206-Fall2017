import re

myfile=open('HW_5actual.txt')

actual_data=[line.strip() for line in myfile.readlines()]
integers=[]
for line in actual_data:
    y=re.findall("[0-9]+",line)
    if y != []:
        for string in y:
            num=int(string)
            integers.append(num)
            
print (sum(integers))
