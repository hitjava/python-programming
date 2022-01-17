def Aisha_181027_combination_of_table_arrangment(X,Y,D):
    TX=eval(input("Enter the no of short Tables TX :")) #user enters the no. of short tables
    TY=eval(input("Enter the no of long tables TY :"))  #user enters the no. of long tables
    empty_distance=eval(input("Enter the empty distance :")) #user enters the distance of empty space
    RD=D
   
    while empty_distance >0:  #since we don't know the exact distance we use while loop
            sum = empty_distance %Y+(D - empty_distance)%X
            if sum <RD:
               RD=sum
               TX=(D - empty_distance)//X
               TY =empty_distance//Y
            empty_distance = empty_distance - X
    print("number of short tables are (TX) : ",TX)#print statement for no. of short tables
    print("number of long tables are (TY) : ",TY)#print statement for no. of long tables
    print("remaining distace is (RD) : ",RD) #print the remaining distance
Aisha_181027_combination_of_table_arrangment(3,9,29)    
