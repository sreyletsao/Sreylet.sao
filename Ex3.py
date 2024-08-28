# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]

def max(num):
    max=num[0]
    for i in range(len(num)):
        if num[i]>max:
            max=num[i]
    return max
array =[2,3,5,0,11,5,2]
print(max(array))