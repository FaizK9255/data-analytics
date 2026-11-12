# Outputs:
# Your total assets are [number]
# Your total debts are [number]
# Your net worth is [number]

realEstateAsset = 500000
vehicleAsset = 20000
bankAccountAsset = 50000

mortgageDebt = 300000
creditCardDebt = 10000
studentLoansDebt = 20000

print(f'Your total assets are { realEstateAsset + vehicleAsset + bankAccountAsset }')
print(f'Your total debts are { mortgageDebt + creditCardDebt + studentLoansDebt }')
print(f'Your networth is {(realEstateAsset + vehicleAsset + bankAccountAsset) - (mortgageDebt + creditCardDebt + studentLoansDebt)}')

