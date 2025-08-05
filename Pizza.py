print("Welcome to python Piza Deliveries")
size=(input("What sizes do you want S, M, L ? "))
Bill=0

if size=='S':
    Bill=15
elif size=='M':
    Bill=20
else:
    Bill=25

pep=input("Do you want pepricon on pizza or not? Y or N")
if pep=='Y':
   if size=='S':
     Bill+=2
   else:
      Bill+=3     

chhes=input("Do you want extra cheese or not Y or N")
if chhes=='Y':
    Bill+=1   
print(f"Tota Bill {Bill}")
   
