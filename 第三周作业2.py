def Digitsum(n):
    if n<10:
        return n 
    else:
        return n%10+Digitsum(n//10)

print(Digitsum(114))
