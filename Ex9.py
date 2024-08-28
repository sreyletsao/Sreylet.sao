# EX9.Create function to find average of price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def average(products):
    average=0
    for i in range(len(products)):
        average+=products[i]["price"]*10/100
    return average
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},]
print(average(products))
