import math
''' 
Project 2 - Name That Triangle - Spring 2022  
Author: Ethan Leinberger Lethan20

Describe the program here. 

I have neither given or received unauthorized assistance on this assignment. 
Signed:  Ethan Leinberger 
'''

#gets sides and returns them
def get_side(side):
    side1=0
    side2=0
    side3=0
    if side1<=0 or side2<=0 or side3<=0:
        if side1<=0:
            side=int(input('Enter side length #1: '))
            while side<=0:
                side = int(input('Invalid value. Please reenter: '))
        if side2<=0:
            side=int(input('Enter side length #2: '))
            while side<=0:
                side = int(input('Invalid value. Please reenter: '))
        if side3<=0:
            side=int(input('Enter side length #3: '))
            while side<=0:
                side = int(input('Invalid value. Please reenter: '))

#categorizes triangle as either equilateral, isosceles, or scalene
def categorize_triangle(side1, side2, side3):
    if side1==side2==side3:
        return "equilateral"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "isosceles"
    else:
        return "scalene"
       
#computes the perimeter and then the area of the triangle
def compute_area(side1, side2, side3):
    s=(float(side1 + side2 + side3) / 2)
    area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return(area)

#prints the results in the correct format
def print_results(category, area):
    category = categorize_triangle(input, input, input)
    area = compute_area(input, input, input)
    if category == "scalene":
        print()
        print('That is a', category, 'triangle with an area of', area)
    else:
        print()
        print('That is an', category, 'triangle with an area of', area)
    
#calls all of the previous functions to allow the evaluator to work properly
def main():
    print("Welcome to the Triangle Evaluator!")
    get_side(input)
    print()
    print_results(input, input)
    print()
    process_another = input('Process another triangle (y or n)? ')
    print()
    while process_another.lower() =='y':
        get_side(input)
        print_results(input,input)
        print()
        process_another = input('Process another triangle (y or n)? ')
        print()
    print('Thanks for using the Triangle Evaluator!')

#calls the main function so the evaluator prints 
if __name__ == '__main__': 
    main()