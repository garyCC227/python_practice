import time
##
t1 = time.time()

t = int(input())

def has_odd(t):
    for i in range(1, t+1):
        num = int(input())
        if is_existed(num) == False:
            print ("Case #{}: {}".format(i, 0))
        else:
            plus_couter = 0
            minus_couter = 0
            plus_num = num
            minus_num = num
            while True:
                plus_couter +=1
                minus_couter +=1
                plus_num+=1
                minus_num-=1
                if is_existed(plus_num) == False:
                    break
                elif is_existed(minus_num) == False:
                    break

            if plus_num < minus_num:
                print ("Case #{}: {}".format(i, plus_couter))
            else:
                print ("Case #{}: {}".format(i, minus_couter))


def is_existed(num):
    odd = ['1','3','5','7','9']
    for e in odd:
        if e in str(num):
            return True

    return False

has_odd(t)

t2 = time.time()

print(t2-t1)
