names = ['peter','Tom','James','Kevin','Okello'] 
print(names[1])

names[0] = 'Brian'
print(names[0])

names.append('Owen')
print(names)

names.insert(2,'Bathel')
print(names)

del names[3]
print(names)

print(names[-1])

colors = ['red','orange','green','purple','black','pink','white']
print(colors[2:5])

countries = ['Uganda','Kenya','Rwanda','Burundi','Tanzania']
countries_copy = countries.copy()
print(countries_copy)

for country in countries:
    print(country)
    
    animals = ['cheeter','lion','zebra','ostrich','elephant']
    animals.sort()
print("Ascending:", animals)

animals.sort(reverse=True)
print("Descending:", animals)

for animal in animals:
    if 'a' in animal:
        print(animal)
        
first_names = ['Ariho','Ajuna', 'Kato']
second_names = ['Derrick', 'Peter', 'Francis']
full_names = first_names + second_names
print(full_names)
