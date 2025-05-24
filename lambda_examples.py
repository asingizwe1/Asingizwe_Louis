#use lambda tp get sqaure
square = lambda x: x**2
print(square(5))
add = lambda x,y:x+y
print(add(5,10))


numbers = [1,2,3,4,5]
#lambda will just help with single task of having number squared then it can be done throught the list 
squared = list(map(lambda x: x**2, numbers))