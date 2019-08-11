#!/usr/bin/python3
import copy

def main(T):
    for i in range(1, T+1):
        N,Q = map(int, input().split(' ')) # N is block, Q is question
        array = input()
        yes = 0;
        for j in range(1, Q+1):
            L,R = map(int, input().split(' '))
            #print(L,R)
            #temp = copy.deepcopy(array[L-1:R-1])
            #print(array[L-1:R]);
            if (palindrome(array[L-1:R])):
                #print(str(j)+ " is right")
                yes+=1;

        print("Case #{}: {}".format(i, yes))



def palindrome(str):
    if (is_palindrome(str)):
        #print("check direct")
        return True;

    hash = {};
    for i in range(len(str)):
        if str[i] in hash.keys():
            hash[str[i]]+=1
        else:
            hash[str[i]] = 1;
    #print(hash)
    odd = 0;
    for value in hash.values():
        if value % 2 != 0:
            odd+=1;

    if odd > 1:
        return False;
    return True;

def is_palindrome(str):
    mid = len(str)//2;
    neg = -(mid+1)
    return ( str[0:mid] == str[-1:neg:-1]  )

if __name__ == '__main__':
    T = int(input())

    main(T)
    #print(is_palindrome(T))
