beverages = {"soda", "water", "juice"}
print(beverages)

beverages.add("liqour")
beverages.add("milkshake")
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

mySet.remove("kettle")
print(mySet)

for item in mySet:
    print(item)
    
mySet = {"apple", "banana", "cherry", "mango"}
myList = ["orange", "grape"]
mySet.update(myList)

ages = {8,20,25}
names ={"Dorcus", "Winnie", "Britah"}
combined_set = ages.union(names)
print(combined_set)