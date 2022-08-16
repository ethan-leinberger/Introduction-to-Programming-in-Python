''' 
Project 4 - NATO Alphabet - Spring 2022  
Author: Ethan Leinberger Lethan20

This program reads 2 files. One that is the NATO alphabet,
and one that has a list of identifiers to spell out using the
NATO alphabet. It validates and categorizes each identifier and prints it


I have neither given or received unauthorized assistance on this assignment. 
Signed:  Ethan Leinberger 
'''

#This reads the alphabet and creates a dictionary. Adds two special
#characters, space, and dash
def get_dictionary():
    o = open('alphabet.txt' , 'r')
    d = {}
    for line in o.readlines():
        line = line.strip()
        line = line.split()
        d[line[0]] = line[1]
    o.close()
    d[" "] = "Space"
    d["-"] = "Dash"
    return d

#this validates the identifier based on length, and returns the category
def categorize_identifier(identifier):
    length = len(identifier)
    if length >= 5 and length <= 8:
        return 'TAG'
    elif length == 10:
        return 'BOAT'
    elif length == 17:
        return 'VIN'
    return 'INVALID'

#this returns a string representing the spelling of the identifier
#from the parameters
def get_spelling(dictionary, identifier):
    spell = ''
    for i in identifier:
        spell += dictionary[i]
        spell += ' '
    spell = spell[:len(spell) - 1]
    return spell

#Thid function is the driver of the program that runs all of the
#previously written code
def main():
    d = get_dictionary()
    o = open('identifiers.txt', 'r')
    cvalid = 0
    cinvalid = 0
    for line in o.readlines():
        line = line.strip()
        line = line.upper()
        validate = categorize_identifier(line)
        if validate == 'INVALID':
            print(validate + ':', line)
            print('\n')
            cinvalid += 1
        else:
            print(validate + ':', line)
            print(get_spelling(d, line))
            print()
            cvalid += 1
    print('Number of identifiers processed = ', cvalid)
    print('Number of invalid identifiers = ', cinvalid)
    
if __name__ == '__main__': 
    main()
    
    
    
    
    