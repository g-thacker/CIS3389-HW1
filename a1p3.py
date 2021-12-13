print("####################################################")
print("#FILENAME:\t\ta1p3.py\t\t\t   #") 
print("#ASSIGNMENT:\t\tHomework Assignment 1 Pt. 3#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tWednesday, 12.February 2020#")
print("####################################################\n\n\n")

sum = 0
for i in range(1,6):
    print("\nMONTH ", i, "\n--------")
    sum += float(input("Enter rainfall for month: "))

print("\n\n")

if sum >= 20:
    print(sum, " inches:\nPLENTY RAINFALL")
elif sum >= 15:
    print(sum, " inches:\nMODERATELY HIGH RAINFALL")
elif sum >= 10:
    print(sum, " inches:\nMODERATELY LOW RAINFALL")
else:
    print(sum, " inches:\nLOW RAINFALL")

print("\n\n") #add blank line before return to prompt
