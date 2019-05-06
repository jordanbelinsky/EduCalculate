"""
File Name: functions.py
Description: store functions to be called in the main program
"""

# intro screen information #
def main_info():
    #learn printf()
    print()
    print("educ[alcul]ate")
    print("a program written by jordan belinsky")
    print()
    print("program options:")
    print("1. weighted average")
    print("2. exam mark")

# average calculation #
def calc_avg(num_of_marks, numerator, denominator, markList, valueList):
    for i in range(num_of_marks):
        num = markList[i]*valueList[i]
        numerator += num
    for j in range(num_of_marks):
        den = valueList[j]
        denominator += den
    average = numerator/denominator
    return round(average, 2)

# exam mark calculation #
def calc_final(current, final, weight):
    decimal_weight = weight/100
    current_weight = 1 - decimal_weight
    required_mark = (final - current_weight*current)/decimal_weight
    return round(required_mark, 2)

# convert fraction to decimal #
def fraction_decimal(numerator, denominator):
    mark = numerator/denominator
    return mark

# weighted average output #
def output_1(mark_num, avg_num, avg_den, marks, values):
    print()
    print("your weighted average is: "+str(calc_avg(mark_num, avg_num, avg_den, marks, values))+"%.")
    print()

# final mark output #
def output_2(current_grade, final_grade, final_worth):
    print()
    print("you require a "+str(calc_final(current_grade, final_grade, final_worth))+"% on the final exam to finish with an "+str(final_grade)+"%.")
    print()