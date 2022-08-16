num = 1

while num <= 20:
    print(num)
    num += 1
    
value = int(input('Enter a number between 20 and 30, inclusive: '))

while value < 20 or value > 30:
    value = int(input('Invalid value. Please reenter: '))


print('The number you entered is', value)
    
full_str = ''
read_another = 'y'
while read_another.lower() =='y':
    str = input('Enter a string: ')
    full_str += str
    read_another = input('Read another string (y or n)? ')
    
print(full_str)

print()
    
full_str = ''
str = 'xxx'

while str.lower() != 'quit':
    str = input('Enter a string (or "quit"): ')
    if str.lower() != 'quit':
        full_str += str
    
    
print(full_str)
    
    
    

print('All done')