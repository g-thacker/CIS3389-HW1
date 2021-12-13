print("####################################################")
print("#FILENAME:\t\ta1p1.py\t\t\t   #") 
print("#ASSIGNMENT:\t\tHomework Assignment 1 Pt. 1#")
print("#COURSE/SECTION:\tCIS 3389.251\t\t   #")
print("#DUE DATE:\t\tWednesday, 12.February 2020#")
print("####################################################\n\n\n")

cont = 'y'

while cont.lower() == 'y' or cont.lower() == 'yes':
    total = 0
    avg = 0

    number1 = float(input("First number:\t"))
    number2 = float(input("Second number:\t"))
    number3 = float(input("Third number:\t"))
    
    total = number1 + number2 + number3
    avg = total/3

    
    if number1 >= number2 and number1 >= number3:
        first_largest = number1
        if number2 >= number3:
            second_largest = number2
            third_largest = number3
        else:
            second_largest = number3
            third_largest = number2
    elif number1 >= number2 and number1 < number3:
        first_largest = number3
        second_largest = number1
        third_largest = number2
    elif number1 < number2 and number1 < number3:
        third_largest = number1;
        if number2 >= number3:
            first_largest = number2
            second_largest = number3
        else:
            first_largest = number3
            second_largest = number2
    elif number1 < number2 and number1 >= number3:
        first_largest = number2
        second_largest = number1
        third_largest = number3
    
    print("\n\nSecond largest number entered:\t", second_largest)
    print("Average:\t\t\t", avg, "\n\n")
    cont = input("Would you like to continue? ")
