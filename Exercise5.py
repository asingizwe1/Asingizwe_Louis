Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"]) 

Shoes["brand"] = "Adidas"
print(Shoes)

Shoes["type"] = "sneakers"
print(Shoes)

print(list(Shoes.keys()))

print(list(Shoes.values()))


if "size" in Shoes:
    print("Key 'size' exists.")
else:
    print("Key 'size' does not exist.")

for key, value in Shoes.items():
    print(key, ":", value)

Shoes.pop("color")
print(Shoes)

Shoes.clear()
print(Shoes) 


person = {
    "name": "Alice",
    "age": 28,
    "city": "Kampala"
}
person_copy = person.copy()
print(person_copy)


students = {
    "student1": {
        "name": "John",
        "age": 20
    },
    "student2": {
        "name": "Mary",
        "age": 22
    }
}
print(students)
