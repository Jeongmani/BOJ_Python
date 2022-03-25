def solution(numbers):
    str_numbers=[]
    for i in numbers:
        str_numbers.append(str(i))
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(str_numbers)))
   