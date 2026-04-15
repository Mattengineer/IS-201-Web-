name = input("Enter salesperson name: ")
sales = float(input("Enter weekly sales amount: "))

# Decision logic
if sales < 1000:
    commission = sales * 0.10
elif sales < 5000:
    commission = sales * 0.20
else:
    commission = sales * 0.30

# Output

print("Name:", name)
print("Weekly Sales:", sales)
print("Commission:", commission)

