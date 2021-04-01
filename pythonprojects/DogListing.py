# Quick listing program, lists dog names.
#
#
# - Bentley 8/3/2020

dogNames = []
while True:
    print('Enter the name of a dog ' + str(len(dogNames) + 1) +
    ' (Or enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    dogNames = dogNames + [name] # list concatenation
print('The dog names are:')
for name in dogNames:
    print(' ' + name)

