day=input("enter any day between sunday and saturday :")
day=day.lower()
if day=="saturday" or day=="sunday":
    print("weekend")
else:
    print("weekday")