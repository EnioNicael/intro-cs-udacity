# Strings and numbers

name = 'Yoda'

print(f'Hello {name}') # Hello Yoda
print('!' * 5) # !!!!!


# Indexing Strings
# <string>[<expression>]

print('udacity'[0]) # u
print('udacity'[1 + 1]) # a
name = 'Yoda'
print(name[0]) # Y


# Selecting sub-sequences
#
#            start           stop
# <string>[<expression> : <expression>]]
#            number          number

word = 'udacity'
print(word[3:3]) # ""
print(word[:3]) # uda
print(word[3:]) # city
print(word[2:6]) # acit
print(word[:]) # udacity