price = int(input("Enter your price: "))
tax = 10

tax_calculation = price * tax/100
final_price =price + tax_calculation
print("Final: ", final_price)