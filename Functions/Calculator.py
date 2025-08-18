
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

Operation ={
'+':add,
'-':substract,
'*':multiplication,
'/':division
}

m1=0
m2=int(input("Whats your first number: "))
o=input("Select your operation +,-,*,/")

Continue_Calution=True
while  Continue_Calution:
     result=Operation[o](m1,m2)
     print(result)

     Continue=input("Do you want to continue the calculation yes or no")

     if Continue=="yes":
            m1=result
            m2=int(input("Whats your first number: "))    
            o=input("Select your operation +,-,*,/")
     else:
          Continue_Calution=False            
          print("Calculation ends")



