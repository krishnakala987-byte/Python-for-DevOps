# break Statement Example

print("Break Example\n")

for number in range(1, 11):

    if number == 7:
        break

    print(number)

print("\nContinue Example\n")

for value in range(1, 6):

    if value == 3:
        continue

    print(value)