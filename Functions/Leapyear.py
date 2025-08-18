def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")

# Test the function
leap(2100)   # 2100 is NOT a leap year
leap(1999)   # 2000 IS a leap year
