def pole(a, b=0):
    if b:
        pole = a * b
    else:
        pole= a **2
    return pole

print(pole(2, 3))
print(pole(2))
#