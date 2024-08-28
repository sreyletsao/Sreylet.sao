# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def sum(products):
    sum=0
    
    for i in range(len(products)):
            sum+=products[i]["price"]
    return sum
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},]
print(sum(products))



# def sum_total_price(products):
#     total_price = 0
#     for product in products:
#         total_price += product["price"]
#     return total_price

# # Example usage:
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

# total = sum_total_price(products)
# print("Total price:", total)