people = float(input("Enter how many people are going on tour: "))

vansNeeded = round(people/15)

vansCostperDay = vansNeeded * 250

costPerperson = vansCostperDay/people

print(f'With {people} amount of people going on tour, we would need {vansNeeded:.2f} vans.')
print(f'This would cost ${vansCostperDay:.2f} total, and ${costPerperson:.2f} per person. ')
