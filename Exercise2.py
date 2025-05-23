x = ("samsung", "iphone", "tecno", "redmi")
print ('my favorite brand is', x[1])

print(x[-2])

x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)

x = x + ("Huawei",)
print(x)

for phone in x:
    print(phone)
    
    x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(x)

cities = ("Kampala", "Gulu", "Mbale", "Mbarara", "Fort Portal")
print(cities)

city1, city2, city3, city4, city5 = cities
print(city1, city2, city3, city4, city5)

print(cities[1:4]) 

first_names = ("John", "Mary", "Luke")
second_names = ("Smith", "Johnson", "Brown")
full_names = first_names + second_names
print(full_names)

colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print(colors_multiplied)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thistuple.count(8))  
