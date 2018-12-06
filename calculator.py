# Variables #
from functions import *
marks = []
values = []
avg_num = 0
avg_den = 0

# Application States #
intro = True
num_check = False
allow_input = False
option_1 = False
option_2 = False

# Preset Values #
math_weights = [5, 20, 20, 15, 5]
math_sections = ["CK", "KU", "APP", "TH", "COM"]

# Intro Screen #
while intro:
    print()
    print("Program Options:")
    print("1. Calculate My Total Mark Based On Marks")
    print("2. Calculate My Required Final Mark")
    program_choice = input("Please type '1' or '2': ")
    if program_choice == "1":
        intro = False
        option_1 = True
        num_check = True
    elif program_choice == "2":
        intro = False
        option_2 = True
        allow_input = True

# Option 1 #
while option_1:
    # Number of Marks Check #
    while num_check:
        mark_num = int(input("How many marks are you averaging: "))
        subject = input("What subject do these marks represent ('1' = Math/'2' = Other): ")
        num_check = False
        allow_input = True

    # Marks Input #
    while allow_input:
        if subject == '1':
            for i in range(mark_num):
                print()
                print("Mark #"+str(i+1))
                section = math_sections[i]
                value = math_weights[i]
                print("Enter the weighting: "+str(section)+" - "+str(value)+"%")
                values.append(value)
                mark = int(input("Enter the value: "))
                marks.append(mark)
        if subject == '2':
            for i in range(mark_num):
                print()
                print("Mark #"+str(i+1))
                mark = int(input("Enter the value: "))
                marks.append(mark)
                value = int(input("Enter the weighting: "))
                values.append(value)
        allow_input = False
    option_1 = False

# Option 2 #
while option_2:
    while allow_input:
        current_grade = int(input("What is your current grade (%): "))
        final_grade = int(input("What final mark would you like to reach (%): "))
        final_worth = int(input("What is your final exam worth (%): "))
        allow_input = False
    option_2 = False

# Output #
if program_choice == "1":
    print()
    print("Your weighted average is: "+str(calc_avg(mark_num, avg_num, avg_den, marks, values)))
    print()
elif program_choice == "2":
    print()
    print("You require a "+str(calc_final(current_grade, final_grade, final_worth))+"% on the final exam to finish with an "+str(final_grade)+"%.")
    print()
