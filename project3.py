import random
''' 
Project 3 - Luck of the Draw - Spring 2022  
Author: Ethan Leinberger Lethan20

This program will randomly pick today's winning numbers and the superball value.
It will then read a set of customer entries from a data file and determine how many
of the entries are winners. 

I have neither given or received unauthorized assistance on this assignment. 
Signed: Ethan Leinberger 
'''

#this creates a list determining the winning numbers at random
def pick_winning_numbers(minimum, maximum, count):
    win_list = [*range(minimum, maximum + 1)]
    random.shuffle(win_list)
    return win_list[:count]

#this function picks the superball value at random
def pick_superball(minimum, maximum):
    return random.choice(range(minimum, maximum + 1))

#accepts list of strings and returns list of integers corresponding
def convert_list_to_integers(win_list):
    new_list = []
    for i in win_list:
        new_list.append(int(i))
    return new_list

#compares winning list to the numbers that the customer enters
#does not take superball into account
def count_matches(l1, l2):
    matches = 0
    for i in l1:
        if i in l2:
            matches += 1
    return matches

#main program
#picks and prints winning numbers 
#reads the customer picks file and it loops through those user entries
#adds to the matches to find total numbers.
def main():
    win_numbers = pick_winning_numbers(1, 9, 4)
    superball = pick_superball(1, 9)
    
    print("Python Pick 4 Lottery Results")
    print()
    print("Today's winning numbers:" , win_numbers)
    print("Today's superball:", superball)
    print()
    with open("customer_picks.txt", "r") as file:
        line = file.readlines()
        super_entries = 0
        three_matches = 0
        four_matches = 0
    #i don't know how to not use readlines 
    print("\nNumber of entries:", len(line))
    for l in line:
        matches = 0
        superball_entry = False
        entry = l.split()
        
        if len(entry) == 5:
            super_entries += 1
            entry = entry[:-1]
            superball_entry = True
        
        entry = convert_list_to_integers(entry)
        matches = count_matches(entry, win_numbers)
        
        if superball_entry == True and superball in win_numbers and superball not in entry:
            matches += 1
        if matches == 3:
            three_matches += 1
        elif matches == 4:
            four_matches +=1
    print("Number of entries that used superball:", super_entries)
    print("Number of entries that matched 3 numbers:", three_matches)
    print("Number of entries that matched 4 numbers:", four_matches)
        
        
    
if __name__ == '__main__': 
    main()