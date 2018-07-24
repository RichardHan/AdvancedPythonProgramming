# Loop - range 5
for x in range(5):
    print(x)

# Loop - Lists
fruits = ['apple', 'orange']
for fruit in fruits:
    print(fruit)

# Loop - Dictionaries
countries = {
    'TW': 'Taiwan',
    'PH': 'Philippines'
}
for key, value in countries.items():
    print('%s: %s' % (key, value))

# While Loop
x = 0
while x < 10:
    print (x)
    x += 1

# List Comprehensions
#  %: Modulus operator, it is used for remainder division on integers
odds = [ x for x in range(10) if x % 2]
print ("odds:")
print ([ x for x in range(10) if x % 2])

odds = []
for x in range (10):
    if x % 2:
        odds.append(x)
print (odds)
