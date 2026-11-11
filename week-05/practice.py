item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.67
item5 = 45.60

subTotal = item1 + item2 + item3 + item4 + item5
tax = subTotal * 0.07
totalCost = subTotal + tax

print(f'Sub-Total = ${subTotal: .2f}')
print(f'      Tax = ${tax: .2f}')
print(f'Total Cost = ${totalCost: .2f}')