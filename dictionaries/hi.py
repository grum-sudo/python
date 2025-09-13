capitals = {"USA" : "washington D.C",
            "india": "new delhi",
            "china": "beijing",
            "russia": "moscow"}

#print(help(capitals))
#print(dir(capitals))

#print(capitals.get"("USA"))

#if capitals.get("USA"):
#    print("that capital exists")#vscode is exploding rn 
#else:
#    print("that capital does not exist")

# capitals.update({"germany": "berlin"})
# capitals.update({"USA": "detroit"})
# capitals.pop("china")
# capitals.popitem()  

# keys = capitals.keys()
# for key in capitals.keys():
#    print(key)

# values = capitals.values()
# for value in capitals.values():
#    print(value)

#items = capitals.items()
#print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
    