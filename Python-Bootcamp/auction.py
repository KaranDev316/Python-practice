print("Welcome to the silent auction program!")
names = []
amounts = []
bidders = True
while bidders:
    name = input("What is your name? ")
    amount = int(input("How much would you like to bid? "))
    names.append(name)
    amounts.append(amount)
    bidder = input("Are there any bidders? Type 'yes' or 'no' ")
    if bidder.lower() == "no":
        bidders = False

max_amount = amounts[0]
position = 0
for i in range(len(amounts)):
    if amounts[i] > max_amount:
               max_amount = amounts[i]
               position = i

print(f"The highest bidder is  {names[position]} with {max_amount} bids.")



