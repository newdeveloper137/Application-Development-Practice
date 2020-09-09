#define variables
max_order = 100000.0
min_order = 10.0
price = 4.264

#get user input
order_amount = float(input("How many pounds of beef would you like to order?"))

#if statement for various situations
if order_amount > max_order:
    print(order_amount,"is more than currently available stock.")
elif order_amount < min_order:
    print(order_amount,"is below minimum order amount.")
else:
    order_price = str(round((price*order_amount),2))
    print(order_amount,"pounds costs $"+order_price)

#this is the end of the requirements, for fun and for learning purposes, I tried to make a function work for this

def beef_stuff(amount):
    order_amount = amount
    if order_amount > max_order:
        msg = str(order_amount) + " pounds is more than currently available stock. Try again."
        while msg == str(order_amount) + " pounds is more than currently available stock. Try again.":
            print(msg)
            order_amount = float(input("How many pounds of beef would you like to order?"))
            msg = beef_stuff(order_amount)
    elif order_amount < min_order:
        msg = str(order_amount) + " is below minimum order amount. Try again."
        while msg == str(order_amount) + " is below minimum order amount. Try again.":
            print(msg)
            order_amount = float(input("How many pounds of beef would you like to order?"))
            msg = beef_stuff(order_amount)
    else:
        order_price = str(round((price*order_amount),2))
        msg = str(order_amount) + " pounds costs $"+ order_price
        while msg == str(order_amount) + " pounds costs $" + order_price:
            print(msg)
            more_beef = input("Would you like to order more beef? (Yes/No)").lower()
            if more_beef == "yes":
                order_amount_2 = float(input("How many more pounds of beef would you like to order?"))
                if (order_amount + order_amount_2) > max_order:
                    msg = str(order_amount) + " pounds is more than currently available stock. Try again."
                    while msg == str(order_amount) + " pounds is more than currently available stock. Try again.":
                        print(msg)
                        print("You already have " + str(order_amount) + " pounds costing $" + str(order_price) + " ordered. Continue")
                        order_amount_2 = float(input("How many more pounds of beef would you like to order?"))
                        msg = beef_stuff(order_amount + order_amount_2)
                else:
                    msg = beef_stuff(order_amount + order_amount_2)
            elif more_beef == "no":
                msg = str(order_amount) + " pounds costs $" + order_price + ". Link to Checkout:"
            else:
                print("Invalid Entry. Must enter either Yes or No. Try again.".upper())
                msg = str(order_amount) + " pounds costs $" + order_price

    return msg

wants_beef = beef_stuff(float(input("How many pounds of beef would you like to order?")))
print(wants_beef)
