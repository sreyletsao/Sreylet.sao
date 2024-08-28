# EX2.Create function to sum odd number in array [1,2,3,4,5,6]
def sum(odd_num):
    sum=0
    for i in range(len(odd_num)):
        if odd_num[i]%2==1:
            sum+=odd_num[i]
    return sum
array= [1,2,3,4,5,6]
print(sum(array))
