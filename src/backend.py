def difference(r_temp) :
     return abs(r_temp - 24)

def solving(numbers):
    op_counter = 3
    numbers = list(map(int, numbers))
    numbers.sort(reverse = True)
    r_temp = numbers[0]
    result = [str(numbers[0])]
    del numbers[0]
    
    while (difference(r_temp) != 0) and (op_counter != 0):
        diff_temp = 0
        op_temp = ''
        for n in numbers:
            diff_temp = difference(r_temp + n)
            op_temp = '+'
            if difference(r_temp - n) < diff_temp:
                diff_temp = difference(r_temp - n)
                op_temp = '-'
            if difference(r_temp * n) < diff_temp:
                diff_temp = difference(r_temp * n)
                op_temp = '*'
            if difference(r_temp / n) < diff_temp:
                diff_temp = difference(r_temp / n)
                op_temp = '/'
            result.append(op_temp)
            result.append(str(n))
            if (op_temp == '+'): r_temp += n
            elif (op_temp == '-'): r_temp -= n
            elif (op_temp == '*'): r_temp *= n
            elif (op_temp == '/'): r_temp /= n
            op_counter -= 1

    if (result[5] == '*' or result[5] == '/') and (result[3] == '+' or result[3] == '-'):
        result.insert(0, '(')
        result.insert(6, ')')
    elif (result[3] == '*' or result[3] == '/') and (result[1] == '+' or result[1] == '-'):
        result.insert(0, '(')
        result.insert(4, ')')

    expression = ''.join(result) + '=' + str(r_temp)

    return expression