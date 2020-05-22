pet = ['kitten', 'mouse', 'hamster', 'parrot', 'shrimp']

from random import choice
from random import shuffle

quiz = choice(pet)
list_quiz = list(quiz)
shuffle(list_quiz)
for i in range(len(list_quiz)):
    print(list_quiz[i], end=' ')
print('\n')

answer = input('your answer:')
if answer == quiz:
    print("Hura")
else:
    print(":(")