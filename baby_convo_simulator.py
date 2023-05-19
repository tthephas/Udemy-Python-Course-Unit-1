# talking to a baby simulator

from random import choice


questions = ['why though?', 'why is the sea blue?', 'what is the moon?']

question = choice(questions)

answer = input(question).strip().lower()

while answer != 'just because':
    answer = input('Why?: ').strip().lower()

