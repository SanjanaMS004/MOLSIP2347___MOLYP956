num={1,5,4,45,5,26,35,57,8,9}
num2={1,2,3,4,5,6,7,8}

print("set      : ",num)
num.add(15)
print("add      : ",num)
print("copy     : ",num.copy())
print("pop      : ",num.pop())
num.remove(26)
print("remove   : ",num)

print("isdisjoint: ",num.isdisjoint(num2))
print("issubset : ",num.issubset(num2))
print("issuperset: ",num.issuperset(num2))

union_Set=num.union(num2)
print("union    : ",union_Set)
new_set=num.intersection(num2)
print("intersection : ",new_set)
diff=num.difference(num2)
print("difference   : ",diff)
Sym_dif=num.symmetric_difference(num2)
print("symmetric diff: ",Sym_dif)
