pressure_arr = [80, 90, 100, 150, 120, 110, 160, 110, 100]

sum = 0
for pressure in pressure_arr:
    sum = pressure + sum
    length = len(pressure_arr)
    mean = sum / length
print("The mean is", mean)
