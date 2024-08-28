# EX10.Show product name that has maximum price

# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def maximum(products):
    maximum=0
    name = ""
    for i in range(len(products)):
        if maximum==0:
            maximum=products[0]["price"]
            name=products[i]["name"]
        elif products[i]["price"] >maximum:
            maximum=products[i]["price"]
            name=products[i]["name"]
    return name
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},]
print(maximum(products)) 

        
