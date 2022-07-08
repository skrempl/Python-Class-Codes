# First Assignment for Python Course!
# Extra Credit: don't let $ break your code. Tip: google replacement function

bill = input("What is your total bill? ")
bill= float(bill.replace("$", ""))

print(f"Suggested tip is ${round(bill * 0.15, 2)} for 15%, ${round(bill * 0.18, 2)} for 18%, and ${round(bill * 0.2, 2)} for 20%")