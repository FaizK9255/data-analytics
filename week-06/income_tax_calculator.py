# Faiz Khan
# 11/16/2026
# Year Up United - Data Analytics

# Define constants for the tax rate, standard deduction, and dependent deduction.
taxRate = 0.20
standardDeduction = 10000
dependantDeduction = 2000

# Display the program title and a divider line.
print(f'{"Income Tax Calculator":^30}')
print("-" * 30)

# Prompt for gross annual income and convert it to a float.
grossAnnualIncome = float(input("Provide gross annual income: $"))

# Prompt for the number of dependents and convert it to an int.
numberOfDependants = int(input("Provide number of dependants: "))

# Calculate the dependent deductions and the total deductions.
dependantCalculations = dependantDeduction * numberOfDependants

totalDeductions = dependantCalculations + standardDeduction

# Calculate the taxable income
taxableIncome = grossAnnualIncome - totalDeductions

estimatedIncomeTax = taxableIncome * taxRate

# Display the income tax summary, with monetary values formatted to two decimal places.
print()
print(f'{"Income Tax Summary":^30}')
print("-" * 30)
print(f'Gross Annual Income: ${grossAnnualIncome:,.2f}')
print(f'Standard Deduction: ${standardDeduction:,.2f}')
print(f'Dependent Deduction: ${dependantCalculations:,.2f}')
print(f'Total Deductions: ${totalDeductions:,.2f}')
print(f'Taxable Income: ${taxableIncome:,.2f}')
print(f'Estimated Income Tax: ${estimatedIncomeTax:,.2f}')