table1 = row(std_List,1,10)

table2 = cols(table1,0,5)

table3 = to_float(table2)
print(table3)
print()

tableCA = []
for x in table3:
    ca = x[1]+ x[2]
    x[3] = ca
    tableCA.append(x)
print(tableCA)
print()

tableLG = []
for x in tableCA:
    ca=x[3]
    final = x[4]/2
    if ca<15 or final<20:
        x[5] = "F"
    else:
        finalGrade = ca + final
        if finalGrade>=90:
            x[5]="A"
        elif finalGrade >= 77:
            x[5]="B"
        elif finalGrade >= 65:
            x[5]="C"
        elif finalGrade >= 50:
            x[5]="D"
        else:
            x[5]="E"
    tableLG.append(x)       
