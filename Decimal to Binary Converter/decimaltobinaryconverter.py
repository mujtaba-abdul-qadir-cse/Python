def dec2bin(n):
    bin = []
    s = ""
    
    while n != 0:  
        
        digit = n % 2
        
        bin.append(digit)
        
        n = n // 2
    
    bin.reverse()
    
    for i in bin:
        s = s + str(i)
    
    return s
        
        
    
binarynum = dec2bin(int(input()))
print(binarynum)
        
        

