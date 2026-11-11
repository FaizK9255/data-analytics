

mealCost = float(input('Enter the cost of the meal: $'))
tip = mealCost * 0.20
tax = mealCost * 0.0825
totalCost = mealCost + tip + tax


print('\n----- Meal Cost Breakdown -----')
print(f'Meal Cost:    ${mealCost: 10,.2f}')
print(f'Tip (20%):    ${tip: 10,.2f}')
print(f'Tax (8.25%):  ${tax: 10,.2f}')
print('-' * 30)
print(f'Total Cost:    ${totalCost: 10,.2f}')



