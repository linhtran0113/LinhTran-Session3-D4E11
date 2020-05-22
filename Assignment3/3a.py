from random import shuffle
from getpass import getpass

quiz = getpass('')
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