name = input("Name of Sender? --> ")
item = input("Type of Item? ---> ")

is_fragile = bool(input("Is it Fragile? (Enter \"yes\" if yes, enter \"no\" if no) ---> ") == "yes")

weight = float(input("Weight of the item (in kg) ---> "))
distance = float(input("The distance (In km) ----> "))

is_express = bool(input("Express? (Enter \"yes\" if yes, enter \"no\" if no) --> ") == "yes")

is_international = bool(input("International? (Enter \"yes\" if yes, enter \"no\" if no) --> ") == "yes")


base_cost = (weight * 2.50) + (distance * 0.15)
print("==============================================")
if weight <= 2 and distance <= 100 and not is_express and not is_international:
    print("Free Shipping!!")
    Total = 0

elif is_international and is_express:
    print("International Express is applied")
    Total = (base_cost * 1.4) + 50

elif (is_express or is_international) and weight > 20:
    print("Express or Heavy International is applied")
    Total = (base_cost * 1.2) + 25

elif weight > 30 or distance > 1000:
    print("Oversized is applied")
    Total = base_cost + 30

else:
    Total = base_cost
    print("Standard rate is applied")

Shippingfee = Total - base_cost


print("==============================================")
print("Name of the sender:", name)
print("Type of Item:", item)
print("Item Weight is:", weight)
print("The Distance is:", distance)
print("Is it Fragile?:", is_fragile)
print("Express?:", is_express)
print("Is it international?:", is_international)
print("The Shipping fee cost:", Shippingfee)
print("Total of your order:", Total, "php")
print("==============================================")

