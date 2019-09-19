
temperatures_arr = [21, 23, 26, 22, 25, 20, 19, 23]

i = 0
max = 0
while i < 8:
   temp = temperatures_arr[i]
   i = i + 1
   if temp > max:
       max = temp
print("maximum is", max)

min = max
while i < len(temperatures_arr):
    temperature = temperatures_arr[i]
    i = i + 1
    if temperature < min:
        min = temperature
print("minimun is", min)
