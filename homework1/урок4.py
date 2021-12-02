
#numbers = [1,2,3,4,5]
numbers2 = range(0,100)
for num in numbers2:
    print(num ** 2)

people = [("jack", "smith", 20, "tallin", "male"),("mary", "gold", 25 ,"london", "female"),("piere","summer", 30, "milan", "male"),("sarah", "simpson", 30,"new-york", "female")]


for person in people:
    if person[4] == "male":
        print(f"this is{person[0]},{person[1]}. he is {person[2]} yers old. he lives in {person[3]}")
    elif person[4] == "female":
        print(f"she is{person[0]},{person[1]}. he is {person[2]} yers old. he lives in {person[3]}")
#############

#
# for num in range(0,100):
#     if num % 5 == 0 and num % 3 == 0:
#         print(num,"fizzBuzz")
#     elif num % 5 == 0:
#         print(num,"Buzz")
#     elif num % 3 == 0:
#         print(num,"Fizz")

# while True
#     print("yes")


condition = True
while condition:
    print("hello")
