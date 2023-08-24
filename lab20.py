#!/usr/bin/env python3
""" Alta3 Research | Lists Challenge """

# part1 put this list in your code
wordbank= ["indentation", "spaces"]

# part2 put this list in your code
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# part3 add a line of code that appends the integer 4 to the list wordbank
wordbank.append(4)

# part4 include an iput asking for a number between 0 and 20. save this as the variable num
num= input("Pick a student number!")

# part5 remember that input() always returns a string... convert num into an integer!
num= int(input("Pick a student number!"))

# part5a Use the integer num to slice one of the elements from ths list tlgstudents. Save the name you return as the variable student_name.
choice= int(input("Pick a student number!"))
student_name= tlgstudents[choice]

# part6 using elements from the tlgstudents list and the student_name string, print this output
#<student_name> always uses <4> <spaces> to indent.
# "4" and "spaces" should come from wordbank!


# import random module
import random

def main():
    
    # enter variable data
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 
                  'Craig', 'Deja', 'Elihu', 'Eric', 
                  'Giovanni', 'James', 'Joshua', 'Maria', 
                  'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 
                  'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    # print the tlg list as shown above. This helps to compare differences later implemented.
    print(tlgstudents)
    
    # append the integer 4 to the wordbank list and then print the new list
    wordbank.append(4)
    print(wordbank)
    
    # for Bonus 2. Student name printed out below is related to input from user.
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]
    
    
    print(f"Your unfortunate victim is {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
    
    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()

