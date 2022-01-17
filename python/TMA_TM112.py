from turtle import*
m=[1,2,3,4,5,6,7,8,9,10,11,12]
s=[120,110,80,66,66,45,40,20,45,75,95,130]
goto(180,0)
goto(0,0)
goto(0,150)
goto(0,0)
for i in range(len(s)):
    if m[i]%2==0:
      goto(m[i]*15,s[i])
      dot(9,"orange")
    else:
       goto(m[i]*15,s[i])
       dot(9,"blue")
    write(m[i],False,"center","Bold")
ht()   


