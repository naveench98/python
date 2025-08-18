tuple=(123.5,567.7)
available_products={"milk","bread","oil","powder"}
dict={
    "milk":10,
    "bread":50,
    "oil":160,
    "powder":25
}

print("Welcome to the kirana store")
basket=[]


while True:
    items=input(f"please enter the product{dict} or type done for total bil")
    if items=="done":
        break
    if items in available_products:
        basket.append(items)
    else:
        print("Sorry Currently we dont have these product")   
    total_bill=0
    for i in basket:
        total_bill+=dict[i]
print(f"your total bill is{total_bill}") 