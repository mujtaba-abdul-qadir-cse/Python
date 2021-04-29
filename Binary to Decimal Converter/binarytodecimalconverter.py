# This programs converts a binary string to a decimal integer.

def bin2dec(s):
    l = len(s) - 1
    num = 0
    for i in s:
        num = num + int(i) * 2 ** l
        l = l - 1

    return num


n = bin2dec(input())
print(n)
