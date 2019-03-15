def reverse(x):
    output = list(x)
    output = output[::-1]
    return ''.join(output)

def generator():
    for x in range(5):
        yield x
if __name__ == '__main__':
    #print(reverse('first'))
    my_ge = generator()
    for e in my_ge:
        print(e)