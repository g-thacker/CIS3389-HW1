print("####################################################")
print("#FILENAME:\t\ta1p2.py\t\t\t   #") 
print("#ASSIGNMENT:\t\tHomework Assignment 1 Pt. 2#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tWednesday, 12.February 2020#")
print("####################################################\n\n\n")

print("NUMBER\t\t\t\t\t SQUARE\n")
sum = 0
for i in range(5, 30):
    if i%5==0 and i!=10 and i!=15:
        print(i, "\t\t\t\t\t", (i*i))
        sum += (i*i)
print("\nSum of squares:\t\t\t\t", sum)
print("\n") #add a blank line before returning to command prompt
