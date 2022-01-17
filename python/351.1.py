def DISPLAY(mystr): 
    L = len(mystr) 
    str2=' ' 
    str3=' ' 
    for i in range(0,L,1): 
         str2=str2+mystr[i] 
    for ch in str2: 
       if ch>='R' and ch<='U': 
            str3+='@' 
       elif ch.isupper(): 
            str3+=ch 
       else: 
           str3+=ch.lower() 
    return str3 
mystr="FiRST#tERM#ExAM" 
mystr=DISPLAY(mystr) 
print(mystr)
