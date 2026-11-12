bill = float(input("Provide a bill amount: "))
tipPercentage = float(input("Provide the tip percentage: "))

tip = bill * (tipPercentage / 100)

print(f'The tip on a ${bill: .2f} restaurant bill is ${tip: .2f}')