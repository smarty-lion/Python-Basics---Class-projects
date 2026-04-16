# Calculate the percentage for the subjects

print("Enter the marks for the below subjects ")

math = float(input("Math : "))

latin = float(input("Latin : "))

english = float(input("English : "))

socialogy = float(input("Socialogy : "))

total = math + latin + english + socialogy

percentage = (total / 40) * 100

print(percentage)