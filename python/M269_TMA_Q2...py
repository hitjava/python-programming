def Aisha_181027(prices) :
 
  buy_price=eval(input("enter the buying price"))  #user enters the buying price
  sell_price=eval(input("enter the selling price")) #user enters the selling price
  buy_date=eval(input("enter the date of purchase")) #user enters the buying date
  sell_date=0   #selling date
  profit=0      # variable that carries the value of the profit
  for i in range (len (prices)):
     temp = prices[i]
     if prices[i]> temp:   #check if the prices[i] is greater than temp
       prices[i]=temp      # if yes the change the value of the temp
     elif temp-buy_price<profit:
            buy_price=temp
            buy_date=i+1
     elif temp-buy_price>profit:
            sell_price = temp
            sell_date=i+2
  profit=sell_price-buy_price          
  #return(buy_price, buy_date, sell_price,sell_date, profit)       
  print("buying date:",buy_date, ", at the price of:",buy_price,"$")
  print("selling date:",sell_date, ", at the price of:",sell_price,"$")
  print("profit earned :",profit,"$")
prices=[320,45,70,90,70]
Aisha_181027(prices)
