import re

T = int(input())

def has_odd(T):
    for i in range(1, T+1):
        num = int(input())
        if(bool(re.match('.*[13579].*', str(num))) == False):
            print("Case #{}: {}".format(i, 0))
        else:
            minus_press = 0;
            plus_press = 0;

            largest_odd_digit, largest_odd_place = find_odd_by_place(num)
            even_plus_num = find_even_plus_num(num, largest_odd_digit, largest_odd_place)
            plus_press = (even_plus_num - num)

            #TODO find minus press
            minus_press = minus_even_num(num, largest_odd_place)
            if(minus_press < plus_press):
                print("Case #{}: num is {} = {}".format(i,num, minus_press))
            else:
                print("Case #{}: num is {} = {}".format(i, num, plus_press))

def find_odd_by_place(num):
    '''
    find odd digit from left to right
    '''
    odd_digits = ['1','3','5','7','9']

    counter = len(str(num))+1
    for digit in list(str(num)):
        counter-=1
        if digit in odd_digits:
            return int(digit), counter

def find_even_plus_num(num, largest_odd_digit, largest_odd_place):
    len_ = len(str(num))
    if(len_ == 1) :return num+1
    num_list = list(str(num))
    even_num = 0
    len_ -= 1
    for i in range((len_ + 1 - largest_odd_place)):
        even_num += (int(num_list[i])*10**(len_))
        len_ -= 1

    even_num += (largest_odd_digit+1)*10**(largest_odd_place-1)
    return even_num

def minus_even_num(num, largest_odd_place):
    length = len(str(num))
    start = length -largest_odd_place
    input_num = list(str(num))[start:]
    input_num = int(''.join(map(str, input_num)))
    even_num = 0
    step = 0
    total_step = 0
    for i in range(largest_odd_place):
        input_num -= step
        input_num = find_sub_num(input_num)
        step = minus_help(input_num)
        #print('{}, {}'.format(step, input_num))
        total_step += step
    return total_step

def minus_help(num):
    if len(str(num)) == 1:
        return 1

    num_list = list(str(num))

    result = num - (((int(num_list[0]) - 1)*10**(len(num_list)-1)) + int(str((len(num_list)-1) * '9')))
    return result

def find_sub_num(num):
    largest_odd_digit, largest_odd_place = find_odd_by_place(num)
    length = len(str(num))
    start = length -largest_odd_place
    input_num = list(str(num))[start:]
    input_num = int(''.join(map(str, input_num)))

    return input_num

has_odd(T)