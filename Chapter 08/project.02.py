mydata = [1, 2, 3, 4, 5]

def rerata(*mydata):
    i = sum(mydata)
    j = len(mydata)
    a = i/j
    return a
rerata(*mydata)
a = rerata(*mydata)

def terbesar(*mydata):
    b = max(mydata)
    return b
terbesar(*mydata)
b = terbesar(*mydata)

def terkecil(*mydata):
    c = min(mydata)
    return c
terkecil(*mydata)
c = terkecil(*mydata)

data = [a, b, c]
print(data)











