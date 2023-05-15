# Health potion exercise and game
# Use numbers and python random number generator
import random

health = 50
# three modes, 1-3, easy medium and hard
difficulty = 1

# get random integer between 2 numbers
random.randint(10,20)

# create variable called potionhealth and have it be a random number between 25 and 50
potion_health = int(random.randint(25,50) /difficulty)

# store what health is when potion health is added
health = health + potion_health

print(health)




