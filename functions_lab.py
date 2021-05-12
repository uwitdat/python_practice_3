# 1:
print('|--------EX 1: ---------|')


def pokemon_contains(incoming_letter):
    if incoming_letter in "pokemon":
        return True
    else:
        return False


result1 = pokemon_contains('k')
print(result1)
result1 = pokemon_contains('l')
print(result1)


# 2:
print('|--------EX 2: ---------|')


def sum_two(a, b):
    answer = a + b
    return answer


result3 = sum_two(5, 6)
print(result3)
result4 = sum_two(5, 6)
print(result4)

# 3:
print('|--------EX 3: ---------|')


def multiply(num1, num2):
    answer = num1 * num2
    return answer


result5 = multiply(10, 10)
print(result5)
result6 = multiply(5, 6)
print(result6)


# 4:
print('|--------EX 4: ---------|')


def multiplication(a, b):
    my_answer = a*b
    print("Calculating...")
    return my_answer


print("Let's Multiply stuff...")
answer = multiplication(5, 6)
answer = str(answer)
print("The answer is..." + answer)

# 5
print('|--------EX 5: ---------|')


def subtract(num1, num2):
    result = num1 - num2
    return result


result1 = subtract(2, 1)
print(result1)

result2 = subtract(4, 2)
print(result2)

# 6
print('|--------EX 6: ---------|')


def greater_than_5(input):
    if input > 5:
        return True
    else:
        return False


res1 = greater_than_5(6)
print(res1)

res2 = greater_than_5(1)
print(res2)

# num 7
print('|--------EX 7: ---------|')


def sum_to(input):
    countdown = (list(range(1, input + 1)))
    return sum(countdown)


print(sum_to(6))
print(sum_to(10))
print(sum_to(20))


# num 8
print('|--------EX 8: ---------|')


def largest(list):
    sorted_list = sorted(list)
    return sorted_list[-1]


print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))


# num 9
print('|--------EX 9: ---------|')


def occurances(str1, str2):
    count = str1.count(str2)
    return count


print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# num 10
print('|--------EX 10: ---------|')


def product(*args):
    result = 1
    for num in args:
        result = result * num
    return result


print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))
print(product(4, 0.5, 10, 6))
