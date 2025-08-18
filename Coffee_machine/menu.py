Menu={
    "expresso":{
        "ingredients":{
            "water":50,
            "coffe":18
        },
        "cost":1.5
    },
    
     "Latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffe":24
        },
        "cost":2.5
    },
     "Capacino":{
        "ingredients":{
            "water":240,
            "milk":100,
            "coffe":24
        },
        "cost":3.0
    }
    
}
Profit=0
Resources={
    "water":300,
    "milk":200,
    "coffe":100
}

def resources_available(order_ingredients):
   for items in order_ingredients:
      if items>=Resources[items]:
        print("We are god to serve")
      else:
        print("We dont have enough resources")  

def process_coins()

machine=True
while machine:
 choice=input("What would you like? (espresso/latte/cappuccino):")
 if choice== 'off':
    print("Turning off the machine")
    machine=False
 elif choice=='report':
    print(f"Water: {Resources['water']} ml")
    print(f"Milk: {Resources['milk']} ml")
    print(f"Coffe: {Resources['coffe']} ml")
    print(f"Money: {'profit'}")
 else:
  drink= Menu[choice]       
  if resources_available(drink["ingredients"]):
     