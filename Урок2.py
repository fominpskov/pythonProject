string_sample1 = "Hello world world"
string_sample2 = "first letteR is towERcase"
string_sample3 = " extral whitespace string "
string_sample4 = "der Fluß"

print(len(string_sample1))
print(string_sample1[::3])
print(string_sample1[-5:])
print(string_sample1[17:1:-1])
print(string_sample1[::-1])
sliced_string = print(string_sample1[6:11])

print("world" in string_sample1)
print("World" in string_sample1)
print(string_sample1.upper())
print(string_sample4.lower())
print(string_sample4.casefold())
print(string_sample1.lower())
print(string_sample1.casefold())
print(string_sample2.capitalize())


#
string_sample3.strip()
string_sample1.replace("world" , "planet")
string_sample1.split("w")
a,b,c = string_sample1.split()
print(string_sample1.count( "world" ))
print(string_sample1.rfind("world"))


a = "hello"
b = "World"

salary = 1000
text = "John salary is {0},{1},{2}"
pr#int(text.format(salary,a,b))

prise_string = "this{product} coste{price} euro"
print(prise_string.format(product="computer",price=1000))


a = 1000
b = john
c = true

print((f"my name is{b}. I am "))