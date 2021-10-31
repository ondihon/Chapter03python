def ispythagoras(a, b, c):
    if c**2==(a**2+b**2):
        print(f'a={a}, b={b}, c={c} -> True')
    else:
        print(f'a={a}, b={b}, c={c} -> False')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
ispythagoras(a, b, c)
