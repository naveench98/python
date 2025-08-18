from prettytable import PrettyTable   # importing class
table = PrettyTable()  #creation of object
table.add_column("pokeman",['Pikachu','squartle'])  # methods
table.add_column("type",['electric','water']) # method
table.align="l"  # attributes
print(table)