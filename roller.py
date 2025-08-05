print("Welcome to the Rollar Coaster");
height = int(input("Please enter your height"))
Bill=0

if height>120:
      print("you can enjoy the ride")
      age=int(input("What's your age"))
      if age<=12:
            print("please pay 12")
            Bill=12
      elif age <=18:
            print("please pay 8")
            Bill=8
      else:
            print("Please pay 5")
            Bill=5
      phote=(input("if you want phote while ridind please enter Y if not N"))
      if phote=='Y':
            Bill+=3
            print(f"Your Total bill is {Bill}")
            
else:
      print("As your height is not matching you are not eligible for roller")