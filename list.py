list1= ["yellow","orange","red"]
print("original List   :  ",list1)

list1.append("blue")
print("appended List   :  ",list1)

list1.extend(["black","white"])
print("Extended List   :  ",list1)

list1.reverse()
print("reversed List   :  ",list1)

list1.sort()
print("Sorted List     :  ",list1)

list1.insert(0,"green")
print("insert operation:  ",list1)

list1.remove("green")
print("remove operation:  ",list1)
 
list1.pop()
print("pop operation   :  ",list1)

list1.pop(0)
print("pop op at pos 0 :  ",list1)

c=list1.copy()
print("copy of List    :  ",c)

a=list1.count("black")
print("count of 'black':  ",a)

b=list1.index("red")
print("indes of 'red'  :  ",b)
 
list1.clear()
print("List after clear() op:",list1)