import math
num = int(input("Enter any number: "))
result = 0
num_list = []

for i in range(num):
    result = result + i
    num_list.append(i)

size = len(num_list)
avarage = result / size

print(avarage)
print(result)