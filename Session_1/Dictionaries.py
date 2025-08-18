#Dictionaries
Captial = {
    "France":"bro"
}

travel_log ={
    "France":["Breakfast","lunch","Dinner"]
}
nested_list={
    "Italy":["A","B",["C","D"]],
    "visted_places":{
        "cities":["newyotk","road"],
             } # type: ignore
    }


print(Captial["France"])
print(travel_log["France"][1])
print(nested_list["visted_places"]["cities"][1])


