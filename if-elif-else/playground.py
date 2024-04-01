age = 16#int(input("Enter your age: ")) # 16
income = 40000#float(input("Enter your annual income: ")) # 80000

if age >= 18: # false
    if income < 50000:
        category = "Low Income Adult"
    elif 50000 <= income < 100000:
        category = "Middle Income Adult"
    else:
        category = "High Income Adult"
else:
    if income < 20000:
        category = "Low Income Minor"
    elif 20000 <= income < 50000:
        category = "Middle Income Minor"
    else:
        category = "High Income Minor"

print(f"You are in the category: {category}")
