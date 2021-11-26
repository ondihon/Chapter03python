c = [0, 1, 2, 3, 4, 5, 6, 7]
d = [2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 0
def lol(x, y):
    e = []
    l = len(c)    
    while True:
        l -= 1
        k = c[x] + d [y]
        e = e + [k]
        x += 1
        y += 1
        if l == 0:
            break
    return e
            
lol(x, y)
e = lol(x, y)
print(str(e))
