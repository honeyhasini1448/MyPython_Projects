Menu = {"sizzling brownie": 250,
        "donuts": 60,
        "icecream": 80,
        "cupcakes": 50,
        "chocolava cake": 70,
        "walnut brownie": 150,
        "cookies": 70,
        "waffles": 100
        }

Cart = []
total = 0 

print("-------------MENU--------------")
for key,value in Menu.items() :
    print(f"{key:20}:" + "\u20B9" + f"{value:.2f}")
print("-------------------------------")

while True : 
    order = input("Please Enter Your Order(q to quit): ").lower()
    if order == "q":
       break
    elif Menu.get(order) is not None :
       Cart.append(order)
print("----------YOUR ORDER-----------")
for order in Cart :
    total += Menu.get(order)
    print(order, end=" ")

print()
print("Total is:"+ "\u20B9"+ f"{total:.2f}")
print("-------------------------------")

