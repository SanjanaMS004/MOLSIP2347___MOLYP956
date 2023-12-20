D={"name":"joey",
    "Lastname":"geller",
    "age": 22,
    "place":"Mysore",
    "color":"blue"
    }

#accessing val
print("name     : ",D['name'])

#adding/updating k-val pair
D['name']='Ross'
print("updated  :",D)

print("Keys     : ",D.keys())
print("values   : ",D.values())
print("items    : ",D.items())
print("Copy     : ",D.copy())
print("length   : ",len(D))
print("get()    : ",D.get("age"))

D.popitem()
print("popitem  : ",D)
D.pop("Lastname")
print("Pop method:",D)

print("clear    : ",D.clear())

