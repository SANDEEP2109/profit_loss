def item():
    item_name = input("Enter the item name: ")
    return item_name

def item_cost_price():
    while True:
        cost_price = input("Enter the cost price of item: ")
        if cost_price.isdigit():
            cost_price=float(cost_price)
            if 0< cost_price:

                break
            else:
                print("cost price should be greater than zero")
        else:
            print("please enter the numbers")

    return cost_price

def item_sell_price():
    while True:
        sell_price = input("Enter the sell price of item: ")
        if sell_price.isdigit():
            sell_price = float(sell_price)
            if sell_price >0:

                break
            else:
                print("sell price should be greater than zero")
        else:
            print("please enter the numbers")

    return sell_price

def profit(cost_price, sell_price):
    if sell_price > cost_price:
        a = sell_price - cost_price
        print(f"Your profit is {a}")
    elif sell_price < cost_price:
        b = cost_price - sell_price
        print(f"You are at the loss of {b}")
    else:
        print("no profit and no loss")

def profit_percentage(cost_price, sell_price):
    if sell_price > cost_price:
        p = ((sell_price - cost_price) / cost_price) * 100
        print(f"Your profit percentage is {p}%")





def main():
    item_name = item()
    cost_price = item_cost_price()
    sell_price = item_sell_price()
    profit(cost_price, sell_price)
    profit_percentage(cost_price, sell_price)
if __name__ == '__main__':
    main()


