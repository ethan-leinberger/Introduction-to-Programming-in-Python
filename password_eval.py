'''
Example from the Week of 1/31.
A program that evaluates the quality of passwords read from
the user.
Demonstrates function definitions and if statements.
'''
def check_length(password):
    ''' Returns a score based on the password's length.
    Parameters:
        password - the password to evaluate
    Return: a score from 1 to 3. '''
    
    if len(password) < 8:
        length_score = 1
    elif len(password) < 12:
        length_score = 2
    else:
        length_score = 3
    return length_score
def check_case(password):
    ''' Returns a score based on the password's use of
    upper and lower case letters.
    Parameters:
        password - the password to evaluate
    Return: a score of 1 if their are only lowercase or
    uppercase letters used and 2 otherwise. '''
    
    if password.islower() or password.isupper():
        case_score = 1
    else:
        case_score = 2
    return case_score
def check_content(password):
    ''' Returns a score based on the content of the password.
    Parameters:
        password - the password to evaluate
    Return: a score of 1 if all characters are alphabetic,
    2 if they are all alphanumeric, and 3 if it includes
    special characters. '''
    
    if password.isalpha():
        content_score = 1
    elif password.isalnum():
        content_score = 2
    else:
        content_score = 3
    return content_score
def print_results(score):
    ''' Prints the final results of the password evaluation.
    Parameters:
        score - the overall score for the password
    Return: none '''
    
    print('Overall Score:', score)
        
    if score <= 5:
        print('That password is weak!')
    elif score <= 7:
        print('That password is acceptable.')
    else:
        print('That password is strong!')
   
def main():
    ''' The main driver of the password evalutor. Repeatedly
    reads a password from the user to evaluate. Combines
    scores based on length, case, and content to draw a
    final conclusion.
    Parameters: none
    Return: none '''
    print('Welcome to the Password Evaluator!')
    print()
    password = input('Enter a password or "q" to quit: ')
    while password.lower() != 'q':
        score = check_length(password)
        score += check_case(password)
        score += check_content(password)
        
        print_results(score)
        
        print()
        password = input('Enter a password or "q" to quit: ')
    print()
    print('Thanks for using the Password Evaluator!')
# Call the main function.
if __name__ == '__main__':
    main()
    
for val in range(5, 10):
    print('wow')
    
    
    
    side = int(input('Enter side length #1: '))
    while side <= 0:
        side = int(input('Invalid value. Please reenter: '))
    return side

while side1 != 1 or side2 != 2 or side3 !=3:
        side= input('Invalid value. Please reenter: ')
    if side==1:
        return side1
    if side ==2:
        return side2
    if side == 3:
        return side3
    return -1



while side1<=0 or side2<=0 or side3<=0:
        if side1<=0:
            side1=int(input('Enter side length #1: '))
            while side1<=0:
                side1 = int(input('Invalid value. Please reenter: '))
        if side2<=0:
            side2=int(input('Enter side length #1: '))
            while side2<=0:
                side2 = int(input('Invalid value. Please reenter: '))
        if side3<=0:
            side3=int(input('Enter side length #1: '))
            while side3<=0:
                side3 = int(input('Invalid value. Please reenter: '))
                
                
                
side1 == side2 and side1 + side2 >= side3 and side2 + side1 >= side3: