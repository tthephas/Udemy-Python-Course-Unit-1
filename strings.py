# Ask user for name
name = input("What is your name?: ")
# Ask user for age
age = input("How old are you?: ")

# Ask user for city
city = input("What city do you live in?: ")

# Ask user what they enjoy doing
hobby = input("What is your favorite hobby?: ")

print(name)
print(age)
print(city)
print(hobby)

# Create the output text 
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, hobby)

# Print the output to the screen

print(output)




