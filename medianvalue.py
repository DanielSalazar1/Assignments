
power_arr = [4, 5, 2, 6, 3, 7, 8, 9, 6, 5, 2]

power_arr.sort()

a = int(input("please enter a number : "));
if (a % 2 == 0):
    print("This number is even")
else:
    print("This number is odd")

a = len(power_arr)
print("the number of items inside list is", a)

def find_middle(input_list):
    middle = float(len(input_list))/2
    return (input_list[int(middle)], input_list[int(middle-1)])

middle_value = 0
if (a % 2):
    print("This number is even")
    x, y = find_middle(power_arr)
    middle_value = (x + y) / 2
else:
    print("This number is odd")
    middle_index = float(len(power_arr))/2
    print("The middle index is", middle_index)
    middle_value = power_arr[int(middle_index - .5)]
print("The median is", middle_value)
