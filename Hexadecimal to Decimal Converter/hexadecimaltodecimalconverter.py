def hex2dec(s):
    
    power = len(s)-1
    el = 0
    sm = 0
    n = 0
    
    for i in range(0, len(s)):     
       
        if s[i] == 'A':
            el = 10
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        elif s[i] == 'B':
            el = 11
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        elif s[i] == 'C':
            el = 12
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        elif s[i] == 'D':
            el = 13
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        elif s[i] == 'E':
            el = 14
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        elif s[i] == 'F':
            el = 15
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
        else:
            el = int(s[i])
            n = el * (16 ** power)
            sm = sm + n
            power = power - 1
     
    return sm
     
     
s = hex2dec(input())
print(s)
