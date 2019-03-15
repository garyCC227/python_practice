def gensquares(N):
    output = []
    for num in range(N):
        #yield num**2
        output.append(num**2)
    return output

gensquares(10)