#Solution2
#Make a Grocery List for supermarket shopping with name, price and quantity
groceryList = [[], [], []]
name = groceryList[0]
price = groceryList[1]
quantity = groceryList[2]

#Ask the user his/her budget initially
while True:
    try:
        budget = float(input("Enter Your budget : "))
        temp = budget
    except:
        print("\nPlease enter a valid value of the budget!")
        continue
    else: 
        break

choice = 1
while(choice ==1):
    try:
        print("1.Add an item")
        print("2.Exit")
        choice = int(input("Enter your choice : "))
        print()
    except:
        print("\nPlease enter a valid value of the choice!")
        continue
    else: 
        if(choice==1 and temp>0):
            itemName = input("Enter product : ")
            itemQuantity = input("Enter quantity : ")
            itemPrice = float(input("Enter Price : "))
            print()
            
            if(itemPrice>temp):
                print("Can't Buy the product ###(because budget left is ",temp,")")
                print()
                continue
            else:
                if(itemName not in name):
                    name.append(itemName)
                    quantity.append(itemQuantity)
                    price.append(itemPrice)
                    
                    temp = budget - sum(price)
                    print("Amount left : ", temp)
                    print()
                else:
                    itemIndex = name.index(itemName)
                    del quantity[itemIndex]
                    quantity.insert(itemIndex, itemQuantity)
                    del price[itemIndex]
                    price.insert(itemIndex, itemPrice)
                    
                    temp = budget - sum(price)
                    print("Amount left : ", temp)
                    print()
        elif(temp<=0):
            print("No more budget left!\n")
        else:
            break

for p in price:
    if(p<=temp):
        ind = price.index(p)
        print("Amount left can buy you ", name[ind])

print("\nGROCERY LIST is: \n")
headings = ["Product name", "Quantity", "Price"]
data = [name, quantity, price]
format_row = "{:>15}" * (len(headings) + 1)
print(format_row.format("", *headings))
for h, row in zip(headings, data):
    print(format_row.format(h, *row))
