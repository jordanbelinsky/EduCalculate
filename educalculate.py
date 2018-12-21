"""
File Name: educalculate.py
Description: main application program
"""

# import #
from functions import *         # import calculations
from course_marks import *      # import preset marks and weights
marks = []
values = []
avg_num = 0                     # empty integer to calculate the numerator of the weighted average calculation
avg_den = 0                     # empty integer to calculate the denominator of the weighted average calculation

# TEST #

# states #
intro = True
num_check = False
allow_input = False
option_1 = False
option_2 = False

# intro state #
while intro:
    main_info()
    program_choice = input("type '1' or '2': ")
    if program_choice == "1":
        intro = False
        option_1 = True
        num_check = True
    elif program_choice == "2":
        intro = False
        option_2 = True
        allow_input = True

# program option 1 #
while option_1:
    print()
    print("option 1:")
    print()
    while num_check:
        mark_num = int(input("how many marks are you averaging: "))
        subject = input("what subject ('1' = math/'2' = other): ")
        input_type = input("what mark format ('1' = decimal/'2' = fraction): ")
        num_check = False
        allow_input = True

    # decimal input #
    while allow_input and input_type == "1":
        # math #
        if subject == '1':
            for i in range(mark_num):
                print()
                print("mark #"+str(i+1))
                section = math_sections[i]
                value = math_weights[i]
                print("enter the weighting: "+str(section)+" - "+str(value)+"%")
                values.append(value)
                mark = int(input("enter the value: "))
                marks.append(mark)
        # other #
        if subject == '2':
            for i in range(mark_num):
                print()
                print("mark #"+str(i+1))
                mark = int(input("enter the value: "))
                marks.append(mark)
                value = int(input("enter the weighting: "))
                values.append(value)
        allow_input = False
    option_1 = False

    # fraction input #
    while allow_input and input_type == "2":
        # math #
        if subject == '1':
            for i in range(mark_num):
                print()
                print("mark #"+str(i+1))
                section = math_sections[i]
                value = math_weights[i]
                print("enter the weighting: "+str(section)+" - "+str(value)+"%")
                values.append(value)
                mark_numerator = float(input("enter the fraction numerator: "))
                mark_denominator = float(input("enter the fraction denominator: "))
                mark = fraction_decimal(mark_numerator, mark_denominator)
                mark = mark*100
                print("calculated mark: "+str(round(mark, 2)))
                marks.append(mark)
        # other #
        if subject == '2':
            for i in range(mark_num):
                print()
                print("mark #"+str(i+1))
                mark_numerator = float(input("enter the fraction numerator: "))
                mark_denominator = float(input("enter the fraction denominator: "))
                mark = fraction_decimal(mark_numerator, mark_denominator)
                mark = mark*100
                print("calculated mark: "+str(round(mark, 2)))
                marks.append(mark)
                value = int(input("enter the weighting: "))
                values.append(value)
        allow_input = False
    option_1 = False

# program option 2 #
while option_2:
    print()
    print("option 2:")
    print()
    while allow_input:
        current_grade = int(input("what is your current grade (%): "))
        final_grade = int(input("what final mark would you like to reach (%): "))
        final_worth = int(input("what is your final exam worth (%): "))
        allow_input = False
    option_2 = False

# program output #
if program_choice == "1":
    output_1(mark_num, avg_num, avg_den, marks, values)
elif program_choice == "2":
    output_2(current_grade, final_grade, final_worth)
