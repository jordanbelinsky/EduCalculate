def calc_avg(num_of_marks, numerator, denominator, markList, valueList):
    for i in range(num_of_marks):
        num = markList[i]*valueList[i]
        numerator += num
    for j in range(num_of_marks):
        den = valueList[j]
        denominator += den
    average = numerator/denominator
    return round(average, 2)

def calc_final(current, final, weight):
    decimal_weight = weight/100
    current_weight = 1 - decimal_weight
    required_mark = (final - current_weight*current)/decimal_weight
    return round(required_mark, 2)