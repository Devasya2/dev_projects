print('Hello Python')

# Asking the player's name
player = input('Enter name: ')

# Saying hello to the player
print('Hello', player, 'Good game', sep='|')

print()
print()

print('Are you ready to learn about Arithmetic Progression?')

import time
time.sleep(4)

print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)

print("Let's dive straight in!")

print()

ap = '2 6 10 14 18 22 .....'
print(ap)

print('What is the 16th term of the AP?')

time.sleep(4)

print('Hint: use formula a + (n - 1)d')

print('1st term')
a = int(input(''))

print('No. of terms')
n = int(input(''))

print('Difference between 2nd and 1st term')
d = int(input(''))

print('The answer is')
print()

print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)

answer = a + (n - 1) * d

print('Ans:', answer)

import pyfiglet

result = pyfiglet.figlet_format('Hope you had fun', font='bubble')
print(result)