# Task7. Menu Problem: Menu Using Functions
price_list = [100,500,200,400]

def add_price(price_list,price):
    price_list.append(price)
    return price_list
def get_average_price(price_list):
    total = 0
    for val in price_list:
        total += val
    return total/len(price_list)
def get_max_price(price_list):
    highest = price_list[0]
    for val in price_list:
        if val > highest:
            highest = val
    return highest
        
while True:
    print("1. Add Price")
    print("2. Show average price")
    print("3. Show highest price")
    print("4. Quit")
    choice = input("Enter your desired option: ")
    if choice == "1":
        price = int(input("Please enter price you want to add: "))
        add_price(price_list, price)
    elif choice == "2":
        print(get_average_price(price_list))
    elif choice == "3":
        print(get_max_price(price_list))
    elif choice == "4":
        break
    else:
        print("Invalid Input")
