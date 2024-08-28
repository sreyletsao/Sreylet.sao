# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]
def min(num):
    min=num[2]
    for i in range(len(num)):
        if num[i]<min:
            min=num[i]
    return min
array =[2,3,5,0,11,5,2]
print(min(array))