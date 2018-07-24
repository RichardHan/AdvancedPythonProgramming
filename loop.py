# Loop - range 5
for x in range(5):
    print(x)
"""
     0 
     1
     2
     3
     4
"""

# Loop - Lists
fruits = ['apple', 'orange']
for fruit in fruits:
    print(fruit)
"""
apple
orange
"""

# Loop - Dictionaries
countries = {
    'TW': 'Taiwan',
    'PH': 'Philippines'
}
for key, value in countries.items():
    print('%s: %s' % (key, value))
"""
TW: Taiwan
PH: Philippines
"""

# While Loop
x = 0
while x < 3:
    print (x)
    x += 1
"""
0
1
2
"""

# List Comprehensions
#  %:  Modulus operator, it is used for remainder division on integers
odds = []
for x in range (10):
    if x % 2:
        odds.append(x)
print (odds)
"""
[1, 3, 5, 7, 9]
"""
