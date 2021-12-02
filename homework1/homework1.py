#homework2_strenger
# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(len(example_string1))
print(str(example_string1[0:2])+(example_string1[-2:]))



# Write a code to return "Jack is my name"

example_string2 = "jack Is My NAME"
print(len(example_string2))
slise_str1 = example_string2[0:4]
slise_str2 = example_string2[5:7]
slise_str3 = example_string2[8:10]
slise_str4 = example_string2[-4:]
print((slise_str1 + " " + slise_str2 + " " + slise_str3 + " "+ slise_str4).capitalize())
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip("*"))
print(example_string3.replace("*",""))

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"
print(example_string4.lower())

# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(var2.capitalize() +", " + var3.lower() + " " + var1.capitalize())

# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode())

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000