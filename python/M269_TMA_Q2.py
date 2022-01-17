prices =[]
profit=0
buy=prices[0]
profit=0
sell=0
sdate=0

for i in range(len(prices)):
 
    temp = prices[i]
    if tem<buy:
        {
                buy == temp
                buydate = i+1
        }
    elif temp- buy> profit:
        {
                profit = temp-buy
                sell=temp
                sdate=i+1
        }
    print("buying date:  day ", buydate: ", at the price of " , buy, "$")
    print("selling date:  day ",sdate: ", at the price of " , buy, "$")
    print("maxium profit : " ,profit , "$")
prices =[300, 450, 720, 90,30,50,900,500,70]
